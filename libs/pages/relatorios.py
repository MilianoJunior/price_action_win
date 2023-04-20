# -*- coding: utf-8 -*-

import time
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen

class Rerport(MDScreen):
    
    start = time.time()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.criar_layouts())
        
    def criar_layouts(self):
        layout_principal = BoxLayout(orientation="vertical")
        
        # self.grafico = # Adicione aqui o widget de gráfico
        # self.botoes = # Adicione aqui o layout com os botões
        # self.dados_mercado = # Adicione aqui o widget com os dados do mercado

        layout_principal.add_widget(self.grafico)
        layout_principal.add_widget(self.botoes)
        layout_principal.add_widget(self.dados_mercado)

        return layout_principal
        
    def get_name(self):
        return 'Relatorios'
    
    def desempenho(self):
        return round(self.start - time.time(), 3)