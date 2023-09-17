from django.shortcuts import render
from Glover_main.views import *

# Create your views here.
def main(request):
	return render(
		request,
		'Glover_back/main.html'
	)
 
def user_page(request):
	return render(
		request,
		'Glover_back/user_page.html'
	)

def manager_page(request):
	return render(
		request,
		'Glover_back/manager_page.html'
	)