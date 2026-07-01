import requests
from requests.auth import HTTPBasicAuth
import json

class ClassGetMethod:
    def __init__(self, route_key):
        self.ripeusername = ""  #your username
        self.ripepassword = ""  #your username
        self.route_key = route_key


    def get_method(self):
        url = "https://rest.db.ripe.net/RIPE/route/{}.json".format(self.route_key)
        req = requests.get(url, auth=HTTPBasicAuth(self.ripeusername, self.ripepassword)).json()
        print(req)
        print(req['objects']['object'][0]['attributes']['attribute'][3]['name'])
        print(req['objects']['object'][0]['attributes']['attribute'][3]['value'])
        print(json.dumps(req, indent=4))
# obj_get_method = ClassGetMethod("89.37.1.0/24AS50810")
# obj_get_method.get_method()
