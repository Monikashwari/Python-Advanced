from main import weather_check
import pytest
@pytest.mark.parametrize("temp, expected", [
    (-5, "It's freezing!"),
    (5, "It's cold!"),
    (25, "It's warm!"),
    (35, "It's hot!")
]) # This decorator allows us to run the same test function with different sets of parameters. 
# when we have to test the same function with multiple inputs and expected outputs, this is a more efficient way to write tests. 
# It reduces code duplication and makes it easier to maintain the tests. 
def test_weather_check(temp, expected):
    assert weather_check(temp) == expected
