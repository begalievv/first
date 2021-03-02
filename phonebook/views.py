from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from phonebook.models import PhoneBook



def show_list(request):

	search_query = request.GET.get("search", "")

	if search_query:
	    query = PhoneBook.objects.filter(Q(name__icontains=search_query) | Q(number__icontains=search_query))
	else:
	    query = PhoneBook.objects.all()


	paginator = Paginator(query, 4)
	page_number = request.GET.get("page", 1)

	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = "?page={}".format(page.previous_page_number())
	else:
		prev_url = ""

	if page.has_next():
		next_url = "?page={}".format(page.next_page_number())
	else:
		next_url = ""

	context = {
		'phonebooks': page.object_list,
		"page_object": page,
		"is_paginated": is_paginated,
		"next_url": next_url,
		"prev_url": prev_url,
		'search_query': search_query
	}

	return render(request, 'base.html', context)

