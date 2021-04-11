from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
