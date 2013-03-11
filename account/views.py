from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
	return render(request, "index.html", {})

def login(request):
	if request.method == "GET":
		return render(request, "login.html", {})
	elif request.method == "POST":
		return login_user(request)
	else:
		raise "Invalid request method"

def login_user(request):
	user = ahtenticate(username=request.POST.get("username"), password=request.POST.get("password"))
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			next

def logout(request):
	logout(request)
	return redirect('index', permenant=True)
