from ._anvil_designer import walletTemplate
from anvil import *
from anvil.js import window
import anvil.server
from anvil.tables import app_tables

class wallet(walletTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    wallet_row = app_tables.oxi_wallet.get()  # Modify this line to suit your table structure
    
    if wallet_row:
        # Get the wallet balance
        balance = wallet_row['wallet_balance']
        
        # Display the wallet balance in label_4
        self.label_4.text = f"{balance} Rs"
    else:
        # Handle the case where there is no row in the 'wallet' table
        self.label_4.text = "Wallet data not found."  
    # user_id = self.id.text
    # if user_id:
    #     # Query the database directly
    #     user_row = app_tables.users.get(user_id=id)
    #     if user_row is not None:
    #         balance = user_row['wallet_balance']
    #         self.label_4.text = f"Wallet Balance: {balance}"
    #     else:
    #         self.label_4.text = "User not found."  
    # Any code you write here will run before the form opens.
  def button_4_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass
  # Event handler for Button 1
  def button_1_click(self, **event_args):
      self.text_box_2.text = "1000"
  
  # Event handler for Button 2
  def button_2_click(self, **event_args):
      self.text_box_2.text = "3000"
  
  # Event handler for Button 3
  def button_3_click(self, **event_args):
      self.text_box_2.text = "5000"

  def back_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
  # def setup_user_data(self):
  #       # Get the current user
        
        
  #       if user is not None:
  #           # Retrieve the user's data from the Users table
  #           user_data = app_tables.users.get(user_id=user.get_id())
            
  #           if user_data is not None:
  #               # Retrieve the wallet_balance from the user's data
  #               wallet_balance = user_data['wallet_balance']
                
  #               # Set the value of textbox_1 to the wallet_balance
  #               self.text_box_1.text = str(wallet_balance)
  #           else:
  #               # If user_data is None, handle the case where user data is not found
  #               self.text_box_1.text = "User data not found"
  #       else:
  #           # If user is None, handle the case where no user is logged in
  #           self.text_box_1.text = "No user logged in"

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      entered_number = self.text_box_2.text
      try:
          # Convert to float to handle numbers with decimals
          entered_number = float(entered_number)
          
          # Retrieve the current balance from the 'wallet' table
          # Assuming there is only one row in the table or you have a way to identify the correct row
          wallet_row = app_tables.oxi_wallet.get()  # Modify this line to suit your table structure
          
          if wallet_row:
              # Add the entered number to the current wallet balance
              new_balance = wallet_row['wallet_balance'] + entered_number
              
              # Update the 'wallet' table with the new balance
              wallet_row['wallet_balance'] = new_balance
              
              # Update the label_4 text to reflect the new balance
              self.label_4.text = f"{new_balance} Rs"
              
              # Provide some user feedback
              anvil.alert(f"The balance has been updated to {new_balance} Rs.")
              
          else:
              # Handle the case where there is no row in the 'wallet' table
              anvil.alert("No wallet data found. Please create an initial wallet entry.")
          
          # Optionally, clear the text box after updating the value
          self.text_box_2.text = ""
          
      except ValueError:
          # Handle the case where the input is not a valid number
          anvil.alert("Please enter a valid number.")
  
          
      except ValueError:
          # Handle the case where the input is not a valid number
          anvil.alert("Please enter a valid number.")
      window.location.assign("https://razorpay.me/@oxivivelifecareprivatelimited")
    