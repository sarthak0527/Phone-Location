import phonenumbers
import opencage

from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro= phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key ='c029e0d7695c42b8a53603bbaf67e566'
geocoder = OpenCageGeocode(key)
query = str(location)
results= geocoder.geocode(query)
print(results)
