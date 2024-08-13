from ._anvil_designer import new_dashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class new_dashboard(new_dashboardTemplate):
  def __init__(self, oxi_id=None, oxi_username=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1.items = []
        # Set up the event handler for text changes in text_box_1
    self.text_box_1.set_event_handler('change', self.text_box_1_change)
        # Set up the event handler for clicks on text_box_2
    self.text_box_2.set_event_handler('x-click', self.text_box_2_focus)
        # Make text_box_2 initially invisible
    self.text_box_2.visible = False
    self.card_3.visible = False
    self.card_4.visible = False
    self.card_5.visible = False

    self.oxi_id = oxi_id  # Store the oxi_id
    self.oxi_username = oxi_username
    print(f"User ID in Dashboard opened: {self.oxi_id}")  # Print the user ID
    print(f"User Name in Dashboard: {self.oxi_username}")
    self.location_name = None  # Initialize location_name variable
    self.id_of_serviceprovider = None  # Initialize id_of_serviceprovider variable    
    

  
  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.card_3.visible:
        service_provider_id = self.card_3.tag.get('id_of_serviceprovider')
        service_type = 'OxiClinic'
        print(f"Service Provider ID (Clinic): {service_provider_id}")
    else:
        service_provider_id = None
        service_type = 'None'
        print("No clinic provider available.")

    print(f"Service Type: {service_type}")
    open_form('slot_book', oxi_id=self.oxi_id, location_name=self.location_name, id_of_serviceprovider=service_provider_id, service_type=service_type, oxi_username=self.oxi_username)
  
  def primary_color_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.card_5.visible:
        service_provider_id = self.card_5.tag.get('id_of_serviceprovider')
        service_type = 'OxiWheel'
        print(f"Service Provider ID (Wheels): {service_provider_id}")
    else:
        service_provider_id = None
        service_type = 'None'
        print("No wheels provider available.")
    print(f"Service Type in dashboard : {service_type}")
    open_form('slot_book', oxi_id=self.oxi_id, location_name=self.location_name, id_of_serviceprovider=service_provider_id, service_type=service_type, oxi_username=self.oxi_username)

 
  def  primary_color_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.card_4.visible:
        service_provider_id = self.card_4.tag.get('id_of_serviceprovider')
        service_type = 'OxiGym'  
        print(f"Service Provider ID (Gym) in dashboard: {service_provider_id}")
    else:
        service_provider_id = None
        service_type = 'None'
        print("No gym provider available.")
      
    print(f"Service Type: {service_type}")
    open_form('slot_book', oxi_id=self.oxi_id, location_name=self.location_name, id_of_serviceprovider=service_provider_id, service_type=service_type, oxi_username=self.oxi_username)


    
  def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        pass

  def text_box_1_change(self, **event_args):
        # Get the query from the text box
        query = self.text_box_1.text
        if len(query) > 3:
            # Call the server function to get location data
            result = anvil.server.call('get_location', query)
            self.repeating_panel_1.visible = True
            if 'error' in result:
                alert(result['error'])
            else:
                # Update the repeating panel with location suggestions
                self.repeating_panel_1.items = result['results']
                # Store the first location result in location_name
                if result['results']:
                    self.location_name = result['results'][0]['formatted']
                    print(f"Location Name: {self.location_name}")  # Print the location name in the console

  def repeating_panel_1_item_click(self, item, **event_args):
        # Called when a user clicks on an item in the repeating panel
        if item:
            self.location_name = item['formatted']  # Store the selected location
            print(f"Selected Location: {self.location_name}")  # Print the selected location in the console 

  def text_box_2_focus(self, **event_args):
        # Alert message when text_box_2 is clicked
  
        # Make text_box_2 invisible and text_box_1 visible
        self.text_box_2.visible = False
        self.text_box_1.visible = True

  def update_text_boxes(self, address):
        self.text_box_2.text = address
        self.text_box_2.visible = True
        self.text_box_1.visible = False
        
        # Extract the location name (we assume it's the first part of the address)
        location_name = address.split(",")[0].strip()
        
        # Call the server function to check the pin code in the tables
        result = anvil.server.call('check_pincode_in_tables', location_name)
        
        # Show or hide cards based on the results
        self.card_3.visible = result['oxiclinics_exists']
        self.card_3.tag = {'id_of_serviceprovider': result['id_of_serviceprovider_clinic']}
    
        self.card_4.visible = result['oxiwheels_exists']
        self.card_4.tag = {'id_of_serviceprovider': result['id_of_serviceprovider_gym']}
    
        self.card_5.visible = result['oxigyms_exists']
        self.card_5.tag = {'id_of_serviceprovider': result['id_of_serviceprovider_wheel']}

         # Print the IDs of the service providers found
        print(f"Clinic ID: {result['id_of_serviceprovider_clinic']}")
        print(f"Gym ID: {result['id_of_serviceprovider_gym']}")
        print(f"Wheel ID: {result['id_of_serviceprovider_wheel']}")

  def primary_color_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form('home')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('home')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('notifications', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bookings', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('reports', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('profile', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

  # def open_profile_form(self):
  #       # Create an instance of the profile form and pass oxi_id and oxi_username
  #       profile_form = profile(oxi_id=self.oxi_id, oxi_username=self.oxi_username)
  #       # Open the profile form
  #       self.open_form(profile_form)
