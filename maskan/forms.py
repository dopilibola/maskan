from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django import forms
from .models import Profile
from .validators import validate_password_length, validate_password_not_numeric

# Ro'yxatdan o'tish formasi
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email manzilingiz'})
    )
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'})
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Familiyangiz'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Foydalanuvchi nomi maydoni sozlamalari
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Foydalanuvchi nomi'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted small">Majburiy. 150 tagacha belgi. Harflar, raqamlar va @/./+/-/_.</span>'

        # Parol maydoni (1) — validatsiya va ko‘rinish
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Parol'
        self.fields['password1'].label = ''
        self.fields['password1'].validators = [validate_password_length, validate_password_not_numeric]
        self.fields['password1'].help_text = """<ul class="form-text text-muted small">
            <li>Parolingiz boshqa shaxsiy ma'lumotlarga juda o‘xshamasligi kerak.</li>
            <li>Parol kamida 8 ta belgidan iborat bo'lishi kerak.</li>
            <li>Parol juda keng tarqalgan bo'lmasligi kerak.</li>
            <li>Parol faqat raqamlardan iborat bo'lmasligi kerak.</li>
        </ul>"""

        # Parolni tasdiqlash maydoni
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Parolni tasdiqlang'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted small">Parolni qayta kiriting.</span>'


# Parolni yangilash formasi
class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        # Yangi parol maydoni
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Yangi parol'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].validators = [validate_password_length, validate_password_not_numeric]
        self.fields['new_password1'].help_text = """<ul class="form-text text-muted small">
            <li>Parolingiz boshqa shaxsiy ma'lumotlarga juda o‘xshamasligi kerak.</li>
            <li>Parol kamida 8 ta belgidan iborat bo'lishi kerak.</li>
            <li>Parol juda keng tarqalgan bo'lmasligi kerak.</li>
            <li>Parol faqat raqamlardan iborat bo'lmasligi kerak.</li>
        </ul>"""

        # Parolni qayta kiriting maydoni
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Parolni tasdiqlang'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted small">Parolni qayta kiriting.</span>'


# Profilni tahrirlash formasi
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'job', 'image']
