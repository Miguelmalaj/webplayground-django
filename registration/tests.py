from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test11', 'test11@test.com', 'test118383')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test11').exists()
        self.assertEqual(exists, True)
