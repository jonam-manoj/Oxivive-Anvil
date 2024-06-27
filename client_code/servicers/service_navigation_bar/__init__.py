from ._anvil_designer import service_navigation_barTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import user_id



class service_navigation_bar(service_navigation_barTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.id = user_id.user_id

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('servicers.servicers_dashboard')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('servicers.servicers_dashboard.notification')

  def link_3_click(self, **event_args):
    
    data = app_tables.oxi_users.get(oxi_id=self.id)
   
    """This method is called when the link is clicked"""
    open_form('servicers.servicers_dashboard.profile', user_data = data)

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('servicers.servicers_dashboard.support')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('login')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('servicers.servicers_dashboard.add_services',id=user_id.user_id)
