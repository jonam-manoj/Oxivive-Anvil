from ._anvil_designer import profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class profile(profileTemplate):
  def __init__(self,user_data, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.c_id.text=user_data['oxi_id']
    self.name.text=user_data['oxi_username']
    self.email.text=user_data['oxi_email']
    self.phone.text=user_data['oxi_phone']
    self.address.text=user_data['oxi_address']
    self.image_1.source=user_data['oxi_profile']
    
    

  

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.image_1.source=file

  

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.name.enabled = True

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.email.enabled = True

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.phone.enabled = True

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.address.enabled = True

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    id = self.c_id.text
    name = self.name.text
    email = self.email.text
    phone = self.phone.text
    address = self.address.text
    profile = self.image_1.source
    user_row = app_tables.users.get(id=id)
    
    # Check if the user exists
    if user_row is not None:
        # Update the attributes of the user row
        # user_row['username'] = name
        # user_row['email'] = email
        # user_row['phone'] = int(phone)
        # user_row['address'] = address
        # Save the changes to the table
      user_row.update(username=name, email=email, phone=int(phone), address=address,profile=profile)
      self.phone.enabled = False
      self.name.enabled = False
      self.email.enabled = False
      self.address.enabled = False
      alert("Profile is updated sucessfully. ")
      
      
    
