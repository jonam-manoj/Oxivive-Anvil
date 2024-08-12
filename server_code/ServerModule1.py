import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.media
import base64
import requests
import random
import string

import hashlib
import anvil.secrets
import hmac

@anvil.server.callable
def user(oxi_id,oxusername,email,password,phone,pincode,wallet_balance):
  app_tables.users.add_row(id=id, username=username, email=email, password=password,phone=phone,pincode=pincode,wallet_balance=wallet_balance)
  
@anvil.server.callable
def BookSlot(slot_id, user_id, username,book_date,book_time):
  app_tables.bookslot.add_row(slot_id=slot_id, user_id=user_id, username=username, book_date=book_date, book_time=book_time)

@anvil.server.callable
def Oxiclinics(id, name, email, password, phone, address, Oxiclinics_Name, established_year, District, State, pincode, address_2, capsules, medical_licence, building_licence):
  app_tables.oxiclinics.add_row(id=id, name=name, email=email, password=password, phone=phone, address=address, Oxiclinics_Name=Oxiclinics_Name, established_year=established_year, District=District, State=State, pincode=pincode, address_2=address_2, capsules=capsules, medical_licence=medical_licence, building_licence=building_licence)

@anvil.server.callable
def Oxiwheels(id, name, email, password, phone, address, Oxiwheels_Name, model_year, District, State, pincode, address_2, capsules, vehicle_rc, driving_licence):
  app_tables.oxiwheels.add_row(id=id, name=name, email=email, password=password, phone=phone, address=address, Oxiwheels_Name=Oxiwheels_Name, model_year=model_year, District=District, State=State, pincode=pincode, address_2=address_2, capsules=capsules, vehicle_rc=vehicle_rc, driving_licence=driving_licence)

@anvil.server.callable
def Oxigyms(id, name, email, password, phone, address, Oxigyms_Name, established_year, District, State, pincode, address_2, capsules, gym_licence, building_licence):
  app_tables.oxigyms.add_row(id=id, name=name, email=email, password=password, phone=phone, address=address, Oxigyms_Name=Oxigyms_Name, established_year=established_year, District=District, State=State, pincode=pincode, address_2=address_2, capsules=capsules, gym_licence=gym_licence, building_licence=building_licence)

@anvil.server.callable
def create_media_object(content_type, file_data_base64, file_name):
    # Decode the base64 string to get the bytes data
    file_data = base64.b64decode(file_data_base64)
    media_object = anvil.media.BlobMedia(content_type, file_data, file_name)
    return media_object

@anvil.server.callable
def check_internet_status():
    # Perform a simple server call to check connectivity
    return True
# @anvil.server.callable
# def add_info(email, username, password, phone,pincode):
#     user_row = app_tables.users.add_row(
#         email=email,
#         username=username,
#         password=password,
 
#         phone=phone,
#         pincode=pincode
#     )
#     return user_row
@anvil.server.callable
def check_login_credentials(email, password):
    # Retrieve the user record based on the provided email address
    user = app_tables.users.get(email=email)
    
    # Check if a user exists with the provided email address and password matches
    if user and user['password'] == password:
        return True
    else:
        return False



@anvil.server.callable
def get_location(query):
    api_key = "AIzaSyA8GzhJLPK0Hfryi5zHbg3RMDSMCukmQCw"  # Replace with your Google Maps API key
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={query}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'results' in data:
            # Extract only the relevant information
            formatted_results = [{'formatted': result['formatted_address']} for result in data['results']]
            return {'results': formatted_results}
        else:
            return {"error": "No results found"}
    else:
        return {"error": "Unable to fetch data"}


# Predefined nearby pin codes for locations
nearby_pincodes_map = {
    "Hebbal": [560024, 560032, 560094, 560080],    # Example pin codes for Hebbal
    "Yelahanka": [560064, 560063, 560057, 560092], # Example pin codes for Yelahanka
    "Marathahalli": [560037, 560066, 560103, 560048] # Example pin codes for Marathahalli
}


@anvil.server.callable
def check_pincode_in_tables(location_name):
    nearby_pincodes = nearby_pincodes_map.get(location_name, [])

    results = {
        'oxiclinics_exists': False,
        'oxigyms_exists': False,
        'oxiwheels_exists': False,
        'id_of_serviceprovider_clinic': None,        
        'id_of_serviceprovider_wheel': None,
        'id_of_serviceprovider_gym': None
    }
    
    if nearby_pincodes:
        # Check oxiclinics
        for record in app_tables.oxiclinics.search():
            if record['oxiclinics_pincode'] in nearby_pincodes:
                results['oxiclinics_exists'] = True
                results['id_of_serviceprovider_clinic'] = record['oxi_id']
                break

        # Check oxiwheels
        for record in app_tables.oxiwheels.search():
            if record['oxiwheels_pincode'] in nearby_pincodes:
                results['oxiwheels_exists'] = True
                results['id_of_serviceprovider_wheel'] = record['oxi_id']
                break
              
        # Check oxigyms
        for record in app_tables.oxigyms.search():
            if record['oxigyms_pincode'] in nearby_pincodes:
                results['oxigyms_exists'] = True
                results['id_of_serviceprovider_gym'] = record['oxi_id']
                break

        
    
    return results



