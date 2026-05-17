from main import weather

def test_weather_check():
    w = weather()
    assert w.weather_check(-5) == "It's Freezing outside!"
    assert w.weather_check(5) == "It's Cold outside!"
    assert w.weather_check(15) == "It's Cool outside!"
    assert w.weather_check(25) == "It's Warm outside!"
    assert w.weather_check(35) == "It's Hot outside!"

def test_rain_check():
    w = weather()
    assert w.rain_check(0.8) == "It's likely to rain today. Don't forget your umbrella!"
    assert w.rain_check(0.6) == "There's a chance of rain today. You might want to carry an umbrella just in case."
    assert w.rain_check(0.4) == "It's unlikely to rain today."

# if __name__ == "__main__":
#     test_weather_check()
#     test_rain_check()
#     print("All tests passed!") 
# Uncomment this block if you want to run the tests without using pytest command line tool. 
# without these lines, you can run the tests using pytest command line tool which will automatically discover and run the test functions.