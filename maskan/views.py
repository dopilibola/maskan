from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, ChangePasswordForm, ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Create your views here.


def home(request):
    is_qabriston_egasi = False
    if request.user.is_authenticated:
        is_qabriston_egasi = request.user.groups.filter(name='Qabriston Egasi').exists()

    return render(request, 'home.html', {'is_qabriston_egasi': is_qabriston_egasi})





def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user) 
            messages.success(request, ('Login successful'))
            return redirect('home')
        else:
            messages.success(request, ('error try again....'))
            return redirect('login')
    else: 
        return render(request, 'login.html', {})
    




def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out succesfully')
    return redirect('home')






def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # ✅ Userni login qilish
            login(request, user)

            # ✅ Ro'yxatdan o'tgan userga avtomatik ravishda 'Foydalanuvchi' guruhini qo'shish
            group = Group.objects.get(name='Foydalanuvchi')
            user.groups.add(group)

            messages.success(request, 'User created. Please fill out your profile.')
            return redirect('edit_profile')  # ✅ Ro'yxatdan keyin profilingni to'ldirishga yo'naltiramiz
        
        else:
            messages.error(request, ('Registration failed. Please try again.'))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form })
    


# Parolni yangilash
@login_required
def update_password(request):
    current_user = request.user

    if request.method == 'POST':
        form = ChangePasswordForm(current_user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated. Please log in again.")
            return redirect('login')
        else:
            # ✅ Har bir xatoni alohida ko‘rsatamiz
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('update_password')

    form = ChangePasswordForm(current_user)
    return render(request, "update_password.html", {'form': form})


# Profilni tahrirlash
@login_required
def edit_profile(request):
    # ✅ Profil mavjud bo'lmasa avtomatik yaratiladi
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


# Profil tafsilotlari
@login_required
def profile_detail(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # ✅ Profil yo'q bo‘lsa, foydalanuvchini tahrirlash sahifasiga yo‘naltiramiz
        messages.warning(request, "Profil mavjud emas.")
        return redirect('edit_profile')

    return render(request, 'profile_detail.html', {'profile': profile})


# ✅ Ruxsat berilgan foydalanuvchilargina kirishi mumkin bo‘lgan sahifa (masalan: Qabriston egasi uchun)
@login_required
def owner_dashboard(request):
    # ✅ Faqatgina "Qabriston Egasi" guruhidagi user kirishi mumkin
    if not request.user.groups.filter(name='Qabriston Egasi').exists():
        messages.error(request, "Sizda bu sahifaga ruxsat yo'q.")
        return redirect('home')

    return render(request, 'owner_dashboard.html')  # Faqat egalar ko‘radigan HTML

