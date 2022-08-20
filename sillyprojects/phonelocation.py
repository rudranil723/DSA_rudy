import phonelocation
from phonelocation import geocoder

phonenumber = phonelocation.parse("+8016613206")

print(geocoder.description_for_number(phonenumber, 'en'))
