from django.test import TestCase

from .models import ModelA


class TestMain(TestCase):
    fixtures = ['basic']

    def test_index_selection(self):
        self.assertEqual(ModelA.index_selection.random(5).count(), 5)
        self.assertEqual(ModelA.index_selection.random(25).count(), 20)

    def test_index_exclusion(self):
        self.assertEqual(ModelA.index_exclusion.random(5).count(), 5)
        self.assertEqual(ModelA.index_exclusion.random(25).count(), 20)

    def test_index_combo(self):
        self.assertEqual(ModelA.index_combo.random(5).count(), 5)
        self.assertEqual(ModelA.index_combo.random(25).count(), 20)

    def test_empty_queryset(self):
        ModelA.objects.all().delete()
        ModelA.objects.random(1)

