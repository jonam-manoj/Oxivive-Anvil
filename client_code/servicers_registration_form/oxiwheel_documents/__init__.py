from ._anvil_designer import oxiwheel_documentsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
import string

class oxiwheel_documents(oxiwheel_documentsTemplate):
  def __init__(self, oxiwheel_details, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id =user_id
    self.oxiwheel_details=oxiwheel_details

    # Any code you write here will run before the form opens.
  first_file_name = None
  second_file_name = None
  def back_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiwheel',user_id=self.user_id)

  def Submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if not self.first_file_name and not self.second_file_name:
      Notification('Upload Documents.' ).show()
    else:
      user_details = app_tables.oxi_users.get(oxi_id=self.user_id)
      print(user_details)
      oxiwheel_details = self.oxiwheel_details
      print(oxiwheel_details)
      app_tables.oxiwheels.add_row(oxi_id=str(user_details['oxi_id']),
                                   oxi_name=user_details['oxi_username'],
                                   oxi_email=user_details['oxi_email'],
                                   oxi_password=user_details['oxi_password'],
                                   oxi_phone=int(user_details['oxi_phone']),
                                   oxiwheels_pincode=int(oxiwheel_details[4]),
                                   oxiwheels_Name=oxiwheel_details[0],
                                   oxiwheels_model_year=str(oxiwheel_details[1]),
                                   oxiwheels_State=oxiwheel_details[2],
                                   oxiwheels_District=oxiwheel_details[3],
                                   oxiwheels_address=oxiwheel_details[5],
                                   oxiwheels_capsules=int(oxiwheel_details[6]),
                                   oxiwheels_fees=oxiwheel_details[7], 
                                   oxiwheels_vehicle_rc=oxiwheel_details[8],
                                   oxiwheels_driving_licence=oxiwheel_details[9],
                                  oxiwheels_id=self.generate_unique_random_code())
                                  
      alert("You added oxiwheel successfully.")
      open_form('servicers_registration_form.services_register_add_service',id=self.user_id)

  def medical_file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.first_file_name =file.get_name()
    self.file_name_1.text = self.first_file_name
    self.oxiwheel_details.append(file)

  def building_file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.second_file_name =file.get_name()
    self.file_name_2.text = self.second_file_name
    self.oxiwheel_details.append(file)

  def generate_unique_random_code(self):
    prefix = "OW"
    while True:
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        code = prefix + random_numbers
        
        # Check if the code already exists in the data table
        existing_rows = app_tables.oxiwheels.get(oxiwheels_id=code)
        if not existing_rows:
            # If the code does not exist, return it
            return code

