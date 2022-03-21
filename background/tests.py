from django.test import TestCase

# Create your tests here.
import requests

res = requests.post('http://127.0.0.1:8000/background/auth/', data={'username': 3, 'passwd': 4})

print(res.text)