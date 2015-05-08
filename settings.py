
import logging
import os
import sys
import warnings

from django.utils.translation import ugettext_lazy as _

from openstack_dashboard import exceptions

SECRET_KEY="not empty"

HORIZON_CONFIG = {
    'dashboards': ('project', 'admin', 'settings', 'router',),
    'default_dashboard': 'project',
    'user_home': 'openstack_dashboard.views.get_user_home',
    'ajax_queue_limit': 10,
    'auto_fade_alerts': {
        'delay': 3000,
        'fade_duration': 1500,
        'types': ['alert-success', 'alert-info']
    },
    'help_url': "http://docs.openstack.org",
    'exceptions': {'recoverable': exceptions.RECOVERABLE,
                   'not_found': exceptions.NOT_FOUND,
                   'unauthorized': exceptions.UNAUTHORIZED},
}

TEST_RUNNER = "openstack_dashboard.dashboards.horizon_nedge_dashboard.tests.NoDbTestRunner"
