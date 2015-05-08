
from django.test import TestCase
from django.test import Client

from django.http import HttpRequest, HttpResponse

from django.template import Context, Template

from views import IndexView

class MypanelTests(TestCase):

    def setUp(self):
        # c = Client()
        # response = c.get('/nedge_dashboard')
        # print "+++ +++"
        # print response

        pass

    def test_sanity(self):
        self.assertTrue(1 + 1 == 2)

    def test_not_ok(self):
        request = HttpRequest()
        context = Context({})
        index_view = IndexView()
        response = index_view.get_data(request, context)

        self.assertEqual('NOT OK', response['system_status'])
        self.assertEqual('Missing parameter NEDGE_URL in settings.py. For example, NEDGE_URL="http://192.168.100.1:8080"',
                         response['notifications'][0]['raw_message'])

    def test_url_with_and_without_slash(self):
        request = HttpRequest()
        request.GET.__setitem__('NEDGE_URL', 'http://10.3.30.116:8080/') # with
        context = Context({})
        index_view = IndexView()
        response = index_view.get_data(request, context)
        self.assertEqual(response['nedge_url'], 'http://10.3.30.116:8080')

        request.GET.__setitem__('NEDGE_URL', 'http://10.3.30.116:8080') # without
        response = index_view.get_data(request, context)
        self.assertEqual(response['nedge_url'], 'http://10.3.30.116:8080')

a = """
    def test_url_with_slash(self):
        request = HttpRequest()
        request.GET.__setitem__('NEDGE_URL', 'something-rather')
        context = Context({})
        index_view = IndexView()
        response = index_view.get_data(request, context)

        self.assertEqual('NOT OK', response['system_status'])
        self.assertEqual('System is down!', response['notifications'][0]['raw_message'])
"""

