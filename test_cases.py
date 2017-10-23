from test_framework import construct
import re

class Utils(object):
    def set_url(self,url):
        self.url = url

    def req_exec(self):
        req_handler = construct()
        res = req_handler.construct_request(self.url)
        return res

    def is_num(self,n):
        try:
            int(n)
            return True
        except ValueError:
            pass
        return False

    def is_Phone(self,number):
        pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
        return pattern.match(number) is not None

class Test_API(Utils):
    def test_all_records(self):
        url = 'http://localhost:5000/interview/api/v1.0/results'
        self.set_url(url)
        res = self.req_exec()
        assert res is not None

    def test_limit_1(self):
        limit = 1
        url = 'http://localhost:5000/interview/api/v1.0/results/'+str(limit)
        self.set_url(url)
        res = self.req_exec()
        assert res is not None

    def test_area_code(self):
        area_code = 844
        url = 'http://localhost:5000/interview/api/v1.0/resultsForArea/'+str(area_code)
        self.set_url(url)
        res = self.req_exec()
        assert res is not None

    def test_area_limit(self):
        area_code = 844
        limit = 1
        url = 'http://localhost:5000/interview/api/v1.0/resultsForArea/'+str(area_code)+'/'+str(limit)
        self.set_url(url)
        res = self.req_exec()
        assert res is not None

class Test_Json(Utils):
    def test_area_code(self):
        limit = 1
        url = 'http://localhost:5000/interview/api/v1.0/results/'+str(limit)
        self.set_url(url)
        res = self.req_exec()
        assert res is not None
        area_code = res[0]['area_code']
        assert self.is_num(area_code) == True

    def test_area_code(self):
        limit = 1
        url = 'http://localhost:5000/interview/api/v1.0/results/'+str(limit)
        self.set_url(url)
        res = self.req_exec()
        assert res is not None
        phone_num = res[0]['phone_number']
        assert self.is_Phone(phone_num) == True

    def test_report_count(self):
        limit = 1
        url = 'http://localhost:5000/interview/api/v1.0/results/'+str(limit)
        self.set_url(url)
        res = self.req_exec()
        assert res is not None
        report_count = res[0]['report_count']
        assert self.is_num(report_count) == True

    def test_commment(self):
        #Comments may or may not be present. No validation required
        pass
