import requests
from requests.auth import HTTPBasicAuth
import json

class ClassDeleteMethod:
    def __init__(self, route_key):
        self.ripeusername = "" #your username
        self.ripepassword = "" #your password
        self.accept = "application/json"
        self.ContentType = "application/json"
        self.route_key = route_key
        self.url = "https://rest.db.ripe.net/RIPE/route/{}.json".format(self.route_key)


    def delete_method(self):
        headers = {
            "Content-Type": self.ContentType,
            "accept": self.accept
        }

        req = requests.delete(self.url, headers=headers, auth=HTTPBasicAuth(self.ripeusername, self.ripepassword))
        # print(req.status_code)
        # print(req)
# obj_delete_method = ClassDeleteMethod("89.37.1.0/24AS50810")
# obj_delete_method.delete_method()
