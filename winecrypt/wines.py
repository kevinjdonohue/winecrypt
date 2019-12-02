"""Wines."""

import json

import falcon


class Wines(object):
    """Wines Controller."""

    def on_get(self, req, resp):
        """GET All Wines."""
        doc = {
            "wines": [
              {
                  "name": "Kevins Fancy Red"
              },
                {
                  "name": "Kevins Fancy White"
              }
            ]

        }

        # old example used JSON -- now we're using MSGPACK instead
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

        # resp.data = msgpack.packb(doc, use_bin_type=True)
        # resp.content_type = falcon.MEDIA_MSGPACK
        # resp.status = falcon.HTTP_200
