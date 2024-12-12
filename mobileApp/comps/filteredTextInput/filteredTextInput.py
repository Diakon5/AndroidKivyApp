from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty
import re
class FilteredTextInput(TextInput):
    pattern = re.compile("\'\"\:\;\`")
    accept_empty = BooleanProperty(False)
    def on_text_validate(self):
        if not self.accept_empty and (len(self.text)==0 or not self.text.isspace()):
            return False
        return True
    def insert_text(self, substring, from_undo=False):
        
        substring = re.sub(self.pattern,"",substring)
        return super().insert_text(substring, from_undo=from_undo)