import requests
from requests.auth import HTTPBasicAuth
import json

class ClassPostMethod:
    def __init__(self, route, origin, mntby, source, descr):
        self.ripeusername = "" #your username
        self.ripepassword = "" #your password
        self.url = "https://rest.db.ripe.net/RIPE/route"
        self.accept = "application/json"
        self.ContentType = "application/json"
        self.route = route
        self.origin = origin
        self.mntby = mntby
        self.source = source
        self.descr = descr

    def post_method(self):
        data = {
            "objects": {
                "object": [
                    {
                        "type": "route",
                        "attributes": {
                            "attribute": [
                                {
                                    "name": "route",
                                    "value": self.route
                                },
                                {
                                    "name": "origin",
                                    "value": self.origin
                                },
                                {
                                    "name": "mnt-by",
                                    "value": self.mntby
                                },
                                {
                                    "name": "source",
                                    "value": self.source
                                },
                                {
                                    "name": "descr",
                                    "value": self.descr
                                }
                            ]
                        }
                    }
                ]
            }
        }
        headers = {
            "Content-Type": self.ContentType,
            "accept": self.accept
        }

        req = requests.post(self.url, json=data, headers=headers, auth=HTTPBasicAuth(self.ripeusername, self.ripepassword))
        print(req.status_code)
        print(req)
# obj_post_method = ClassPostMethod("89.37.1.0/24", "AS50810", "MOBINNET1-MNT", "RIPE", "ripeautomationtools")
# obj_post_method.post_method()
