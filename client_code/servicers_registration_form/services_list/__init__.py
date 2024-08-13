from ._anvil_designer import services_listTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import servicer_id

class services_list(services_listTemplate):
  def __init__(self, user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = user_id
    
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
   
    rows = app_tables.oxiclinics.search(oxi_id=str(self.user_id)) 
    
    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}
      
      # Assign data to dictionary keys
      user_info['serial_no'] = i  # Assuming you want to include a serial number
      user_info['clinics_id'] = row["oxiclinics_id"]
      user_info['Oxiclinics_Name'] = row['Oxiclinics_Name']
      user_info['State'] = row['State']
      
      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    rows =app_tables.oxiwheels.search(oxi_id=str(self.user_id))
    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}
      
      # Assign data to dictionary keys
      user_info['serial_no'] = i  # Assuming you want to include a serial number
      user_info['clinic_id'] = row["oxywheel_id"]
      user_info['Oxiclinics_Name'] = row['Oxiwheels_Name']
      user_info['State'] = row['State']
      
      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""  
    rows =app_tables.oxigyms.search(oxi_id=str(self.user_id))
    
    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}
      
      # Assign data to dictionary keys
      user_info['serial_no'] = i  # Assuming you want to include a serial number
      user_info['clinic_id'] = row["oxigym_id"]
      user_info['Oxiclinics_Name'] = row['Oxigyms_Name']
      user_info['State'] = row['State']
      
      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.services_register_add_service', id=self.user_id)

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.data_grid_1.rows_per_page = int(self.text_box_1.text) + 1
