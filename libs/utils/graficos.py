from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
from datetime import timedelta
from matplotlib.animation import FuncAnimation
from kivy_garden.graph import Graph, MeshLinePlot
import time

start = time.time()

class CustomGraph:
    def __init__(self, graph_config):
        self.graph = Graph(size_hint=graph_config['size_hint'],
                  pos_hint=graph_config['pos_hint'],
                  background_color=(0, 0, 0, 0),
                  x_axis_label='X',
                  y_axis_label='Y',
                  x_grid_label=True,
                  y_grid_label=True,
                  padding=5,
                  x_grid=True,
                  y_grid=True,
                  xmin=0,
                  xmax=100,
                  ymin=-1,
                  ymax=1,
                  xlabel='X Axis',
                  ylabel='Y Axis')

        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = [(x, (x / 100) ** 2) for x in range(0, 101)]
        self.graph.add_plot(plot)


# class RealTimeOHLCPlotter:
#     def __init__(self, timeframe='1min'):
#         self.timeframe = timeframe
#         self.fig, self.ax = plt.subplots()
#         self.ohlc_data = []
#         self.current_price_line = None
#         self.tick_count = 0
#         # self.animation = FuncAnimation(self.fig, self.plot_ohlc, interval=100)
#         self.animation = FuncAnimation(self.fig, self.plot_ohlc, interval=0.1, save_count=100)

#     def __call__(self):
#         return self
    
#     def add_tick(self, tick):
#         self.tick_count += 1
#         timestamp = tick["time"].to_pydatetime()
#         price = tick["last"]

#         # Arredonda o timestamp para o timeframe especificado
#         rounded_timestamp = self.round_timestamp_to_timeframe(timestamp, self.timeframe)

#         # Atualiza os dados OHLC
#         if len(self.ohlc_data) == 0 or self.ohlc_data[-1][0] != mdates.date2num(rounded_timestamp):
#             self.ohlc_data.append([mdates.date2num(rounded_timestamp), price, price, price, price])
#         else:
#             self.ohlc_data[-1][2] = max(self.ohlc_data[-1][2], price)  # High
#             self.ohlc_data[-1][3] = min(self.ohlc_data[-1][3], price)  # Low
#             self.ohlc_data[-1][4] = price  # Close

#         self.current_price = price

#     def round_timestamp_to_timeframe(self, timestamp, timeframe):
#         if timeframe.endswith('min'):
#             minutes = int(timeframe[:-3])
#             return timestamp.replace(second=0, microsecond=0) - timedelta(minutes=timestamp.minute % minutes)
#         elif timeframe.endswith('H'):
#             hours = int(timeframe[:-1])
#             return timestamp.replace(minute=0, second=0, microsecond=0) - timedelta(hours=timestamp.hour % hours)
#         else:
#             raise ValueError("Unsupported timeframe")

#     def plot_ohlc(self, frame):
#         self.ax.clear()
#         candlestick_ohlc(self.ax, self.ohlc_data, width=0.6 / (24 * 60), colorup='g', colordown='r')
#         self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
#         self.ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))
#         self.ax.grid(True)
#         plt.xticks(rotation=45)
#         plt.xlabel('Date')
#         plt.ylabel('Price')
#         plt.title('OHLC Real-time Chart')
#         if self.current_price is not None:
#             self.current_price_line = self.ax.axhline(self.current_price, color='blue', linestyle='--', label='Current Price')
#         # Adiciona informações adicionais na legenda
#         atual = time.time()
#         tempo = atual - start
#         info_text = f'Current Price: {self.current_price}\nTotal Ticks: {self.tick_count}\nCurrent Time: {pd.Timestamp.now()}\nSpeed: {tempo}'
#         self.ax.text(1.02, 0.5, info_text, fontsize=10, transform=self.ax.transAxes, verticalalignment='center')

#         if self.current_price is not None:
#             self.current_price_line = self.ax.axhline(self.current_price, color='blue', linestyle='--', label='Current Price')

#         self.ax.legend(loc='upper left')







# # -*- coding: utf-8 -*-
# # import matplotlib
# # matplotlib.use('TkAgg')  # Ou use 'Qt5Agg' se preferir

# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from mplfinance.original_flavor import candlestick_ohlc
# import pandas as pd
# from datetime import timedelta
# from matplotlib.animation import FuncAnimation
# from utils.pin_bar import is_pin_bar
# import time
# # from observer import Obser
# start = time.time()

# class RealTimeOHLCPlotter:
#     def __init__(self, timeframe='1min'):
#         self.timeframe = timeframe
#         self.fig, self.ax = plt.subplots()
#         self.ohlc_data = []
#         self.current_price_line = None
#         self.current_price = None
#         self.tick_count = 0
#         self.animation = FuncAnimation(self.fig, self.plot_ohlc, interval=1, save_count=100)
        
#     def update(self, tick):
#         # print(f"3-RealTimeOHLCPlotter - Novo tick recebido: {tick}")
#         # self.add_tick(tick)
#         pass

#     def add_tick(self, tick):
#         self.tick_count += 1
#         timestamp = tick["time"].to_pydatetime()
#         price = tick["last"]

