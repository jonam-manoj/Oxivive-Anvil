from ._anvil_designer import signupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re


class signup(signupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
        username = self.text_box_1.text
        email = self.text_box_2.text
        password = self.text_box_3.text
        phone = self.text_box_4.text
        pincode = self.text_box_5.text
        pan = self.pan_text_box.text
        # app_tables.users.add_row(username, email, password, phone, pincode)
        # anvil.server.call('add_info',username, email, password, phone, pincode)
    
        try: 
          # If not present, proceed to insert the new user
          rows = app_tables.oxi_users.search()
          id = f"C{len(rows):04d}"
          app_tables.oxi_users.add_row(oxi_id = id, oxi_username =username, oxi_email = email, oxi_password = password, oxi_phone = int(phone),oxi_pincode=pincode,oxi_pan=pan)
          """This method is called when the button is clicked"""
          alert (self.text_box_2.text + ' added')
          open_form('login')
        except Exception as e:
          print(e)
          pass
    
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("login")
    
  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("servicers_registration_form.servicers_registration_form_main")

  def text_box_1_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.text_box_1.border="1px solid red"

  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_1.border="1px solid black"
    

  def text_box_2_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.text_box_2.border="1px solid red"

  def text_box_2_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_2.border="1px solid black"

  def text_box_3_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.text_box_3.border="1px solid red"

  def text_box_3_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_3.border="1px solid black"

  def text_box_4_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.text_box_4.border="1px solid red"

  def text_box_4_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_4.border="1px solid black"

  def text_box_5_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    self.text_box_5.border="1px solid red"

  def text_box_5_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.text_box_5.border="1px solid black"

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("login")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("signup")

  def link_2_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("home")


