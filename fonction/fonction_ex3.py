# étudiez et executez le code suivant pour le comprendre
# modifiez ensuite la fonction imbriquée pour qu'on puisse changer la température d'une station
# et qu'un subscriber puisse définir une température à partir de laquelle il est notifié

def create_weather_station(localisation):
    observers = []
    temperature = None

    def subscribe(observer_name, seuil):
        observers.append((observer_name, seuil))

    def change_temp(new_temp):
        nonlocal temperature
        temperature = new_temp
        notify()

    def notify():
        for observer_name, seuil in observers:
            if temperature >= seuil:
                print(f"{localisation} : {observer_name} est notifié (température actuelle : {temperature}°C)")

    return subscribe, change_temp



quimper_subscribe, quimper_change_temp = create_weather_station("quimper")

quimper_subscribe("olivier", 23)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)

quimper_change_temp(24)
# aucune notification

quimper_change_temp(30)
# pierre, marie et olivier sont notifiés

quimper_change_temp(32)
# pierre, marie et olivier sont notifiés

"""
quimper_subscribe, quimper_unsubscribe, quimper_change_temp = create_weather_station("quimper")
quimper_subscribe("olivier", 30)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)
quimper_change_temp(24)
# notifications envoyées
quimper_change_temp(30)
# notifications envoyées
quimper_change_temp(32)
# notifications envoyées
"""