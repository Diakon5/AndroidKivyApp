from kivy.uix.textinput import TextInput

from kivy.properties import BooleanProperty
import re


class FilteredTextInput(TextInput):
    pattern = re.compile("[\'\":;`]")
    text_valid = BooleanProperty(False)
    accept_empty = BooleanProperty(False)
    def on_text(self, obj, text):
        if not self.accept_empty and (len(text)==0 or text.isspace()):
            self.text_valid = False
            return
        self.text_valid = True
    def insert_text(self, substring, from_undo=False):
        substring = re.sub(self.pattern,"",substring)
        return super().insert_text(substring, from_undo=from_undo)