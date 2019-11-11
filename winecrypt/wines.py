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

        resp.body = json.dumps(doc, ensure_ascii=False)

        resp.status = falcon.HTTP_200
