from main import api_call
import pytest

def test_api_call(mocker):
    # We use mocker.patch() to replace the actual requests.get function with a mock version that we can control.
    # This allows us to simulate different responses from the API without making real HTTP requests, which makes our tests faster and more reliable.
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.json.return_value = {"main":{"key": "value"}}
    result = api_call("https://api.openweathermap.org/data/2.5/weather?q=London&appid=your_api_key")
    assert result == {"Data": {"main": {"key": "value"}}}