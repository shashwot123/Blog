from django.test import TestCase
from myblog.models import Post
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PostTestCase(TestCase):

    def test_post_creation(self):
        #create user 
        user = User.objects.create_user(username="testuser")

        #create post
        post = Post.objects.create(
            title = "Test Title",
            slug = "test-title",
            content = "Random stuff for testing.",
            author = user,
        )

        self.assertEqual(post.author, user)
        self.assertEqual(post.title, "Test Title")
        self.assertIsNotNone(post.created_at)
        self.assertFalse(post.published_at)

    def test_missing_title(self):
        #create user
        user = User.objects.create_user(username="testuser")

        #create post without title
        post = Post.objects.create(
            slug = "no-title",
            content = "Where is the title?",
            author = user
        )
        #checking required field is not blank
        with self.assertRaises(ValidationError):
            post.full_clean()