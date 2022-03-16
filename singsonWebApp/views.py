from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class indexView(View):
	def get(self, request):
		return render(request,'index.html', {})
