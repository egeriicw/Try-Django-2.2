from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
	my_title = "Home."
	context = {"title": my_title}

	if request.user.is_authenticated:
		context = {"title": my_title, "mylist": [1, 2, 3, 4, 5]}	
#	doc = "<h1>{title}</h1>".format(title=title)
#	django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)
	return render(request, 'home.html', context)

def contact_page(request):
	return render(request, 'contact.html', {"title": "Contact Us."})
	#return HttpResponse("<h1>Contact Page</h1>")

def about_page(request):
	return render(request, 'about.html', {"title": "About Us."})
#	return HttpResponse("<h1>About Us</h1>")

def example_page(request):
	context = {"title": "Example Page"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(rendered_item)