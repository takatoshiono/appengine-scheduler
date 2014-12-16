#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import mail

import base64
from datetime import date

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class EvernoteHandler(webapp2.RequestHandler):

    def get(self):
        sender_email = 'takatoshi.ono@gmail.com'
        subject = '%s @日記' % (date.today().strftime('%Y年%m月%d日'))
        body = ''

        mail.send_mail(sender_email, self.evernote_email(), subject, body)
        self.response.write('To: %s, Subject: %s' % (self.evernote_email(), subject))

    def evernote_email(self):
        return base64.b64decode('dGtfb25vLjgzZjY4QG0uZXZlcm5vdGUuY29t')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/evernote', EvernoteHandler)
], debug=True)
