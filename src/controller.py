from src.my_famous_api import Api

def return_some_important_information():
    api = Api()
    return api.make_an_expensive_request()

def get_some_important_information():
    api = Api()
    return api.a_method_that_takes_parameters('philippe')
