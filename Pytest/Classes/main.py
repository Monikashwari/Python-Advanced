class weather:
    def weather_check(self,temp:float) -> str:
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
    def rain_check(self,rain_chance:float) -> str:
        if rain_chance > 0.7:
            return "It's likely to rain today. Don't forget your umbrella!"
        elif rain_chance > 0.5:
            return "There's a chance of rain today. You might want to carry an umbrella just in case."
        else:
            return "It's unlikely to rain today."