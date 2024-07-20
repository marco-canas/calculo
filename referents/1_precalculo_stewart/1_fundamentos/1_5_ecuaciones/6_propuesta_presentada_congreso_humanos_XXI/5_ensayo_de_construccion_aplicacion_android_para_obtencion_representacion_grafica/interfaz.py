from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import matplotlib.pyplot as plt
import numpy as np

class GraphApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.input_label = Label(text='Ingrese la función matemática:')
        self.layout.add_widget(self.input_label)

        self.input_function = TextInput(hint_text='Ejemplo: np.sin(x)', multiline=False)
        self.layout.add_widget(self.input_function)

        self.plot_button = Button(text='Graficar')
        self.plot_button.bind(on_press=self.plot_function)
        self.layout.add_widget(self.plot_button)

        return self.layout

    def plot_function(self, instance):
        func_str = self.input_function.text
        x = np.linspace(-10, 10, 400)
        try:
            y = eval(func_str)
            plt.plot(x, y)
            plt.title('Grafica de la función')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid(True)
            plt.savefig('/storage/emulated/0/Download/plot.png')  # Guarda la imagen en una ubicación accesible en Android
            plt.clf()
        except Exception as e:
            self.input_label.text = 'Error en la función ingresada'

if __name__ == '__main__':
    GraphApp().run()
