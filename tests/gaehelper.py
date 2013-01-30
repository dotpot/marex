#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.appengine.ext import testbed

class gaetestbed(object):
    def activate(self, *services):
        self.testbed = testbed.Testbed()
        self.testbed.activate()

        if 'app_identity' in services:
            self.testbed.init_app_identity_stub()
        if 'blobstore' in services:
            self.testbed.init_blobstore_stub()
        if 'capability' in services:
            self.testbed.init_capability_stub()
        if 'channel' in services:
            self.testbed.init_channel_stub()
        if 'datastore' in services:
            self.testbed.init_datastore_v3_stub()
        if 'files' in services:
            self.testbed.init_files_stub()
        if 'images' in services:
            self.testbed.init_images_stub()
        if 'logservice' in services:
            self.testbed.init_logservice_stub()
        if 'mail' in services:
            self.testbed.init_mail_stub()
        if 'memcache' in services:
            self.testbed.init_memcache_stub()
        if 'taskqueue' in services:
            self.testbed.init_taskqueue_stub()
        if 'urlfetch' in services:
            self.testbed.init_urlfetch_stub()
        if 'user' in services:
            self.testbed.init_user_stub()
        if 'xmpp' in services:
            self.testbed.init_xmpp_stub()

    def deactivate(self):
        self.testbed.deactivate()
