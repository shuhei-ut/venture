from django.shortcuts import render,render_to_response
from django.contrib.auth.forms import UserCreationForm

def register(request):
   if request.method == 'GET':
       return render(request, 'register.html', {'form':UserCreationForm()})
   elif request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return render_to_response('register_done.html', {'username':form['username'].value()})
       else:
           return render(request, 'register.html', {'form':form})
   else:
       return HttpResponseForbidden
