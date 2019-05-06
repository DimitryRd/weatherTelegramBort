import pyowm

own = pyowm.OWM("84a6548ab22e73804b69892ac22d0d28", language = "ru");

place = input("Enter the city?: ")
observation = own.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print('Temperature is ' + str(temp) + " now")
print('The weather is ' + w.get_detailed_status())

if temp < 10:
    print( "Сейчас пипец как холодно!")
elif temp < 20:
    print ("Сейчас холодно одевайся потеплее")
else:
    print ("Temperature is ok - wear whatever you want!")