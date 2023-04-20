import kivy
kivy.require('2.0.0')
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from kivy.core.window import Window
# from datetime import datetime
from kivymd.app import MDApp
# from typing import NoReturn
from kivy.uix.button import Button
import os
import sys
import subprocess
# Minhas classes
from libs.composite import Composite

MODE = 'development'

module_registration = ['main.py','composite.py']  # add modules that trigger reloading

class KvHandler(FileSystemEventHandler):
    def __init__(self, app, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.app = app

    def on_modified(self, event):
        ''' checks if there have been any change in the registered module '''
        for module in module_registration:
            if os.path.basename(event.src_path) == module:
                python_executable = sys.executable
                cmd_command = f'start cmd.exe /c "python main.py"'
                subprocess.run(cmd_command, shell=True)
                self.app.stop()
                exit()

def run(app: object):
    ''' register the observer with the folder to observe - '''
    o = Observer()
    o.schedule(KvHandler(app), os.getcwd(), recursive=True)
    o.start()

class AppReload(MDApp):
    def __init__(self, *args, **kwargs):
        super(AppReload, self).__init__(*args, **kwargs)
        Window.system_size = [1550, 900]
        Window.top = 30
        Window.left = 1920

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"  # "Purple", "Red"
        # return Button(text='Clique aqui 1!')
        return Composite()()

    def on_start(self):
        if MODE == 'development':
            run(self)
            
    def on_stop(self):
        # MDApp.get_running_app().stop()
        print('On stop')

if __name__ == "__main__":
    app = AppReload()
    app.run()














# -*- coding: utf-8 -*-
# import unittest
# from libs.tests.test_price_action import Test

# Test()()


# import plotly.graph_objects as go

# # Dados de exemplo (adicione mais dados OHLC conforme necessário)
# data = [
#     {
#         "bid": 0.0,
#         "ask": 0.0,
#         "last": 107700.0,
#         "volume": 1,
#         "time_msc": 1681327800062,
#         "flags": 4,
#         "volume_real": 1.0,
#     }
# ]

# # Preparar dados para o gráfico OHLC
# x = [item["time_msc"] for item in data]
# open_data = [item["bid"] for item in data]
# high_data = [item["ask"] for item in data]
# low_data = [item["bid"] for item in data]
# close_data = [item["last"] for item in data]

# # Criar e exibir o gráfico OHLC
# fig = go.Figure(go.Ohlc(x=x, open=open_data, high=high_data, low=low_data, close=close_data))

# fig.update_layout(title="Exemplo de Gráfico OHLC com Plotly", yaxis_title="Preço", xaxis_title="Tempo")

# fig.show()


'''
Price action é uma técnica de análise de mercado que se baseia no estudo dos movimentos de preços de um ativo ao longo do tempo. Os traders que utilizam essa abordagem geralmente analisam gráficos de preços e identificam padrões específicos que podem fornecer sinais de entrada e saída para negociações. Aqui estão alguns dos principais padrões de price action:

Barras de pin (Pin Bars): São velas com mechas longas e corpos pequenos, indicando rejeição de preços mais altos ou mais baixos. Uma barra de pin pode sinalizar uma reversão de tendência ou uma continuação, dependendo da direção da mecha e do contexto do mercado.

Barras internas (Inside Bars): São velas que estão completamente contidas dentro do alcance da vela anterior. Isso indica uma consolidação de preços e pode sinalizar uma pausa antes de uma continuação ou reversão da tendência.

Barras externas (Engulfing Bars): Ocorrem quando uma vela engolfa completamente a vela anterior, indicando uma forte mudança no sentimento do mercado. Uma barra de alta engolindo uma barra de baixa pode sinalizar o início de uma tendência de alta, enquanto uma barra de baixa engolindo uma barra de alta pode sinalizar uma tendência de baixa.

Duplo topo e duplo fundo: São padrões que ocorrem quando o preço testa uma resistência ou suporte duas vezes, respectivamente, antes de reverter a direção. Esses padrões podem sinalizar uma mudança na direção do mercado.

Retestes de suporte e resistência: Ocorrem quando os preços rompem um nível de suporte ou resistência e depois retornam para testar esse nível novamente. Esses retestes podem fornecer oportunidades de entrada ou saída, dependendo do contexto do mercado.

Canais e linhas de tendência: São linhas desenhadas no gráfico para conectar os topos e fundos consecutivos, ajudando a identificar áreas de suporte e resistência, bem como a direção geral do mercado.

Triângulos e bandeiras: São padrões de continuação formados durante uma tendência, quando o preço se consolida antes de seguir na direção original. Triângulos têm linhas de tendência convergentes, enquanto bandeiras têm linhas de tendência paralelas.
'''