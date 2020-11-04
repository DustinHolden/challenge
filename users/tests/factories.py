from factory import Faker
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    email = Faker('email')
    name = Faker('name')
    password = Faker('password', length=18, special_chars=True, digits=True, upper_case=True, lower_case=True)

    class Meta:
        model = get_user_model()
