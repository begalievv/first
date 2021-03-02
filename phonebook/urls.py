from django.urls import path

from phonebook.views import show_list

urlpatterns = [
	path('', show_list, name='main_list'),
]
