import json
import io
import sys

from django.core.management import call_command
from django.test import TestCase


class TestDjangoMigrationsIgnoreAttrs(TestCase):
    databases = {'default', 'django'}

    @staticmethod
    def setUp():
        call_command('loaddata', 'category', database='default', verbosity=0)
        call_command('loaddata', 'note', database='default', verbosity=0)

    def test_database_default(self):
        out = io.StringIO() if sys.version_info >= (3, 0) else io.BytesIO()
        call_command('dumpdata', 'test_project.category', database='default', verbosity=2, format='json', stdout=out)
        data = json.loads(out.getvalue())
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['model'], 'test_project.category')

    def test_database_django(self):
        out = io.StringIO() if sys.version_info >= (3, 0) else io.BytesIO()
        call_command('dumpdata', 'test_project.category', database='django', verbosity=2, format='json', stdout=out)
        data = json.loads(out.getvalue())
        self.assertEqual(len(data), 0)
