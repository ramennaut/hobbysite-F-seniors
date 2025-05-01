from django.test import TestCase
from .models import Thread, ThreadCategory, Comment
from django.contrib.auth.models import User

class ForumTests(TestCase):
    def test_create_thread(self):
        category = ThreadCategory.objects.create(name="Test Category", description="A test category.")
        thread = Thread.objects.create(title="Test Thread", category=category, entry="This is a test thread.")
        self.assertEqual(thread.title, "Test Thread")
        self.assertEqual(thread.entry, "This is a test thread.")

    def test_create_comment(self):
        user = User.objects.create_user(username='testuser', password='password')
        category = ThreadCategory.objects.create(name="Test Category", description="A test category.")
        thread = Thread.objects.create(title="Test Thread", category=category, entry="This is a test thread.")
        comment = Comment.objects.create(entry="This is a test comment.", thread=thread, author=user)
        self.assertEqual(comment.entry, "This is a test comment.")
        self.assertEqual(comment.author.username, "testuser")
