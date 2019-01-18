# this might be important, it explains naming conventions and how pytest finds your tests:
# https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery

import pytest

from src import controller

# simple assert test
def test_should_assert_that_true_is_true():
    assert True == True

# test with using a fixture
def test_using_a_fixture(database):
    assert database.get_clients() == ['Phil', 'Fernando', 'Yuri']

# Test with mocks

def a_simple_mock_test(mocker):
    smartphone = mocker.Mock()

    smartphone.manufacturer = 'Apple'
    smartphone.model = 'iPhone XS Max'

    assert smartphone.manufacturer == 'Apple'
    assert smartphone.model == 'iPhone XS Max'

# mocking something being imported inside another class

@pytest.yield_fixture(autouse=True)
def setup_teardown(mocker):
    # this mocks the Api being imported inside the controller module
    mocker.patch.object(controller, 'Api')

def test_should_return_mocked_result_from_api():
    controller.Api().make_an_expensive_request.return_value = 'mocked return'
    assert controller.return_some_important_information() == 'mocked return'

def test_should_assert_number_of_times_being_called():
    expected_parameter = 'philippe'
    controller.Api().a_method_that_takes_parameters.return_value = 'mocked return'

    result = controller.get_some_important_information()
    
    assert result == 'mocked return'
    controller.Api().a_method_that_takes_parameters.assert_called_with(expected_parameter)
