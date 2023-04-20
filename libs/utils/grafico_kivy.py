# -*- coding: utf-8 -*-
import numpy as np
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

class RLCApp:
    def __init__(self):
        pass
        
    def __call__(self):
        return self.create_layout()

    def create_layout(self):
        layout = BoxLayout(orientation='vertical')
        self.plot = plt.figure()
        self.canvas = FigureCanvasKivyAgg(self.plot)
        layout.add_widget(self.canvas)
        self.sliders = {}
        for parameter in ['R', 'L', 'C']:
            self.add_slider(layout, parameter)
        self.update_graph()
        return layout

    def add_slider(self, layout, parameter):
        box = BoxLayout(orientation='horizontal')
        label = Label(text=f'{parameter}:')
        box.add_widget(label)
        slider = Slider(min=0, max=100, value=50)
        slider.bind(value=self.on_slider_value_change)
        box.add_widget(slider)
        layout.add_widget(box)
        self.sliders[parameter] = slider

    def on_slider_value_change(self, instance, value):
        self.update_graph()

    def update_graph(self):
        R = self.sliders['R'].value
        L = self.sliders['L'].value
        C = self.sliders['C'].value

        # Calcule a resposta em frequência para um circuito RLC série.
        freq = np.linspace(0, 10, 1000)
        response = R * L * C * np.sin(freq)

        self.plot.clear()
        plt.plot(freq, response)
        plt.xlabel('Frequência (Hz)')
        plt.ylabel('Resposta do Circuito')
        plt.title(f'Circuito RLC - R={R:.1f}, L={L:.1f}, C={C:.1f}')
        self.canvas.draw()