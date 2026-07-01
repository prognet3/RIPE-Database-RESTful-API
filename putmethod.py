import requests
from requests.auth import HTTPBasicAuth
import json

class ClassPutMethod:
    def __init__(self, route, origin, mntby, source, descr, route_key):
        self.ripeusername = "" #your username
        self.ripepassword = "" #your password
        self.accept = "application/json"
        self.ContentType = "application/json"
        self.route = route
        self.origin = origin
        self.mntby = mntby
        self.source = source
        self.descr = descr
        self.route_key = route_key
        self.url = "https://rest.db.ripe.net/RIPE/route/{}.json".format(self.route_key)


    def put_method(self):
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

        req = requests.put(self.url, json=data, headers=headers, auth=HTTPBasicAuth(self.ripeusername, self.ripepassword))
        # print(req.status_code)
        # print(req)
# obj_put_method = ClassPutMethod("89.37.1.0/24", "AS50810", "MOBINNET1-MNT", "RIPE", "fortest", "89.37.1.0/24AS50810")
# obj_put_method.put_method()
