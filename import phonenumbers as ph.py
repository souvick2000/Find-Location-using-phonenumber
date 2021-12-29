import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

phonenumber = input("Enter your phone number with country code : ")
number = phonenumbers.parse(phonenumber)

print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number,"en"))
print(geocoder.description_for_number(number,"en"))