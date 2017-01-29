from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Nr_ST, Owner

class StoreListView(ListView):
    model = Nr_ST 


class CreateProduct(CreateView):
	model = Nr_ST
	template_name = 'store/create_product.html'
	fields = ['nr_product', 'name_product', 'date_of_acceptance', 'owner','photo']

	def get_success_url(self):
		return reverse('store-list')

class CreateOwner(CreateView):
	model = Owner
	template_name = 'store/create_owner.html'
	fields = ['first_name', 'last_name', 'nick_name']

	def get_success_url(self):
		return reverse('list-owner')


class ListOwners(ListView):
	model = Owner
	fields = ['first_name', 'last_name', 'nick_name']
	template_name = 'store/owner_view.html'


class EditOwner(UpdateView):
	model = Owner
	fields = ['first_name', 'last_name', 'nick_name']
	template_name = 'store/edit-owner.html'

	def get_success_url(self):
		return reverse('list-owner')

class DeleteOwner(DeleteView):
	model = Owner
	template_name = 'store/delete-owner.html'
	success_url = reverse_lazy('list-owner')

class DetailProductView(DetailView):
	model = Nr_ST
	template_name = 'store/product-detail.html'
