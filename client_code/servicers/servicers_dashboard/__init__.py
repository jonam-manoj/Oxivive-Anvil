from ._anvil_designer import servicers_dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import user_id
from datetime import datetime, timedelta


class servicers_dashboard(servicers_dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.id = user_id.user_id 
    print("sd user id",self.id,user_id.user_id)
    now =datetime.now()
    date = now.date() 
    self.date_picker_1.date=date
    self.customers(date)
    
 
    # Any code you write here will run before the form opens.
  def customers (self,date):
    # self.date_picker_1.pick_time = True
    data = app_tables.oxi_book_slot.search(book_date=date,serviceProvider_id =self.id)
    if not data:
        alert("No bookings yet on this date")

    customers_list =[]
    for row in data:
      customer_details =app_tables.users.get(id=row['user_id'])
      customer = {}
      customer["name"]=customer_details['username']
      customer["email"]=customer_details['email']
      customer["phone"]=customer_details['phone']
      customer["slot_time"]=row['book_time']
      customer["service"]=row['service_type']
      customer["image"] = customer_details['profile']
      customer["date"] = row['book_date']
      customers_list.append(customer)
    self.repeating_panel_1.items=customers_list

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    date = self.date_picker_1.date
    self.customers(date)
