from django.shortcuts import render

def home(request):
	return render(request, "base/home.html") # from import render
	#render takes request parameter in this func
	#base/home.html: specifying the app that the template is coming from