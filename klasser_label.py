#https://realpython.com/python-getter-setter/

class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value


label = Label("Fruits", "JetBrains Mono NL")
print(label.get_text()) #fruits
label.set_text("Vegetables")
print(label.get_text()) #vegetables
print(label.get_font()) #JetBrains