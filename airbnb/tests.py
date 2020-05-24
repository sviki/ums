from django.test import TestCase

from airbnb.models import PageContent

class PageContentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        PageContent.objects.create(title='Big')

    def test_title_label(self):
        author = PageContent.objects.get(id=1)
        field_label = author._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_image_label(self):
        author=PageContent.objects.get(id=1)
        field_label = author._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')