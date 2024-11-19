from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):  # Fixed method name
        super().__init__(**kwargs)
        self.names = ["Ornysha", "Zinia", "Sristi", "Raya", "Ava"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name, font_size=24)  # Removed `color` attribute
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
