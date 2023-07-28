from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text="My first Button",
                      font_size=40,
                      on_press = self.btn_press,
                      background_color = [.13,.55,.13,1],
                      background_normal = "")
    def btn_press(self, instance):
        instance.text = "I am pressed"

if __name__=="__main__":
    MyApp().run()