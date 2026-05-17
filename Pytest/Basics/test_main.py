from main import weather_check

def test_weather_check():
    assert weather_check(-5) == "It's Freezing outside!"
    assert weather_check(5) == "It's Cold outside!"
    assert weather_check(15) == "It's Cool outside!"
    assert weather_check(25) == "It's Warm outside!"
    assert weather_check(35) == "It's Hot outside!"

if __name__ == "__main__":
    test_weather_check()
    print("All tests passed!")