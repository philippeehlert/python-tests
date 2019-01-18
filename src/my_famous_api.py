import time

class Api:

    def make_an_expensive_request(self):
        time.sleep(5)
        return 'actual return from real api'

    def a_method_that_takes_parameters(self, a_parameter):
        return a_parameter
        