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
        self.repeating_panel_2.scroll_direction = 'horizontal'
        self.repeating_panel_2.reverse_order = True  # This will reverse the scroll direction (bottom to top)
 # This will reverse the scroll direction

        self.repeating_panel_2.role = 'repeating-panel-rtl'




        self.repeating_panel_2.items = []  # Initialize repeating panel items
        self.oxi_id = oxi_id  # Store the oxi_id
        self.oxi_username = oxi_username
        print(f"User ID in Dashboard opened: {self.oxi_id}")
        print(f"User Name in Dashboard: {self.oxi_username}")
        self.location_name = None  # Initialize location_name variable

    def update_text_boxes(self, address):
        self.text_box_2.text = address
        self.text_box_2.visible = True
        self.text_box_1.visible = False
    
        # Extract the location name (we assume it's the first part of the address)
        location_name = address.split(",")[0].strip()
    
        # Call the server function to check the pin code in the tables
        result = anvil.server.call('check_pincode_in_tables', location_name)
    
        # Initialize a list to hold the items for the repeating panel
        repeating_panel_items = []
    
        # Check each result and add to the repeating panel items
        if result['oxiclinics_exists']:
            address = app_tables.oxiclinics.get(oxi_id=result['id_of_serviceprovider_clinic'])['oxiclinics_address']
            repeating_panel_items.append({
                'image_source': '_/theme/Untitled design (1).png',
                'label_text': 'OXICLINIC',
                'address': address,
                'id_of_serviceprovider': result['id_of_serviceprovider_clinic']
            })
    
        if result['oxiwheels_exists']:
            address = app_tables.oxiwheels.get(oxi_id=result['id_of_serviceprovider_wheel'])['oxiwheels_address']
            repeating_panel_items.append({
                'image_source': '_/theme/ed and (1).png',
                'label_text': 'OXIWHEELS',
                'address': address,
                'id_of_serviceprovider': result['id_of_serviceprovider_wheel']
            })
    
        if result['oxigyms_exists']:
            address = app_tables.oxigyms.get(oxi_id=result['id_of_serviceprovider_gym'])['oxigyms_address']
            repeating_panel_items.append({
                'image_source': '_/theme/Untitled design (2).png',
                'label_text': 'OXIGYM',
                'address': address,
                'id_of_serviceprovider': result['id_of_serviceprovider_gym']
            })
    
        # Update the repeating panel with the items
        self.repeating_panel_2.items = repeating_panel_items
    
        # Print the IDs of the service providers found
        print(f"Clinic ID: {result['id_of_serviceprovider_clinic']}")
        print(f"Gym ID: {result['id_of_serviceprovider_gym']}")
        print(f"Wheel ID: {result['id_of_serviceprovider_wheel']}")



    def primary_color_1_click(self, **event_args):
        self.handle_service_selection('OxiClinic')
    
    def primary_color_1_copy_click(self, **event_args):
        self.handle_service_selection('OxiWheel')
    
    def primary_color_1_copy_2_click(self, **event_args):
        self.handle_service_selection('OxiGym')

    def handle_service_selection(self, service_type):
        selected_item = None
        for item in self.repeating_panel_2.items:
            if item['service_type'] == service_type:
                selected_item = item
                break
        
        if selected_item:
            print(f"Service Provider ID ({service_type}): {selected_item['service_provider_id']}")
            open_form('slot_book', oxi_id=self.oxi_id, location_name=self.location_name, id_of_serviceprovider=selected_item['service_provider_id'], service_type=service_type, oxi_username=self.oxi_username)
        else:
            print(f"No provider available for {service_type}.")

    def text_box_1_change(self, **event_args):
        query = self.text_box_1.text
        if len(query) > 3:
            result = anvil.server.call('get_location', query)
            self.repeating_panel_1.visible = True
            if 'error' in result:
                alert(result['error'])
            else:
                self.repeating_panel_1.items = result['results']
                if result['results']:
                    self.location_name = result['results'][0]['formatted']
                    print(f"Location Name: {self.location_name}")

    def repeating_panel_1_item_click(self, item, **event_args):
        if item:
            self.location_name = item['formatted']
            print(f"Selected Location: {self.location_name}")
            self.update_text_boxes(self.location_name)

    def text_box_2_focus(self, **event_args):
        self.text_box_2.visible = False
        self.text_box_1.visible = True

    def primary_color_2_click(self, **event_args):
        open_form('home')

    def link_6_click(self, **event_args):
        open_form('home')

    def link_2_click(self, **event_args):
        open_form('notifications', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

    def link_3_click(self, **event_args):
        open_form('bookings', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

    def link_4_click(self, **event_args):
        open_form('reports', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

    def link_1_click(self, **event_args):
        open_form('profile', oxi_id=self.oxi_id, oxi_username=self.oxi_username)
