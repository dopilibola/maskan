from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, ChangePasswordForm, ProfileForm
from .models import Profile, Product, Category, Qabristonmap
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from collections import defaultdict, OrderedDict
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.








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

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # ✅ Parolni tiklash uchun link yuborish logikasi (masalan, email orqali)
            messages.success(request, 'Parolni tiklash uchun email yuborildi.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Email not found.')
            return redirect('forgot_password')

    return render(request, 'forgot_password.html')


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








def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})



def qabristonmap_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Faqat shu productga tegishli qabrlar
    qabrlar = Qabristonmap.objects.filter(product=product).prefetch_related('images')

    # Qator bo‘yicha guruhlash
    grouped_by_row = defaultdict(list)
    for qabr in qabrlar:
        grouped_by_row[qabr.qator].append(qabr)

    # Qator va qabr_soni bo‘yicha tartiblash
    grouped_qabrlar = OrderedDict()
    for qator in sorted(grouped_by_row, key=lambda x: int(x) if str(x).isdigit() else 999):
        sorted_qabrlar = sorted(
            grouped_by_row[qator],
            key=lambda q: int(q.qabr_soni) if str(q.qabr_soni).isdigit() else 999
        )
        grouped_qabrlar[qator] = sorted_qabrlar

    return render(request, 'qabristonmap.html', {
        'product': product,
        'grouped_qabrlar': grouped_qabrlar,
    })





def category(request, foo):
    # spaces
    foo = foo.replace('-', ' ')
    #category url 
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})

    except:
        messages.success(request, ("Category dosn't exist  "))
        return redirect('home')
    

def home(request):
    products = Product.objects.all()
    searched_products = []
    searched_graves = []
    query = None
    is_qabriston_egasi = False

    if request.user.is_authenticated:
        is_qabriston_egasi = request.user.groups.filter(name='Qabriston Egasi').exists()

    if request.method == "POST":
        query = request.POST.get("searched", "").strip()
        if query:
            searched_products = Product.objects.filter(name__icontains=query)
            (
                Q(ism_familiyasi_marhum__icontains=query) |
                Q(product__name__icontains=query)
            )

    context = {
        'products': products,
        'is_qabriston_egasi': is_qabriston_egasi,
        'searched_products': searched_products,
        'searched_graves': searched_graves,
        'query': query
    }
    return render(request, 'home.html', context)


def qabristonmap_search_page(request, pk):
    # HTML sahifa ochish uchun view
    return render(request, 'search.html', {'pk': pk})

def qabristonmap_search_ajax(request, pk):
    # JSON qidiruv uchun view
    query = request.GET.get('query', '')
    results = Qabristonmap.objects.filter(
        product__id=pk
    ).filter(
    
        Q(ism_familiyasi_marhum__icontains=query) |
        Q(years__icontains=query) |
        Q(years_old__icontains=query)
    ).values('id', 'ism_familiyasi_marhum', 'years', 'qator', 'qabr_soni', 'product')
    return JsonResponse(list(results), safe=False)