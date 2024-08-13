from ._anvil_designer import profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime  # Import datetime module

class profile(profileTemplate):
    def __init__(self, oxi_id=None, oxi_username=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        print(f"oxi_id in profile : {oxi_id}")
        print(f"oxi_username in profile : {oxi_username}")
        self.oxi_id = oxi_id  # Store the oxi_id in the instance for later use
        # Any code you write here will run before the form opens.

        user_details = anvil.server.call('get_user_details_by_id', oxi_id)
        print("server calling in profile form ")
        if 'error' in user_details:
            print(user_details['error'])
        else:
            # Print the retrieved user details in the console
            self.username_box.text = user_details['oxi_username']
            self.email_box.text = user_details['oxi_email']
            self.phone_box.text = str(user_details['oxi_phone'])
            self.address_box.text = user_details['oxi_address']
            self.city_box.text = user_details['oxi_city']
            self.state_box.text = user_details['oxi_state']
            self.country_box.text = user_details['oxi_country']

            # Handle the date of birth, checking if it's None
            if user_details['oxi_dob'] is not None:
                self.date_picker_1.date = user_details['oxi_dob']  # Set the date picker value
            else:
                self.date_picker_1.date = None  # or any default value you prefer
            self.profile_image.source = user_details['oxi_profile']

    def update_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Collect the data from the text boxes
        updated_username = self.username_box.text
        updated_email = self.email_box.text
        
        # Convert phone to number
        updated_phone = int(self.phone_box.text) if self.phone_box.text.isdigit() else None
        
        updated_address = self.address_box.text
        updated_city = self.city_box.text
        updated_state = self.state_box.text
        updated_country = self.country_box.text
        
        # Convert DOB to date object
        updated_dob = None
        if self.date_picker_1.date:
            updated_dob = self.date_picker_1.date  # Get date from DatePicker

        updated_profile = self.profile_image.source

        # Call the server function to update the user details
        update_result = anvil.server.call(
            'update_user_details_by_id',
            self.oxi_id,  # Use the instance variable self.oxi_id
            updated_username,
            updated_email,
            updated_phone,
            updated_address,
            updated_city,
            updated_state,
            updated_country,
            updated_dob,
            updated_profile
        )
        
        # Provide feedback to the user
        alert(update_result)

    def link_2_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('notifications', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

    def link_3_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('bookings', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

    def link_4_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('reports', oxi_id=self.oxi_id, oxi_username=self.oxi_username)

    def link_6_click(self, **event_args):
        """This method is called when the link is clicked"""
        open_form('home')

    def file_loader_1_change(self, file, **event_args):
        """This method is called when a new file is loaded into the FileLoader"""
        if file:
            # Update the profile image component with the new file
            self.profile_image.source = file
            
            # Save the uploaded image to the database
            update_result = anvil.server.call(
                'update_user_details_by_id',
                self.oxi_id,  # User ID
                self.username_box.text,
                self.email_box.text,
                self.phone_box.text,
                self.address_box.text,
                self.city_box.text,
                self.state_box.text,
                self.country_box.text,
                self.date_picker_1.date,
                file  # Uploaded file
            )
            
            # Provide feedback to the user
            alert(update_result)

      
    

    

    
