# -*- coding: utf-8 -*-
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
        if upper_tail_ratio >= min_tail_ratio:
            return 'bearish'
        if lower_tail_ratio >= min_tail_ratio:
            return 'bullish'

    return False
