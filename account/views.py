from django.shortcuts import render, redirect, get_object_or_404

# logout will simply taken in the request and the user or it will simply take in the request and simply delete the session id  which implicitly logs the user out
from django.contrib.auth import login, authenticate, logout


# # It stays above any view we want to block and basically require authentication for.
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from . forms import CustomUserCreationForm, ProfileForm

# Create your views here.
def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
#         # Restricting a logged in user from seeing the login page
        return redirect('list') # This restricts the user who is already logged in from seeing the login page by redirecting the user to the main page.
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        context = {
                'username':username,
               'password': password,
               } 
        try:
            user = User.objects.get(username=username)
            
        except:
            pass
            # messages.error(request, 'Username does not exist.')
        user = authenticate(request, username=username, password=password) # Takes in the username and password and  it will make sure that the password matches the username and it will return back either the user instance or  it will return None
        if user is not None:
            login(request, user) # This creates a session for the user in the database an it will also get that session created an add it to our cookies
#             # This login officially sets that in the browser that's how we know a user is loged-in and how the can have there permissions
            return redirect("list")# For testing
            # return redirect(request.GET['next'] if 'next' in request.GET else 'account:account') # Trying to link the login form with the query path at the url search bar of the project.By using ['next'] helps send the user back to the page being passed into the url search bar
        else:
            messages.error(request, "Username OR Password is incorrect")
    return render(request, 'account/login.html')


def logoutUser(request):
    logout(request)  # deletes the session
    messages.info(request, 'User was logged out!!')
    return redirect('account:login')



def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST': # If thee form is POST method
        form = CustomUserCreationForm(request.POST) # The form will then be passed to the backend
        # created = Profile.objects.get_or_create(user=request.user)
        if form.is_valid(): # If the form has all the qualifications on check, pass to next level or save
            user = form.save(commit=False) # SO instead of saving the form right a way, we  decided to hold the temporary instances of it.

            #NOTE: When trying to get firstName and lastname using Fullname
            # name = user.first_name.split()
            # print(name,"==========================================")
            # user.first_name = name[0]
            # user.last_name = name[1]

            user.username = user.username.lower() #Convert the unsername to lower case

            user = form.save() # Then save it.
            
            messages.success(request, 'User account was created!') # Success message
            login(request, user) # Helps create a session id for the user once every detail is valid
            return redirect('create-task')
            # return redirect('users:edit-account')
        else:
            messages.error(request, 'An error occurred during registration!') # Otherwise Error Message
            
    context = {
        'page':page,
        'form': form,
    }
    return render(request,'account/register_user.html', context)


@login_required(login_url='account:login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account edit was successful!')
            return redirect('account:account')
    context = {
        'form': form
    }
    return render(request, 'account/profile_form.html', context)


# def userProfile(request, pk):
#     profile = get_object_or_404(Profile, id=pk)

#     context = {
#         'profile': profile,
#     }
#     return render(request, 'account/user-profile.html', context)


# @login_required(login_url='account:login')
# def userAccount(request):
#     # # request.parentModelName.childModelName Gets us the logged in user if your not logged in you won't be able to access this page
#     profile = request.user.profile

#     form = ProfileForm(request.POST, request.FILES, instance=profile)
#     context = {
#         'profile': form,
#     }
#     return render(request, 'account/account.html', context)


# https://dennisivy.teachable.com/p/django-beginners-course
