def weather_check(temp: int) -> str:
    if temp < 0:
        return "It's freezing!"
    elif temp < 20:
        return "It's cold!"
    elif temp < 30:
        return "It's warm!"
    else:
        return "It's hot!"