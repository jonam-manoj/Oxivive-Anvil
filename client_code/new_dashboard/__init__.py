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
        
        location_name = address.split(",")[0].strip()

        # Call the server function to check the pin code in the tables
        result = anvil.server.call('check_pincode_in_tables', location_name)

        # Prepare items for the repeating panel
        service_providers = []
        
        if result['oxiclinics_exists']:
            service_providers.append({
                'service_type': 'OxiClinic',
                'service_provider_id': result['id_of_serviceprovider_clinic'],
                'name': 'Clinic',
                'image': 'clinic_image.png'  # Replace with the actual image path
            })
        
        if result['oxiwheels_exists']:
            service_providers.append({
                'service_type': 'OxiWheel',
                'service_provider_id': result['id_of_serviceprovider_wheel'],
                'name': 'Wheels',
                'image': 'wheels_image.png'  # Replace with the actual image path
            })
        
        if result['oxigyms_exists']:
            service_providers.append({
                'service_type': 'OxiGym',
                'service_provider_id': result['id_of_serviceprovider_gym'],
                'name': 'Gym',
                'image': 'gym_image.png'  # Replace with the actual image path
            })

        self.repeating_panel_2.items = service_providers  # Update the repeating panel with items

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
