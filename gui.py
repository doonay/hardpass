from kivy.app import App
from kivy.core.window import Window
#from kivy.uix.button import Button
#from kivy.uix.textinput import TextInput
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.label import Label
from hardpass import get_cool_password

class Screen(FloatLayout):
    def on_btn_release(self):
        self.ids.passwd_kv.text = get_cool_password()


class GuiApp(App):
    print(Window.size)
    Window.size = (200, 80)
    print(Window.size)

    def on_start(self, **kwargs):
        # сразу при запуске выводит в лэйбл - готовый пароль
        self.root.ids.passwd_kv.text = get_cool_password()

    def build(self):
        return Screen()



if __name__ == '__main__':
	GuiApp().run()
