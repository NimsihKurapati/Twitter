
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import View
from django.contrib.auth import authenticate, login, get_user_model
from .forms import UserForm, TweetForm
from django.http import HttpResponse
User = get_user_model()

# Create your views here.
def IndexView(request,):
    if request.user.is_authenticated:
        obj = T_user.objects.get_or_create(user_name = request.user, user_email = request.user.email)
        allusers = User.objects.exclude(username = request.user)

        if request.method == 'POST':
            form = TweetForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return redirect('/index')
        else:
            form = TweetForm()
            object = Tweet.objects.filter(user=request.user).order_by('-date_time')
        return render(request, 'TwitterApp/index.html',{'form':form, 'object':object,'obj':obj, 'allusers':allusers })
    else:
        return redirect('/')

def RetweetView(request,username,uuid):
    object = get_object_or_404(Tweet,uuid=uuid)
    obj = Tweet()
    obj.user = request.user
    obj.original = username
    obj.content = object
    obj.RT = True
    obj.location = object.location
    obj.save()

    return redirect('/profile_view/'+username+'/')



def RetweetCommentView(request,username,uuid):
    if request.user.is_authenticated:
        object = get_object_or_404(Tweet, uuid=uuid)
        obj1 = Tweet.objects.filter(uuid=uuid)
        if request.method == 'POST':
            obj = Tweet()
            obj.user = request.user
            obj.original = username
            obj.content = object
            obj.RT = True
            obj.location = object.location
            obj.comment = request.POST['comment']
            obj.save()
            return redirect('/index',{'obj1':obj1})
        return render(request, 'TwitterApp/retweet.html', {'obj1':obj1})



def ExploreView(request,):
    return render(request, 'TwitterApp/explore.html')

def NotificationView(request,):
    return render(request, 'TwitterApp/notification.html')

def MessageView(request,):
    return render(request, 'TwitterApp/messages.html')

def BookmarkView(request,):
    return render(request, 'TwitterApp/bookmarks.html')

def ListView(request,):
    return render(request, 'TwitterApp/lists.html')

def ProfileView(request,):
    if request.user.is_authenticated:
        user_details = T_user.objects.filter(user_name = request.user)
        tweet_details = Tweet.objects.filter(user = request.user)
        return render(request, 'TwitterApp/profile.html',{'tweet_details':tweet_details, 'user_details':user_details})
    else:
        return redirect('/')

def LoginView(reqest,):
    return render(reqest, 'TwitterApp/login.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'TwitterApp/register.html'

    #display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credintials are correct
            user = authenticate(username = username, password = password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/index')

        return render(request, self.template_name, {'form': form})

def PublicView(request,username):
    get_object_or_404(User, username=username)
    obj = Tweet.objects.filter(user=username).order_by('-date_time')
    allusers = User.objects.exclude(username = username)
    return render(request, 'TwitterApp/public_view.html', {'obj':obj, 'allusers':allusers})