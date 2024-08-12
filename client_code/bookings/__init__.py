from ._anvil_designer import bookingsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class bookings(bookingsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('home')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bookings')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('notifications')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('new_dashboard')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('profile')
