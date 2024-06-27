from ._anvil_designer import services_register_add_serviceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...servicers import user_id

class services_register_add_service(services_register_add_serviceTemplate):
  def __init__(self, id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_id = id 
    

    # Any code you write here will run before the form opens.

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_registration_form_main')

  def add_oxiclinic_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiclinic', user_id=self.user_id)

  def add_oxiwheel_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxiwheel', user_id=self.user_id)

  def add_oxigym_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.servicers_register_add_oxigym', user_id=self.user_id)

  def services_list_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('servicers_registration_form.services_list',user_id=self.user_id)

  def servicers_register_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    oxiclinic = app_tables.oxiclinics.search(oxi_id=str(self.user_id))
    oxiwheel = app_tables.oxiwheels.search(oxi_id =str( self.user_id))
    oxigym = app_tables.oxigyms.search(oxi_id =str( self.user_id))

    if oxiclinic or oxiwheel or oxigym:

      user_id.user_id=self.user_id
      
      open_form('servicers.servicers_dashboard')
    else:
      alert('If you want complete registration, please add at least one service')

  