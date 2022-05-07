from django.shortcuts import render
from Revisionapp.models import visitors, UserProfileInfo
from Revisionapp.forms import Form_visitors, UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    context_dict = {'text':'Moo that"s a cow, man oh man!','number':120}
    return render(request,'Revisionapp/index.html',context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def formpage(request):
    visitors_list = visitors.objects.order_by('visitorage')
    visitors_dict = {'vk':visitors_list,'just':'Just checking bruv!'}
    return render(request,'Revisionapp/formpage.html',context=visitors_dict)

def usersignup(request):
    form = Form_visitors()

    if request.method == 'POST':
        form = Form_visitors(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return formpage(request)
    return render(request,'Revisionapp/usersignup.html',{'form':form})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'Revisionapp/registration.html',{'user_form':user_form,
                                                            'profile_form':profile_form,
                                                             'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and Password: {}'.format(username,password))
            return HttpResponse('Invalid login details provided!')
    else:
        return render(request,'Revisionapp/login.html',{})
