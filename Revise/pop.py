import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Revise.settings')

import django
django.setup()

from Revisionapp.models import visitors
from faker import Faker
import random

fakegen = Faker()

def popper(n):

    for a in range(n):

        fakename = fakegen.name()
        fakeemail = fakegen.email()
        fakeage = random.randint(18,80)

        t = visitors.objects.get_or_create(visitorname=fakename,visitoremail=fakeemail,visitorage=fakeage)[0]


if __name__ == '__main__':
    print('Populating')
    popper(30)
    print('Done senor')
