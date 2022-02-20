from kivy.app import App
from kivy.uix.button import Button      

class ExempluApp(App):
    def build(self):
        button = Button(text='Hello world', font_size=50)
        return button

if __name__ == '__main__' :
    ExempluApp().run()
 