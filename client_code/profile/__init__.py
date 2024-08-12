from ._anvil_designer import profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class profile(profileTemplate):
  def __init__(self, oxi_id=None, oxi_username=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(f"oxi_id in profile : {oxi_id}")
    print(f"oxi_username in profile : {oxi_username}")
    # Any code you write here will run before the form opens.

    user_details = anvil.server.call('get_user_details_by_id', oxi_id)
    print("server calling in profile form ")
    if 'error' in user_details:
            print(user_details['error'])
    else:
            # Print the retrieved user details in the console
      self.username_box.text = user_details['oxi_username']
      self.email_box.text = user_details['oxi_email']
      self.phone_box.text = user_details['oxi_phone']
      self.address_box.text = user_details['oxi_address']
      self.city_box.text = user_details['oxi_city']
      self.state_box.text = user_details['oxi_state']
      self.country_box.text = user_details['oxi_country']
      self.dob_box.text = user_details['oxi_dob']
      self.profile_image.source = user_details['oxi_profile']

  # for printing data 
      # self.username_box.text = user_details['oxi_username']
      # self.email_box.text = user_details['oxi_email']
      # self.phone_box.text = user_details['oxi_phone']
      # self.address_box.text = user_details['oxi_address']
      # self.city_box.text = user_details['oxi_city']
      # self.state_box.text = user_details['oxi_state']
      # self.country_box.text = user_details['oxi_country']
      # self.dob_box.text = user_details['oxi_dob']
      # self.profile_box.text = user_details['oxi_profile']

  
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

  def update_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Collect the data from the text boxes
        updated_username = self.username_box.text
        updated_email = self.email_box.text
        updated_phone = self.phone_box.text
        updated_address = self.address_box.text
        updated_city = self.city_box.text
        updated_state = self.state_box.text
        updated_country = self.country_box.text
        updated_dob = self.dob_box.text
        # updated_profile = self.profile_image.source

        # Call the server function to update the user details
        update_result = anvil.server.call(
            'update_user_details_by_id',
            self.oxi_id,
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

 
