def weather_check(temp:float) -> str:
    if temp < 0:
        return "It's Freezing outside!"
    elif temp < 10:
        return "It's Cold outside!"
    elif temp < 20:
        return "It's Cool outside!"
    elif temp < 30:
        return "It's Warm outside!"
    else:
        return "It's Hot outside!"
print(weather_check(-5))    
print(weather_check(5))