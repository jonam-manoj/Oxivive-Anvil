from ._anvil_designer import servicers_register_add_oxiclinicTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class servicers_register_add_oxiclinic(servicers_register_add_oxiclinicTemplate):
  def __init__(self, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = user_id

    # Any code you write here will run before the form opens
  def back_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.services_register_add_service',id=self.user_id)

  def next_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    hospital_name =self.hospital_name.text
    establised_year =self.oxiclini_established_year.date
    state = self.state.text
    district =self.district.text
    pincode = self.oxiclinic_pincode.text
    address = self.oxiclinic_address.text
    capsule = self.oxiclinic_capsules.text
    fees = self.oxiclinics_fees.text
    
    if not hospital_name and not address and not capsule and not district and not establised_year and not pincode and not state or not fees :
      Notification('All fields are required.').show()
    else:
      print(self.item)
      oxiclinc_details =[hospital_name, establised_year, state, district, pincode, address, capsule, fees]
      print(oxiclinc_details)
      
      open_form('servicers_registration_form.oxiclinic_documents',oxiclinc_details=oxiclinc_details, user_id =self.user_id)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('home')
