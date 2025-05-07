# ✨ Desafio 100 Dias de Código - Dia 7/100 💻

import pywhatkit as pwk
import time
import json

#load phone numbers from json file
with open("phone_numbers.json", "r") as file:
    phone_numbers = json.load(file)
    phone_numbers = phone_numbers["phone_numbers"]

#settings
phone_number = []
message = ""
hour = 15
minute = 30

for phone_numbers in phone_number:
    try:
        pwk.sendwhatmsg_instantly(phone_number, message, hour, minute)
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"An error occurred: {e}")
