import requests
from Exceptions import req_status_exception

class construct(object):
    def construct_request(self, url = 'http://localhost:5000/interview/api/v1.0/results/1'):
        r = requests.get(url)
        if r.status_code == 200:
            if r.json() is not None:
                return r.json()
            else:
                raise req_status_exception("Request did not return a JSON")
        else:
            raise req_status_exception("Requests status code not 200")
