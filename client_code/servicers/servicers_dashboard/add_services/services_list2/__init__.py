from ._anvil_designer import services_list2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class services_list2(services_list2Template):
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
      user_info["serial_no"] = i  # Assuming you want to include a serial number
      user_info["clinic_id"] = row["oxiclinics_id"]
      user_info["Oxiclinics_Name"] = row["oxiclinics_Name"]
      user_info["State"] = row["oxiclinics_State"]

      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    rows = app_tables.oxiwheels.search(oxi_id=str(self.user_id))
    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}

      # Assign data to dictionary keys
      user_info["serial_no"] = i  # Assuming you want to include a serial number
      user_info["clinic_id"] = row["oxiwheels_id"]
      user_info["Oxiclinics_Name"] = row["oxiwheels_Name"]
      user_info["State"] = row["oxiwheels_State"]

      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    rows = app_tables.oxigyms.search(oxi_id=str(self.user_id))

    List_oxiclinics = []
    for i, row in enumerate(rows, start=1):
      # Initialize dictionary to store row data
      user_info = {}

      # Assign data to dictionary keys
      user_info["serial_no"] = i  # Assuming you want to include a serial number
      user_info["clinic_id"] = row["oxigyms_id"]
      user_info["Oxiclinics_Name"] = row["oxigyms_Name"]
      user_info["State"] = row["oxigyms_State"]

      # Append dictionary to list
      List_oxiclinics.append(user_info)

    # Set repeating panel items
    self.repeating_panel_1.items = List_oxiclinics

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("servicers.servicers_dashboard.add_services", id=self.user_id
    )

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.data_grid_1.rows_per_page = int(self.text_box_1.text) + 1
