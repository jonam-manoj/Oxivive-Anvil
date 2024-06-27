from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = []
    # Set up the event handler for text changes in text_box_1
    self.text_box_1.set_event_handler('change', self.text_box_1_change)
    # Set up the event handler for clicks on text_box_2
    self.text_box_2.set_event_handler('x-click', self.text_box_2_focus)
    # Make text_box_2 initially invisible
    self.text_box_2.visible = False

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.aviailable_Hospital_Address')

  def primary_color_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.availabe_vehical_services')

  def primary_color_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dashboard.available_zym_address')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def text_box_1_change(self, **event_args):
      # Get the query from the text box
      query = self.text_box_1.text
      if len(query) > 3:
          # Call the server function to get location data
          result = anvil.server.call('get_location', query)
          self.repeating_panel_1.visible=True
          if 'error' in result:
              alert(result['error'])
          else:
              # Update the repeating panel with location suggestions
              self.repeating_panel_1.items = result['results']

  def text_box_2_focus(self, **event_args):
      # Make text_box_2 invisible and text_box_1 visible
      self.text_box_2.visible = False
      self.text_box_1.visible = True

  def update_text_boxes(self, address):
      # Update text_box_2 with the selected address
      self.text_box_2.text = address
      self.text_box_2.visible = True
      self.text_box_1.visible = False
      # Store the selected address in the variable
      self.selected_address = address
      print(self.selected_address)

  def primary_color_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("h")
