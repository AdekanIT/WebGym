from django.contrib.auth.forms import forms, UserCreationForm
from .models import Comments, Order


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


class InstructorSearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=256)


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user_comment', 'user_topic', 'user']
        widgets = {
            'user_comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here'
            }),
            'user_topic': forms.HiddenInput(),
            'user': forms.HiddenInput()}


class OrderForm(forms.ModelForm):
    phone_num = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter phone number',
    }))
    class Meta:
        model = Order
        fields = ['user_name', 'subscription', 'phone_num', 'sub_inst', 'user']
        widgets = {
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here'}),
            'sub_inst': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }