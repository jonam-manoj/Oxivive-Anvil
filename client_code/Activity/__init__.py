from ._anvil_designer import ActivityTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Activity(ActivityTemplate):
  def __init__(self, oxi_id=None, location_name=None, id_of_serviceprovider=None, service_type=None, oxi_username=None, oxi_book_time=None, oxi_book_date=None, oxi_book_id=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Store received values in instance variables
        self.oxi_id = oxi_id
        self.oxi_username = oxi_username
        self.location_name = location_name
        self.id_of_serviceprovider = id_of_serviceprovider
        self.service_type = service_type
        self.oxi_book_time = oxi_book_time
        self.oxi_book_date = oxi_book_date
        self.oxi_book_id = oxi_book_id

        # Print the values to the console
        print(f"oxi_id in Activity: {self.oxi_id}")
        print(f"Location Name in Activity: {self.location_name}")
        print(f"ID of Service Provider in Activity: {self.id_of_serviceprovider}")
        print(f"User Name in Activity: {self.oxi_username}")
        print(f"Service Type in Activity: {self.service_type}")
        print(f"Booking Time in Activity: {self.oxi_book_time}")
        print(f"Booking Date in Activity: {self.oxi_book_date}")
        print(f"Booking ID in Activity: {self.oxi_book_id}")

        self.label_5.text = self.oxi_book_date
        self.label_9.text = self.location_name
        self.label_16.text = self.oxi_book_time 
        self.label_6.text = self.oxi_book_time
        self.label_14.text = self.oxi_book_id
        self.label_15.text = self.oxi_book_date

      # Get and display the fee amount
        self.get_and_display_fee_amount()   
    
  def get_and_display_fee_amount(self):
        fee_amount = anvil.server.call('get_fee_amount', self.id_of_serviceprovider)
        if fee_amount is not None:
            self.label_24.text = f"Fees: {fee_amount}"
        else:
            self.label_24.text = "Fees: Not available"