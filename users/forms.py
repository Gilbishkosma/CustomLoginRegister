from django import forms
from .models import CustomUser
from app.models import Education
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import InlineRadios,InlineCheckboxes
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Div,Field
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


Gender_choices = [('Male','Male'),('Female','Female')]

class CustomUserCreationForm(UserCreationForm):
	education = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Education.objects.all())
	email = forms.CharField(required=True)
	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username','email','sex','state','education','interest')
		widgets = {'sex':forms.RadioSelect()}
		labels = {'sex':'Gender'}

	def save(self,commit=True):
		if not commit:
			raise NotImplementedError("Can't create user and education without database save")
		user = super(CustomUserCreationForm,self).save(commit=True)
		user.education.set(self.cleaned_data['education'])
		return user

#To update userdetail
class CustomUserUpdateForm(forms.ModelForm):
	education = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Education.objects.all())


	class Meta:
		model = CustomUser
		fields = ('username','email','sex','state','education','interest')
		widgets = {'sex':forms.RadioSelect()}
		labels = {'sex':'Gender'}

	


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		 model = CustomUser
		 fields = ('username','email') #using default Meta fields


#UserCreationForm and UserChangeForm are the inbuilt classes of django default form
#We are just extending both
#UserCreationForm are used when we sign up
#UserchangeForm are used when we change something from admin site