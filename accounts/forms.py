from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email', 'ngaysinh', 'gioitinh', 'diachi']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match!')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserLoginFroms(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(username_iexact=username).distinct()
        if not user_qs_final.exits() and user_qs_final != 1:
            raise forms.ValidationError("Thông tin không hợp lệ, người dùng không tồn tại!")
        user_object = user_qs_final.first()
        if not user_object.check_password(password):
            raise forms.ValidationError('Không thể kết nối')
        self.cleaned_data['user_object'] = user_object
        return super(UserLoginFroms, self).clean(*args, **kwargs)

