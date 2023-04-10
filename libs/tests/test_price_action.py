# -*- coding: utf-8 -*-
from libs.utils.pin_bar import is_pin_bar
import pandas as pd
import timeit

class Test():
    
    def __init__(self, name='teste'):
        self.name = name
        self.df = pd.DataFrame({
            'Open': [1.0, 1.1, 1.2, 1.15, 1.25],
            'High': [1.2, 1.3, 1.4, 1.35, 1.45],
            'Low': [0.9, 1.0, 1.1, 0.95, 1.05],
            'Close': [1.1, 1.2, 1.1, 1.25, 1.15]
        })
        
    def __call__(self):
        self.test_is_pin_bar()
        
    def assertEqual(self, x , y):
        if x == y:
            print(f"As variáveis são iguais.Resposta: {x}")
        else:
            print(f"As variáveis são diferentes: {x} != {y}")
        return x == y
        
    def measure_performance(func, *args, **kwargs):
        def wrapped_func():
            return func(*args, **kwargs)

        num_repeats = 1000
        total_time = timeit.timeit(wrapped_func, number=num_repeats)
        average_time = total_time / num_repeats
    
        return average_time
        
    def test_is_pin_bar(self):
        self.assertEqual(is_pin_bar(self.df.iloc[0]), False)
        self.assertEqual(is_pin_bar(self.df.iloc[1]), False)
        self.assertEqual(is_pin_bar(self.df.iloc[2]), 'bearish')
        self.assertEqual(is_pin_bar(self.df.iloc[3]), False)
        self.assertEqual(is_pin_bar(self.df.iloc[4]), False)
        
    

# objeto = Test()
# objeto.test_is_pin_bar()
# considerando a execução do arquivo "test_price_action.py", como resolver o erro?

# from ..utils.pin_bar import is_pin_bar

# ImportError: attempted relative import with no known parent package

# projeto/
# │
# ├── main.py
# │
# └── utils/
# |    ├── __init__.py
# |    └── pin_bar.py
# │
# └── test/
#     ├── __init__.py
#     └── test_price_action.py