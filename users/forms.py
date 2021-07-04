from django.contrib.auth.forms import UserCreationForm


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )
