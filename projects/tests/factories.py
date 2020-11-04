from factory import Faker, Sequence, post_generation
from factory.django import DjangoModelFactory
from random import randrange
from projects.models import Project
from users.tests.factories import UserFactory


class ProjectFactory(DjangoModelFactory):
    title = Sequence(lambda n: 'Title %03d' % n)
    description = Sequence(lambda n: 'Description %03d' % n)
    start_date = Faker('past_date')
    end_date = Faker('future_date')

    class Meta:
        model = Project

    @post_generation
    def add_users(self, create, extracted, **kwargs):
        # currently, this creates new users
        # TODO: change logic to pull a random number already created users and new users
        for i in range(1, randrange(0, 10)):
            user = UserFactory()
            self.users.add(user)
