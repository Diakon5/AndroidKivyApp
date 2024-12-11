from kivy.uix.textinput import TextInput
import re
class FilteredTextInput(TextInput):
    pattern = re.compile("\'\"\:\;\`")
    def insert_text(self, substring, from_undo=False):
        
        substring = re.sub(self.pattern,"",substring)
        return super().insert_text(substring, from_undo=from_undo)