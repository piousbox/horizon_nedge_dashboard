
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

    def test_context_not_ok(self):
        request = HttpRequest()
        context = Context({})
        index_view = IndexView()
        response = index_view.get_data(request, context)
        print "+++ +++ 2"
        print response

        self.assertEqual('NOT OK', response['system_status'])
        
    def test_context_ok(self):
        request = HttpRequest()
        request.GET.__setitem__('NEDGE_URL', 'something-rather')
        context = Context({})
        index_view = IndexView()
        response = index_view.get_data(request, context)

        print "+++ +++ 2"
        print response['notifications']
        print "+++ +++ 2.1"
        print request

        self.assertEqual('NOT OK', response['system_status'])
        self.assertEqual('Missing parameter NEDGE_URL in settings.py. For example, NEDGE_URL="http://192.168.100.1:8080" ', 
                         response['notifications'][0]['raw_message'])
