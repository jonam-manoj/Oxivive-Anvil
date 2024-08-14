from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.role = 'card-spacing'
    self.id_of_serviceprovider = None

    # Any code you write here will run before the form opens.
  def form_show(self, **event_args):
        # Set the image source and label text from the item data
        self.image_1.source = self.item['image_source']
        self.label_1.text = self.item['label_text']
        self.label_2.text = self.item['address']
        self.id_of_serviceprovider = self.item['id_of_serviceprovider']

  def button_1_click(self, **event_args):
    # Access the data stored in the tag using the dictionary syntax
    # service_provider_id = self.button_1.tag['id_of_serviceprovider']
    # image_source = self.button_1.tag['image_source']
    # label_text = self.button_1.tag['label_text']
    # address = self.button_1.tag['address']

    # Open the `slot_book` form and pass the data as arguments
   open_form('slot_book', 
                  id_of_serviceprovider=self.id_of_serviceprovider, 
                  image_source=self.image_1.source, 
                  label_text=self.label_1.text, 
                  address=self.label_2.text)