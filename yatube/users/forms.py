from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Никнейм для сайта',
            'email': 'email адрес',
        }
        help_texts = {
            'first_name': ('Имя и фамилия, которые будут видны вашим'
                           ' читателем на сайте'),
            'last_name': 'Ваша фамилия',
            'username': ('После регистрации будет использоваться для входа'
                         ' на сайт'),
            'email': ('Необходим на все случаи жизни'),
        }
