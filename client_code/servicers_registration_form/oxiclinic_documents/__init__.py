from ._anvil_designer import oxiclinic_documentsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string

class oxiclinic_documents(oxiclinic_documentsTemplate):
  def __init__(self, oxiclinc_details, user_id, **properties):
    self.oxiclinc_details=oxiclinc_details
    self.user_id = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  first_file_name = None
  second_file_name = None
  def back_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiclinic',user_id=self.user_id)

  def Submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.first_file_name and not self.second_file_name:
      Notification('Upload Documents.' ).show()
    else:
      user_details = app_tables.oxi_users.get(oxi_id=self.user_id)
      print(user_details)
      oxiclinc_details = self.oxiclinc_details

      
      app_tables.oxiclinics.add_row(oxi_id=str(user_details['oxi_id']),
                                   oxi_name=user_details['oxi_username'],
                                   oxi_email=user_details['oxi_email'],
                                   oxi_password=user_details['oxi_password'],
                                   oxi_phone=int(user_details['oxi_phone']),
                                   oxiclinics_pincode=int(oxiclinc_details[4]),
                                   oxiclinics_Name=oxiclinc_details[0],
                                   oxiclinics_established_year=str(oxiclinc_details[1]),
                                   oxiclinics_State=oxiclinc_details[2],
                                   oxiclinics_District=oxiclinc_details[3],
                                   oxiclinics_address=oxiclinc_details[5],
                                   oxiclinics_capsules=int(oxiclinc_details[6]),
                                   oxiclinics_fees=oxiclinc_details[7],
                                   oxiclinics_medical_licence=oxiclinc_details[8],
                                   oxiclinics_building_licence=oxiclinc_details[9],
                                   
                                   oxiclinics_id=self.generate_unique_random_code())
                                  
                                  
      alert("You added oxiclinic successfully.")
      open_form('servicers_registration_form.services_register_add_service',id=self.user_id)

  def medical_file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name =file.get_name()
    self.file_name_1.text = self.first_file_name
    self.oxiclinc_details.append(file)

  def building_file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name =file.get_name()
    self.file_name_2.text = self.second_file_name
    self.oxiclinc_details.append(file)

  
  def generate_unique_random_code(self):
    prefix = "OC"
    while True:
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        code = prefix + random_numbers
        
        # Check if the code already exists in the data table
        existing_rows = app_tables.oxiclinics.get(oxiclinics_id=code)
        if not existing_rows:
            # If the code does not exist, return it
            return code
