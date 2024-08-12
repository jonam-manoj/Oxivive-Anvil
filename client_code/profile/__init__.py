from ._anvil_designer import profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class profile(profileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('notifications')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bookings')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('home')
