import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = "+" + input("Enter Number Here: ")

parsed_number = phonenumbers.parse(number)

if phonenumbers.is_valid_number(parsed_number):
    geo_description = geocoder.description_for_number(parsed_number, "en")
    print(f"Geographical location: {geo_description}")
    
    time_zones = timezone.time_zones_for_number(parsed_number)
    print(f"Time zones: {', '.join(time_zones)}")
    
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print(f"Formatted number: {formatted_number}")
    
    carrier_name = carrier.name_for_number(parsed_number, "en")
    print(f"Carrier: {carrier_name}")
else:
    print("The phone number is not valid.")

