from django.test import TestCase

# Create your tests here.
from . import models

things = models.ListThings.objects.all()
print(str(things))