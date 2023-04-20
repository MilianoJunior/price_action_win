# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

conceito_pin_bar = '''
Barras de pin (Pin Bars): São velas com mechas longas e corpos pequenos, indicando rejeição de preços mais altos ou mais baixos. Uma barra de pin pode sinalizar uma reversão de tendência ou uma continuação, dependendo da direção da mecha e do contexto do mercado.
'''
def is_pin_bar(row, min_tail_ratio=0.66, min_body_ratio=0.33):
    """
    Identifica se a vela fornecida é uma barra de pin (Pin Bar) de alta ou de baixa.

    Parâmetros:
    row (pd.Series): Uma linha de dados de preço OHLC (Open, High, Low, Close).
    min_tail_ratio (float, opcional): A proporção mínima entre a mecha e o alcance total da vela para ser considerada uma barra de pin. Padrão é 0.66.
    min_body_ratio (float, opcional): A proporção máxima entre o corpo e o alcance total da vela para ser considerada uma barra de pin. Padrão é 0.33.

    Retorna:
    str: 'bullish' se a vela é uma barra de pin de alta, 'bearish' se a vela é uma barra de pin de baixa, ou False se a vela não é uma barra de pin.
    """
    candle_range = row['High'] - row['Low']
    body_range = abs(row['Open'] - row['Close'])
    upper_tail = row['High'] - max(row['Open'], row['Close'])
    lower_tail = min(row['Open'], row['Close']) - row['Low']

    if candle_range == 0:
        return False

    body_ratio = body_range / candle_range
    upper_tail_ratio = upper_tail / candle_range
    lower_tail_ratio = lower_tail / candle_range

    if body_ratio <= min_body_ratio:
        print('tamanho body_ratio', upper_tail_ratio, lower_tail_ratio  )
        if upper_tail_ratio >= min_tail_ratio:
            return 'venda'
        if lower_tail_ratio >= min_tail_ratio:
            return 'compra'

    return False

# def plot_pin_bars(df, pin_bars_bullish, pin_bars_bearish):
#     fig, ax = plt.subplots(figsize=(10, 5))

#     # Convertendo as datas para o formato numérico usado pelo matplotlib
#     df['DateNumeric'] = mdates.date2num(df['Date'])

#     # Plotando os candles
#     candlestick_ohlc(ax, df[['DateNumeric', 'Open', 'High', 'Low', 'Close']].values, width=0.6, colorup='green', colordown='red', alpha=0.8)

#     # Plotando os Pin Bars de alta e baixa
#     ax.scatter(pin_bars_bullish['DateNumeric'], pin_bars_bullish['Low'], color='red', marker='o', label='Pin Bars - Bullish')
#     ax.scatter(pin_bars_bearish['DateNumeric'], pin_bars_bearish['High'], color='blue', marker='o', label='Pin Bars - Bearish')

#     ax.set_title('Price Action - Pin Bars')
#     ax.set_xlabel('Date')
#     ax.set_ylabel('Price')
#     ax.legend()

#     # Formatando as datas no eixo x
#     ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#     ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

#     plt.xticks(rotation=45)
#     plt.show()
    
# # Exemplo de dados de preços em OHLC (open, high, low, close)
# data = [
#     ['2023-01-01', 100, 105, 95, 98],
#     ['2023-01-02', 98, 103, 92, 97],
#     ['2023-01-03', 97, 106, 96, 105],
#     ['2023-01-04', 105, 110, 100, 108],
#     ['2023-01-05', 108, 112, 99, 100],
#     ['2023-01-05', 108, 135, 97, 100],
# ]

# # Criando um DataFrame do pandas a partir dos dados
# df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close'])
# df['Date'] = pd.to_datetime(df['Date'])

# df['PinBar'] = df.apply(is_pin_bar, axis=1)
# pin_bars_bullish = df[df['PinBar'] == 'bullish']
# pin_bars_bearish = df[df['PinBar'] == 'bearish']
# pin_bars_bullish['DateNumeric'] = mdates.date2num(pin_bars_bullish['Date'])
# pin_bars_bearish['DateNumeric'] = mdates.date2num(pin_bars_bearish['Date'])

# plot_pin_bars(df, pin_bars_bullish, pin_bars_bearish)