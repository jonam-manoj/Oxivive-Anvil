from ._anvil_designer import loginTemplate
from anvil import alert, open_form
from anvil.tables import app_tables
from ..servicers import user_id

class login(loginTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def primary_color_1_click(self, **event_args):
        email = self.text_box_1.text
        password = self.text_box_2.text
        
        try:
            # Search for the user in the Data Table
            users_table = app_tables.oxi_users
            user = users_table.get(oxi_email=email, oxi_password=password)
            
            if user:
                if user['oxi_usertype'] =='service provider':
                  user_id.user_id = user['oxi_id']
                  open_form('servicers.servicers_dashboard')
                else:
                  open_form('dashboard')
            else:
                alert("Invalid email or password. Please try again.")
        
        except Exception as e:
            alert(f"Error: {e}")

    def back_click(self, **event_args):
        open_form("home")

    def text_box_1_focus(self, **event_args):
      """This method is called when the TextBox gets focus"""
      self.text_box_1.border = "1px solid red"

    def text_box_1_lost_focus(self, **event_args):
      """This method is called when the TextBox loses focus"""
      self.text_box_1.border = "1px solid black"

    def text_box_2_focus(self, **event_args):
      """This method is called when the TextBox gets focus"""
      self.text_box_2.border = "1px solid red"

    def text_box_2_lost_focus(self, **event_args):
      """This method is called when the TextBox loses focus"""
      self.text_box_2.border = "1px solid black"

    def link_5_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("signup")

    def link_4_click(self, **event_args):
      """This method is called when the link is clicked"""
      open_form("login")
