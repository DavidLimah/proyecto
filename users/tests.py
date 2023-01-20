from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='davidlima',
            email='davidlima@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'davidlima')
        self.assertEqual(user.email, 'davidlima@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='jorgelopez',
            email='jorgelopez@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'jorgelopez')
        self.assertEqual(admin_user.email, 'jorgelopez@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)