from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        ## Заголовок
        main_layout = FloatLayout()
        self.header = Label(text="Счетчик", font_size=55,size_hint=(0.8,0.2),pos_hint={'center_x': 0.5,'top': 1}, color="black")
        main_layout.add_widget(self.header)

        ## Сам счетчик
        counter_layout = BoxLayout(size_hint=(0.8,None),size=(1,80),pos_hint={'center_x': 0.5,'center_y': 0.6})
        button1 = Button(
                    text='-',
                    font_size=55,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    background_color = 'orange',
                    background_normal='',
                )
        button1.bind(on_press=self.on_button_press)
        self.number = TextInput(
            input_filter='int', multiline=False, readonly=False, halign="right", font_size=55,
        )
        button2 = Button(
                    text='+',
                    font_size=55,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    background_color = 'orange',
                    background_normal='',
                )
        button2.bind(on_press=self.on_button_press)
        counter_layout.add_widget(button1)
        counter_layout.add_widget(self.number)
        counter_layout.add_widget(button2)
        main_layout.add_widget(counter_layout)
 
        ## Кнопка очистить
        reset_button = Button(
                    text="C",
                    pos_hint={"center_x": 0.5, "center_y": 0.2},
                    font_size=55,
                    size_hint=(0.3,0.15),
                    background_color = 'orange',
                    background_normal='',
                )
        reset_button.bind(on_press=self.on_button_press)
        main_layout.add_widget(reset_button)
 
        return main_layout
    
    def on_button_press(self, command):
        current = self.number.text
        button_text = command.text

        if current == "":
            current = "0"
        if button_text == "C":
            self.number.text = "0"
        elif button_text == "+":
            self.number.text = str(int(current)+1)
        elif button_text == "-":
            self.number.text = str(int(current)-1)

if __name__ == "__main__":
    app = MainApp()
    app.run()
