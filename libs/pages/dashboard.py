# -*- coding: utf-8 -*-

import time
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from libs.config.colors import thema
from libs.utils.graficos import CustomGraph

class Dashboard(MDScreen):
    
    start = time.time()
    grafico = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(self.criar_layouts())
        
    def criar_layouts(self):
        layout_principal = MDBoxLayout(orientation="vertical",
                                       md_bg_color=thema['background'])
        graph_config = {
            'size_hint': (1, 0.7),
            'pos_hint': {'top': 1}
        }
        graph = CustomGraph(graph_config).graph
        # layout_principal = MDBoxLayout(orientation="vertical",
        #                                md_bg_color=thema['background'])
        
        # self.grafico = # Adicione aqui o widget de gráfico
        # self.botoes = # Adicione aqui o layout com os botões
        # self.dados_mercado = # Adicione aqui o widget com os dados do mercado

        layout_principal.add_widget(graph)
        # layout_principal.add_widget(self.botoes)
        # layout_principal.add_widget(self.dados_mercado)

        return layout_principal
        
    def get_name(self):
        return 'Relatorios'
    
    def desempenho(self):
        return round(self.start - time.time(), 3)
    

    
    
    
    
