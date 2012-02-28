# -*- coding: utf-8 -*-
"""WSGI app setup."""
import os

import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))

# Add lib as primary libraries directory, with fallback to lib/dist
# and optionally to lib/dist.zip, loaded using zipimport.
sys.path[0:0] = [
    os.path.join(current_path, 'lib'),
    os.path.join(current_path, 'lib', 'dist'),
    os.path.join(current_path, 'lib', 'dist.zip'),
]

from tipfy.app import App
from config import config
from urls import rules

def enable_appstats(app):
    """Enables appstats middleware."""
    from google.appengine.ext.appstats.recording import \
        appstats_wsgi_middleware
    app.dispatch = appstats_wsgi_middleware(app.dispatch)

def enable_jinja2_debugging():
    """Enables blacklisted modules that help Jinja2 debugging."""
    if not debug:
        return
    from google.appengine.tools.dev_appserver import HardenedModulesHook
    HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']

# Is this the development server?
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

# Instantiate the application.
app = App(rules=rules, config=config, debug=debug)
enable_appstats(app)
enable_jinja2_debugging()

def main():
    app.run()

if __name__ == '__main__':
    main()
