from django.test import TestCase
from resume.models import Skill,Project
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class ResumeTestCase(TestCase):
    def setUp(self):
        # project and skills
        skill1 = Skill.objects.create(title="android",term="2 years")
        skill2 = Skill.objects.create(title="ios",term="1 years")
        u = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        u.is_staff = True
        u.save()
        project1 = Project.objects.create(title="title lion", description="roar",github_link="http://github.com", \
        android="http://google.com", ios="google.com", web="apple.com",author=u)
        project1.skills.add(skill1)
        project1.skills.add(skill2)
        project2 = Project.objects.create(title="tiger", description="roar",author=u)
        project2.skills.add(skill2)


    def test_project_has_title(self):
        p1 = Project.objects.get(title="title lion")
        p2 = Project.objects.get(title="tiger")
        s1 = p1.skills.all()[0]
        s2 = p1.skills.all()[1]
        self.assertEqual(p1.title, 'title lion')
        self.assertEqual(s1.title, "android")
        self.assertEqual(s2.title, "ios")
        self.assertEqual(p2.title, "tiger")
        self.assertEqual(p2.author.username,"john")

class ResumeViewTests(TestCase):
    def test_resume_index_page(self):
        response = self.client.get(reverse('resume:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'No projects added yet')
