"""API."""
import falcon

from .wines import Wines

api = application = falcon.API()

wines = Wines()

api.add_route("/wines", wines)
