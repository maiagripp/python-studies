from email.mime import base


distance = int(input("Type the distance in km "))

base_km = 0.45
if distance <= 200:
    base_km = 0.5

ticket = distance * base_km
print(f"Your ticket is ${ticket}")
