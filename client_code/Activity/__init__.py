from ._anvil_designer import ActivityTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Activity(ActivityTemplate):
  def __init__(self,oxi_id=None, location_name=None, id_of_serviceprovider=None, service_type=None, oxi_username=None, oxi_book_time=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.oxi_id = oxi_id  # Store the oxi_id
    self.oxi_username = oxi_username   # Store received values
    self.location_name = location_name  # Store the location_name
    self.id_of_serviceprovider = id_of_serviceprovider
    self.service_type = service_type
    self.oxi_book_time = oxi_book_time  # Store the booking time
    # Print the values to the console
    print(f" oxi_id in Activity: {self.oxi_id}")
    print(f"Location Name in Activity: {self.location_name}")
    print(f"ID of Service Provider in Activity : {self.id_of_serviceprovider}")
    print(f"User Name in Activity: {self.oxi_username}")
    print(f"Service Type in Activity: {self.service_type}")
    print(f"Booking Time in Activity: {self.oxi_book_time}")
    # Any code you write here will run before the form opens.

    self.label_5.text = self.service_type
    self.label_9.text = self.location_name