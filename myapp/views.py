from myapp.models import Staff, Depart
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

#class HomeView(TemplateView):
	#template_name = 'index.html'

def index(request):
	#return render(request, "index.html")
	if request.method == "GET":
		staff_list = Staff.objects.all()
		dpt_list = Depart.objects.all()
		template = loader.get_template('index.html')
		context = {
		'staff_list' : staff_list,
		'dpt_list' : dpt_list
		}
		return HttpResponse(template.render(context, request))
	elif request.method == "POST":
		form = addform(request.POST)
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		home_add = request.POST['home_add']
		depart = request.POST['depart']
		phone_number = request.POST['phone_number']
		return HttpResponseRedirect('Staff Added')




			
#def Staff(request):
#	if request.method == "GET":
#		x = staff.objects.all()
#		template = loader.get_template('index.html')
#		context = {
#			'x' : x
#		}
#	return HttpResponse(template.render(context, request))

#def dept(request):
	#return render(request, 'dept.html')

#	if request.method =="GET":
#		staff_list = staff.objects.all()
		#template = loader.get_template('index.html')
		#context = {
			#'staff_list' : staff_list
		#}
#	return HttpResponse('Hello World!')







# Create your views here.
