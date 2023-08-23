from home.models import User
from django.contrib.auth.forms import UserCreationForm

# Write your forms here
class homeUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_dealer', 'is_client']