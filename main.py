from kivy.app import App
from kivy.uix.label import Label

class ArvexaApp(App):
    def build(self):
        return Label(text='ARVEXA Fabrikasi Calisiyor')

if __name__ == '__main__':
    ArvexaApp().run()
