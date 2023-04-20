# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:29:12 2023

@author: jrmfi
"""
from typing import List
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from libs.utils.grafico_kivy import RLCApp
from libs.pages.dashboard import Dashboard

class Composite(BoxLayout):

    def __init__(self, *args, **kwargs) -> None:
        super(Composite, self).__init__(*args, **kwargs)
        self.orientation = 'vertical'
        
    def __call__(self):
        sm = ScreenManager()
        # grafico = RLCApp()()
        # screen = MDScreen(name='principal')
        # icon = Button(text='Clique aqui 1!',
        #               size_hint=(1,1))
        # screen.add_widget(grafico)
        sm.add_widget(Dashboard())
        self.add(sm)
        return self
    def add(self, component) -> None:
        self.add_widget(component)

    def remove(self, component) -> None:
        self.remove_widget(component)

    def is_composite(self) -> bool:
        return True