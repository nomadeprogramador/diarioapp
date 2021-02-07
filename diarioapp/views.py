from django.shortcuts import render,redirect,get_object_or_404
from .forms import LoginForm,DiarioForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .models import Diario
from django.contrib.auth.decorators import login_required
import time 
# Create your views here.
@login_required(login_url='login')
def detalhes_usuario(request):
    diario_qntd=Diario.objects.filter(user=request.user).count()
    data_atual=time.strftime('%d/%m/%y',time.localtime())
    context={
        'diario_quantidade':diario_qntd,
        'data_atual':data_atual,
    }
    return render(request,'diario/detalhes.html',context)

@login_required(login_url='login')
def escrever_diario(request):
    if request.POST:
        form=DiarioForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user=request.user
            form.save()
            return redirect('index')
    form=DiarioForm()
    context={
        'form':form,
    }
    return render (request,'diario/escrever.html',context)

#Editar diario
@login_required(login_url='login')
def editar_diario(request,id):
    diario=get_object_or_404(Diario,id=id)
    form=DiarioForm(instance=diario)
    if request.POST:
        form=DiarioForm(request.POST,instance=diario)
        if form.is_valid():
            form.user=request.user
            form.save()
            return redirect('index')
    context={
        'form':form
    }    
    return render (request,'diario/editar.html',context)
#excluir
@login_required(login_url='login')
def excluir_diario(request,id):
    diario=get_object_or_404(Diario,id=id).delete()
    return redirect('index')



def fazer_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    diario = Diario.objects.filter(user=request.user)
    context={
        'diario':diario,
    }
    return render(request,'diario/index.html',context)


def fazer_login (request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect ('index')
            else:
                return HttpResponse ('<h1> usuario ou senha invalido </h1> ')

    form=LoginForm()
    context={
        'form':form,
    }
    return render (request,'diario/login.html',context)