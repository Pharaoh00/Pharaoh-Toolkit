import string
import random

class PasswordGenerator:

    s_lower = string.ascii_lowercase
    s_letter = string.ascii_letters
    s_digits = string.digits
    s_punctuation = string.punctuation

    def __init__(self, ask_type, ask_number):
        self.ask_type = ask_type
        self.ask_number = ask_number

    def pass_all(self):
        if str(self.ask_type) == "fraca": # caso fraca
            self.ask_type = self.s_lower
        if str(self.ask_type) == "media": # caso media
            self.ask_type = self.s_letter
        if str(self.ask_type) == "forte": # caso forte
            self.ask_type = self.s_letter + self.s_digits
        if str(self.ask_type) == "insana": # caso insana
            self.ask_type = self.s_letter + self.s_digits + self.s_punctuation

        return "".join(random.sample(self.ask_type, int(self.ask_number))) # Junção e Randomização.
