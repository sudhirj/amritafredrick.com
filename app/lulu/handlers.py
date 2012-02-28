# -*- coding: utf-8 -*-
"""
    hello_world.handlers
    ~~~~~~~~~~~~~~~~~~~~

    Hello, World!: the simplest tipfy app.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin


class HomeHandler(RequestHandler, Jinja2Mixin):
    def get(self, page = None):
        if not page: page = 'home'
        if page not in ['home','about','classes','contact','blog']: self.abort(404)
        return self.render_response('%s.html' % page)
