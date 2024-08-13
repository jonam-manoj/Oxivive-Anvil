from ._anvil_designer import bookingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class bookings(bookingsTemplate):
  def __init__(self ,oxi_id=None,  oxi_username=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.oxi_id = oxi_id
    self.oxi_username = oxi_username
    print(f"oxi_id in booking  : {oxi_id}")
    print(f"oxi_username in booking : {oxi_username}")
    

    # Any code you write here will run before the form opens.

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('home')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bookings', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('notifications', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('new_dashboard', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('profile', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('new_dashboard')
    