# def custom_hash_function(password, salt):
#     password_bytes = bytearray(password.encode('utf-8'))
#     salt_bytes = bytearray(salt)
#     mixed_bytes = bytearray(len(password_bytes) + len(salt_bytes))
    
#     for i in range(len(password_bytes)):
#         mixed_bytes[i] = password_bytes[i] ^ salt_bytes[i % len(salt_bytes)]
    
#     for _ in range(100000):
#         for i in range(len(mixed_bytes)):
#             mixed_bytes[i] = (mixed_bytes[i] + i + mixed_bytes[i-1]) % 256
    
#     hashed_password = mixed_bytes.hex()
#     return hashed_password

@anvil.server.callable
def insert_booking_data(oxi_id, oxi_book_date, oxi_servicer_id, oxi_book_id, oxi_date_time, oxi_book_time, oxi_payment_id, oxi_service_type, oxi_username):
    try:
        # Insert data into 'oxi_book_slot' table
        app_tables.oxi_book_slot.add_row(
            oxi_book_date=oxi_book_date,
            oxi_servicer_id=oxi_servicer_id,
            oxi_book_id=oxi_book_id,
            oxi_id=oxi_id,  # Store oxi_id in the table
            oxi_book_time=oxi_book_time,
            oxi_date_time=oxi_date_time,
            oxi_payment_id=oxi_payment_id,
            oxi_service_type=oxi_service_type,
            oxi_username=oxi_username
        )
        return True  # Indicate success if needed
    except Exception as e:
        print(f"Error inserting booking data: {e}")
        return False  # Return False or handle error as per your application logic

@anvil.server.callable
def get_fee_amount(id_of_serviceprovider):
    # Check in oxiclinics table
    clinic = app_tables.oxiclinics.get(oxi_id=id_of_serviceprovider)
    if clinic:
        return clinic['oxiclinics_fees']
    
    # Check in oxigyms table
    gym = app_tables.oxigyms.get(oxi_id=id_of_serviceprovider)
    if gym:
        return gym['oxiclinics_fees']
    
    # Check in oxiwheels table
    wheel = app_tables.oxiwheels.get(oxi_id=id_of_serviceprovider)
    if wheel:
        return wheel['oxiclinics_fees']
    
    return None


@anvil.server.callable
def get_user_details_by_id(oxi_id):
    # Query the oxi_users table to get user details
    user_row = app_tables.oxi_users.get(oxi_id=oxi_id)
    
    if user_row:
        return {
            'oxi_username': user_row['oxi_username'],
            'oxi_email': user_row['oxi_email'],
            'oxi_phone': user_row['oxi_phone'],
            'oxi_address': user_row['oxi_address'],
            'oxi_city': user_row['oxi_city'],
            'oxi_state': user_row['oxi_state'],
            'oxi_country': user_row['oxi_country'],
            'oxi_dob': user_row['oxi_dob'],
            'oxi_profile': user_row['oxi_profile']
        }
    else:
        return {'error': 'User not found'}

@anvil.server.callable
def update_user_details_by_id(oxi_id, oxi_username, oxi_email, oxi_phone, oxi_address, oxi_city, oxi_state, oxi_country, oxi_dob, oxi_profile):
    user_row = app_tables.oxi_users.get(oxi_id=oxi_id)
    
    if user_row:
        user_row['oxi_username'] = oxi_username
        user_row['oxi_email'] = oxi_email
        user_row['oxi_phone'] = oxi_phone
        user_row['oxi_address'] = oxi_address
        user_row['oxi_city'] = oxi_city
        user_row['oxi_state'] = oxi_state
        user_row['oxi_country'] = oxi_country
        user_row['oxi_dob'] = oxi_dob
        if oxi_profile:
            user_row['oxi_profile'] = oxi_profile
        
        return "User details updated successfully"
        
    else:
        return "User not found"

@anvil.server.callable
def update_user_profile_image(oxi_id, file):
    user_row = app_tables.oxi_users.get(oxi_id=oxi_id)
    
    if user_row:
        user_row['oxi_profile'] = file  # Save the uploaded file to the 'oxi_profile' column
        return "Profile image updated successfully"
    else:
        return "User not found"

