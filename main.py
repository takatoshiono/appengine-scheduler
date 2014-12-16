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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class EvernoteHandler(webapp2.RequestHandler):
    def get(self):
        email = self.request.get('email')

        sender_email = 'takatoshi.ono@gmail.com'
        subject = '件名のテスト'
        body = '''
Body のテストです
'''

        mail.send_mail(sender_email, email, subject, body)
        self.response.write('Hello %s!' % email)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/evernote', EvernoteHandler)
], debug=True)
