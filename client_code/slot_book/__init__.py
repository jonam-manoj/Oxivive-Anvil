from ._anvil_designer import slot_bookTemplate
from anvil import *
import anvil.server
from datetime import datetime, timedelta
import random
import string
from datetime import date
# import global_vars

class slot_book(slot_bookTemplate):
    def __init__(self, oxi_id=None, location_name=None, id_of_serviceprovider=None, service_type=None, oxi_username=None, image_source=None, label_text=None, address=None, **properties):
        self.init_components(**properties)
        self.set_button_date()
        self.oxi_id = oxi_id  # Store the oxi_id
        self.oxi_username = oxi_username   # Store received values
        self.location_name = location_name  # Store the location_name
        self.id_of_serviceprovider = id_of_serviceprovider
        self.service_type = service_type
        self.selected_time = None  # Add instance variable to store selected time
        self.selected_date = None
        self.oxi_book_time = None
      # Print the values to the console
        print(f" oxi_id in Slot Book: {self.oxi_id}")
        print(f"Location Name in Slot Book: {self.location_name}")
        print(f"ID of Service Provider in Slot Book : {self.id_of_serviceprovider}")
        print(f"User Name in Slot Book: {self.oxi_username}")
        print(f"Service Type in slot book: {self.service_type}")

        print("data from repeting panal")
        print(f"Service Provider ID: {id_of_serviceprovider}")
        print(f"Image Source: {image_source}")
        print(f"Label Text: {label_text}")
        print(f"Address: {address}")

        self.oxi_image.source = image_source
        self.oxi_type.text = label_text
        self.label_2.text = address
   
    def set_button_date(self):
        current_date = datetime.now()
        for i in range(1, 5):  # Assuming you have 4 buttons named button_1, button_2, ..., button_4
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            date_for_button = current_date + timedelta(days=i-1)
            # Format the date as "Day" (e.g., "Tue") and day number (e.g., "17")
            formatted_date = date_for_button.strftime("%a %d")
            button.text = formatted_date
  
         
    def button_1_click(self, **event_args):
        self.primary_color_1.visible = True
        current_time = datetime.now().time()
        times = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
        for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.text = times[i - 5] if i - 5 < len(times) else "No Time"
            button_time = datetime.strptime(button.text, "%I:%M %p").time()
            button.enabled = not (current_time > button_time)  # Disable past times
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True
            button.set_event_handler('click', self.time_button_click)


    def button_2_click(self, **event_args):
        self.primary_color_1.visible = True
        times = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
        for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            # Display all times without checking current time
            button.text = times[i - 5] if i - 5 < len(times) else "No Time"
            button.enabled = True  # Enable all buttons
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True
            button.set_event_handler('click', self.time_button_click)
        # Set selected_date to the date for button_2 (tomorrow)
        current_date = datetime.now() + timedelta(days=1)
        self.selected_date = current_date.strftime("%a %d")
        print(f"Selected date updated: {self.selected_date}")


    def button_3_click(self, **event_args):
        self.primary_color_1.visible = True
        times = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
        for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            # Display all times without checking current time
            button.text = times[i - 5] if i - 5 < len(times) else "No Time"
            button.enabled = True  # Enable all buttons
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True
            button.set_event_handler('click', self.time_button_click)
        # Set selected_date to the date for button_3 (day after tomorrow)
        current_date = datetime.now() + timedelta(days=2)
        self.selected_date = current_date.strftime("%a %d")
        print(f"Selected date updated: {self.selected_date}")

    def button_4_click(self, **event_args):
        self.primary_color_1.visible = True
        times = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
        for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            # Display all times without checking current time
            button.text = times[i - 5] if i - 5 < len(times) else "No Time"
            button.enabled = True  # Enable all buttons
        for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True
            button.set_event_handler('click', self.time_button_click)
        # Set selected_date to the date for button_4 (2 days after tomorrow)
        current_date = datetime.now() + timedelta(days=3)
        self.selected_date = current_date.strftime("%a %d")
        print(f"Selected date updated: {self.selected_date}")

    
    def time_button_click(self, **event_args):
        clicked_button = event_args['sender']
        self.selected_time = clicked_button.text.strip()   # Store the selected time in the instance variable
        print(f"Selected time: {self.selected_time}")
      
        if self.selected_time == "09:00 AM":
            self.oxi_book_time = "09:00 AM - 11:00 AM"
        elif self.selected_time == "11:00 AM":
            self.oxi_book_time = "11:00 AM - 01:00 PM"
        elif self.selected_time == "1:00 PM":
            self.oxi_book_time = "01:00 PM - 03:00 PM"
        elif self.selected_time == "3:00 PM":
            self.oxi_book_time = "03:00 PM - 05:00 PM"
        elif self.selected_time == "5:00 PM":
            self.oxi_book_time = "05:00 PM - 07:00 PM"
        elif self.selected_time == "7:00 PM":
            self.oxi_book_time = "07:00 PM - 09:00 PM"
        else:
            print(f"Invalid time selected: '{self.selected_time}'")
            raise ValueError("Invalid time selected")

        print(f"Selected date: {self.selected_date}")
        
        print(f"Booking time range: {self.oxi_book_time}")
  
    def primary_color_1_click(self, **event_args):
        try:
            # Generate random booking ID
            oxi_book_id = f"BI{random.randint(10000, 99999)}"  # Example: BI70000

            # Get the current date
            current_date = datetime.now()
            oxi_book_date_db = current_date.date()  # Store as date type for the database

            # Get current datetime and format oxi_date_time
            oxi_date_time = f"{self.selected_date} {self.selected_time}"

            # Prepare variables
            oxi_id = self.oxi_id  # From new_dashboard form
            oxi_servicer_id = self.id_of_serviceprovider  # The ID of the selected service provider
            oxi_service_type = self.service_type  # The type of service selected (OxiGym, OxiWheel, OxiClinic)
            oxi_username = self.oxi_username  # Username from the login form
            oxi_payment_id = "0000"

            # Call the server function to insert booking data
            anvil.server.call('insert_booking_data', oxi_id, oxi_book_date_db, oxi_servicer_id, oxi_book_id, oxi_date_time, self.oxi_book_time, oxi_payment_id, oxi_service_type, oxi_username)

            print("Booking data inserted successfully.")
            # Pass the booking details to the Activity form
            open_form('Activity', oxi_id=oxi_id, location_name=self.location_name, id_of_serviceprovider=oxi_servicer_id, service_type=oxi_service_type, oxi_username=oxi_username, oxi_book_time=self.oxi_book_time, oxi_book_date=oxi_book_date_db, oxi_book_id=oxi_book_id)
        except Exception as e:
            print(f"Error: {e}")

    def button_11_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('new_dashboard')

    def button_12_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('new_dashboard')
      
