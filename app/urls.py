# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule
from lulu import handlers

rules = [
    Rule('/', name='home', handler = handlers.HomeHandler),
    Rule('/<page>/', name='page', handler = handlers.HomeHandler),
]
