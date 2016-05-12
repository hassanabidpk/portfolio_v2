from django.test import TestCase
from blog.models import Post,Category
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class BlogTestCase(TestCase):
    def setUp(self):
    	# create cat
        cat1 = Category.objects.create(title="test cat",description="test")
        cat2 = Category.objects.create(title="test lion",description="test")

        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        u.is_staff = True
        u.save()

        # blog
        post1 = Post.objects.create(title="apple",content="mango",author=u)
        post1.category.add(cat1)
        post1.category.add(cat2)


    def test_post_has_field(self):
    	post1 = Post.objects.get(title="apple")
    	self.assertEqual(post1.title, "apple")
    	self.assertEqual(post1.content,"mango")

class BlogViewTests(TestCase):
    def test_blog_index_page(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'No posts added yet')
