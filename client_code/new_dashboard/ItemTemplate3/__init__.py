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

    # Any code you write here will run before the form opens.
  def form_show(self, **event_args):
        # Set the image source and label text from the item data
        self.image_1.source = self.item['image_source']
        self.label_1.text = self.item['label_text']
        self.label_2.text = self.item['address']
        self.button_1.tag = {'id_of_serviceprovider': self.item['id_of_serviceprovider']}

  def button_1_click(self, **event_args):
    service_provider_id = self.button_1.tag.get('id_of_serviceprovider')
    # Handle the click event, for example, by opening another form
    open_form('slot_book', id_of_serviceprovider=service_provider_id)
