import falcon
import os
import json


class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = '{"hello":"world"}'

class TestStuff(object):
    def on_get(self, req, resp):
        get_os_value = json.dumps(str(os.environ))
        resp.body = get_os_value


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/' URL path
app.add_route('/', things)
app.add_route('/test_stuff', TestStuff())