import eel
from pyowm import OWM

owm = OWM('b6e342c505c7672621eba45c14ee1332')

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "В городе " + place + " сейчас " + str(temp) + " °С"

eel.init("web")
eel.start("main.html", size = (700, 700))
