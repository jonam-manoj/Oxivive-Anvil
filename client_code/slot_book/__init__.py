from ._anvil_designer import slot_bookTemplate
from anvil import *
import anvil.server
from datetime import datetime, timedelta
import random
import string
from datetime import datetime, date
# import global_vars

class slot_book(slot_bookTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.set_button_date()
        
   
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
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          button_time = datetime.strptime(button.text, "%I:%M %p").time()
          if current_time > button_time:
              button.enabled = False  
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          
          button.enabled = True 
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def button_3_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          
          button.enabled = True 
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def button_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      self.primary_color_1.visible=True
      current_time = datetime.now().time()
      times = ["09:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM", "7:00 PM"]
      for i in range(5, 11):  # Assuming you have buttons named button_5 to button_11
          button_name = f'button_{i}'
          button = getattr(self, button_name)
          # Assuming times list is predefined
          button.text = times[i - 5] if i - 5 < len(times) else "No Time"  # Display time if available, otherwise display "No Time"
          
          button.enabled = True 
      for i in range(5, 11):
            button_name = f'button_{i}'
            button = getattr(self, button_name)
            button.visible = True

    def primary_color_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      try:
            # Get the logged-in user ID from the global variable
            self.user_id = global_vars.user_id
            
            if not self.user_id:
                raise Exception("User is not logged in.")
            # Get current datetime
            current_datetime = datetime.now()

            oxi_book_date = current_datetime.strftime("%d-%m-%Y")                                                   
            oxi_book_time = current_datetime.strftime("%H:%M:%S")
            oxi_date_time = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
            oxi_servicer_id = "SP1234"
            oxi_id= self.user_id 
            oxi_book_id = 'BOOK001'
            oxi_payment_id = 'PAY001'
            
            # Insert into the database
            anvil.server.call('insert_booking_data', oxi_book_date, oxi_id, oxi_servicer_id, oxi_book_id, oxi_date_time, oxi_book_time, oxi_payment_id)
            open_form('wallet')
            print("Booking data inserted successfully.")
            
      except Exception as e:
            print(f"Error inserting booking data: {e}")
            print("Failed to insert booking data.")
      