#         # Arredonda o timestamp para o timeframe especificado
#         rounded_timestamp = self.round_timestamp_to_timeframe(timestamp, self.timeframe)

#         # Atualiza os dados OHLC
#         if len(self.ohlc_data) == 0 or self.ohlc_data[-1][0] != mdates.date2num(rounded_timestamp):
#             self.ohlc_data.append([mdates.date2num(rounded_timestamp), price, price, price, price])
#         else:
#             self.ohlc_data[-1][2] = max(self.ohlc_data[-1][2], price)  # High
#             self.ohlc_data[-1][3] = min(self.ohlc_data[-1][3], price)  # Low
#             self.ohlc_data[-1][4] = price  # Close

#         self.current_price = price

#     def round_timestamp_to_timeframe(self, timestamp, timeframe):
#         if timeframe.endswith('min'):
#             minutes = int(timeframe[:-3])
#             return timestamp.replace(second=0, microsecond=0) - timedelta(minutes=timestamp.minute % minutes)
#         elif timeframe.endswith('H'):
#             hours = int(timeframe[:-1])
#             return timestamp.replace(minute=0, second=0, microsecond=0) - timedelta(hours=timestamp.hour % hours)
#         else:
#             raise ValueError("Unsupported timeframe")
#     def plot_ohlc(self, frame):
#         # Limpa o eixo atual para atualizar o gráfico
#         self.ax.clear()
        
#         # Plota os candles no gráfico
#         candlestick_ohlc(self.ax, self.ohlc_data, width=0.6 / (24 * 60), colorup='g', colordown='r')
        
#         # Configura o eixo X
#         self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
#         self.ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))
        
#         # Configura o eixo Y
#         self.ax.grid(True)
#         plt.xticks(rotation=45)
#         plt.xlabel('Date')
#         plt.ylabel('Price')
#         plt.title('OHLC Real-time Chart')
        
#         # Adiciona linha de preço atual, se disponível
#         if self.current_price is not None:
#             self.current_price_line = self.ax.axhline(self.current_price, color='blue', linestyle='--', label='Current Price')
        
#         # Configura a legenda
#         self.ax.legend(loc='upper left')
        
#         # Adiciona informações adicionais na legenda
#         atual = time.time()
#         tempo = atual - start
#         info_text = f'Current Price: {self.current_price}\nTotal Ticks: {self.tick_count}\nCurrent Time: {pd.Timestamp.now()}\nSpeed: {tempo}'
#         self.ax.text(1.02, 0.5, info_text, fontsize=10, transform=self.ax.transAxes, verticalalignment='center')
        
#         # Verifica se há dados OHLC e adiciona o tipo de pin bar, se aplicável
#         if len(self.ohlc_data) > 0:
#             last_ohlc = pd.Series(self.ohlc_data[-1], index=['Date', 'Open', 'High', 'Low', 'Close'])
#             pin_bar_type = is_pin_bar(last_ohlc)
            
#             if pin_bar_type:
#                 x = last_ohlc['Date']
#                 y = last_ohlc['High'] if pin_bar_type == 'venda' else last_ohlc['Low']
#                 self.ax.text(x, y, pin_bar_type, fontsize=10, horizontalalignment='center', verticalalignment='bottom')
        
#         # Atualiza o gráfico
#         plt.pause(0.01)


#     # def plot_ohlc(self, frame):
#     #     self.ax.clear()
#     #     candlestick_ohlc(self.ax, self.ohlc_data, width=0.6 / (24 * 60), colorup='g', colordown='r')
#     #     self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
#     #     self.ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=30))
#     #     self.ax.grid(True)
#     #     plt.xticks(rotation=45)
#     #     plt.xlabel('Date')
#     #     plt.ylabel('Price')
#     #     plt.title('OHLC Real-time Chart')

#     #     if self.current_price is not None:
#     #         self.current_price_line = self.ax.axhline(self.current_price, color='blue', linestyle='--', label='Current Price')

#     #     self.ax.legend(loc='upper left')
#     #     atual = time.time()
#     #     tempo = atual - start
#     #     # Adicionando informações adicionais na legenda
#     #     info_text = f'Current Price: {self.current_price}\nTotal Ticks: {self.tick_count}\nCurrent Time: {pd.Timestamp.now()}\n speed: {tempo}'
#     #     self.ax.text(1.02, 0.5, info_text, fontsize=10, transform=self.ax.transAxes, verticalalignment='center')
#     #     if len(self.ohlc_data) > 0:
#     #         last_ohlc = pd.Series(self.ohlc_data[-1], index=['Date', 'Open', 'High', 'Low', 'Close'])
#     #         pin_bar_type = is_pin_bar(last_ohlc)

#     #         if pin_bar_type:
#     #             x = last_ohlc['Date']
#     #             y = last_ohlc['High'] if pin_bar_type == 'venda' else last_ohlc['Low']
#     #             self.ax.text(x, y, pin_bar_type, fontsize=10, horizontalalignment='center', verticalalignment='bottom')


# # Exemplo de uso
# # plotter = RealTimeOHLCPlotter(timeframe='1min')
# # simulator.add_event_handler(plotter.add_tick)
# # simulator.run_simulation("EURUSD", 1, 3, 4, 2023)
# # plt.show()
