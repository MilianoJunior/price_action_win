import pandas as pd
from datetime import datetime
import numpy as np
import MetaTrader5 as mt5
import pytz
from tabulate import tabulate
import inspect
import time
import random
import threading
import calendar

class MinhaThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        # código a ser executado na thread
        interval_ms = 100
        i = 0
        segundos = 0
        login = '1603115'
        password = '2718lej@JR'
        symbol = 'WINM23'
        conexao = Dados(login, password)
        # conexao.get_profit()
        conexao.get_symbol_info(symbol)
        # conexao.get_terminal_info()
        start_day, end_day, month, year = 14,18,3,2023
        # dias = conexao.get_days_in_month(month, year)
        for dia in range(start_day, end_day):
            print('                                ')
            print('Dia: ',dia)
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            ticks = conexao.get_ticks(symbol, dia, dia + 1, month, year)
            for name in ticks.columns:
                print(name, ticks[name][0])
                print(name, ticks[name].values[-1])
                print('------------------------')
            

class Dados():
    def __init__(self, user: str, password: str):
        self.conectar(user, password)

    def conectar(self, user, password):
        try:
            if not mt5.initialize():
                print("Falha ao conectar ao MetaTrader 5")
                mt5.shutdown()
                return False
            # establish connection to the MetaTrader 5 terminal
            account_info=mt5.account_info()
            if account_info is None:
                print("initialize() failed, error code =",mt5.last_error())
                quit()
                authorized = mt5.login(user, password)
                if not authorized:
                    print("Falha ao autorizar a conexão com a conta", user)
                    return False
    
            return True
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
        
    def get_days_in_month(self, month, year):
        days_in_month = []
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            days_in_month.append(day)
        return days_in_month
    
    def get_ticks(self,symbol: str, start_day: int,end_day ,month: int,year: int):
        # tratamento de exeção para dias não operaveis
        try:
            timezone = pytz.timezone("America/Sao_Paulo")
            # criamos o objeto datatime no fuso horário UTC para que não seja aplicado o deslocamento do fuso horário
            utc_from = datetime(year, month, start_day, tzinfo=timezone)
            utc_to = datetime(year, month, end_day, tzinfo=timezone)
            print(utc_from)
            print(utc_to)
            # solicitamos ticks de um intervalo
            ticks_ = mt5.copy_ticks_range(symbol, utc_from, utc_to, mt5.COPY_TICKS_ALL)
            print('Ticks: ',len(ticks_))
            # Convertemos para pandas dataframe
            ticks_ = pd.DataFrame(ticks_)
            # transformar timestamp em segundos
            ticks_['time']=pd.to_datetime(ticks_['time'],unit='s')
            # ticks_.set_index('time',inplace=True)
            return ticks_
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
        
    def get_profit(self):
        try:
            print('------------------------------')
            print('Informações da Conta')
            print('------------------------------')
            account_info = mt5.account_info()._asdict()
            my_list = list(account_info.items())
            print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
            return account_info
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
    def get_terminal_info(self):
        try:
            terminal_info=mt5.terminal_info()
            if terminal_info!=None:
                # exibimos os dados sobre o terminal tal qual como estão
                print(terminal_info)
                # exibimos os dados como uma lista
                print("Show terminal_info()._asdict():")
                terminal_info_dict = mt5.terminal_info()._asdict()
                my_list = list(terminal_info_dict.items())
                print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO

    def get_symbol_info(self, symbol):
        try:
            print('------------------------------')
            print('Informaçãoes do Simbolo')
            print('------------------------------')
            symbol_info = mt5.symbol_info(symbol)
            symbol_info = symbol_info._asdict()
            my_list = list(symbol_info.items())
            print(tabulate(my_list, headers=['nome','valor'], tablefmt="grid"))
            return symbol_info
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
        
    def get_symbol_book(self, symbol):
        try:
            print('------------------------------')
            print('Profudindade do Mercado')
            print('------------------------------')
            # subscreva para receber atualizações no livro de ofertas para o símbolo EURUSD (Depth of Market)
            if mt5.market_book_add(symbol):
              # obtemos 10 vezes em um loop os dados do livro de ofertas
               for i in range(10):
                    # obtemos o conteúdo do livro de ofertas (Depth of Market)
                    items = mt5.market_book_get(symbol)
                    # exibimos todo o livro de ofertas como uma string tal qual como está
                    print(items)
                    # agora exibimos cada solicitação separadamente para maior clareza
                    if items:
                        for it in items:
                            # conteúdo da solicitação
                            print(it._asdict())
                    # vamos fazer uma pausa de 5 segundos antes da próxima solicitação de dados do livro de ofertas
              # cancelamos a subscrição de atualizações no livro de ofertas (Depth of Market)
               mt5.market_book_release(symbol)
               return True
            else:
                ERRO = f"Error: {inspect.currentframe().f_code.co_name},\n {mt5.last_error()}"
                print(ERRO)
                return ERRO
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
    
    def get_symbols(self, search:str=''):
        try:
            print('------------------------------')
            simbolos = mt5.symbols_get()
            for index in range(mt5.symbols_total()):
                ticket = simbolos[index].name
                if (search in ticket):
                    print(index, ticket)
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
    
    def convert_time(self):
        try:
            date_time = pd.to_datetime(self.base1.pop('date'), format='%Y.%m.%d %H:%M:%S')
            timestamp_s = date_time.map(datetime.datetime.timestamp)
            day = 24*60*60
            self.base1['date'] = date_time
            self.base1['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
            self.base1['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
        
    def select_symbol(self, symbol):
        try:
            selected=mt5.symbol_select(symbol,True)
            if not selected:
                print("Failed to select EURCAD, error code =",mt5.last_error())
            self.get_symbol_info(symbol)

        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO

    def comprar(self, symbol, volume):
        try:
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_BUY,
                "price": mt5.symbol_info_tick(symbol).ask,
                "deviation": 20,
                "magic": 123456,
                "comment": "Minha ordem de compra",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC
            }
    
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("Erro ao comprar", symbol, ":", result.comment)
            else:
                print("Compra de", volume, "de", symbol, "realizada com sucesso")
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO

    def vender(self, symbol, volume):
        try:
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_SELL,
                "price": mt5.symbol_info_tick(symbol).bid,
                "deviation": 20,
                "magic": 123456,
                "comment": "Minha ordem de venda",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC
            }
    
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("Erro ao vender", symbol, ":", result.comment)
            else:
                print("Venda de", volume, "de", symbol, "realizada com sucesso")
        except Exception as e:
            ERRO = f"Error: {inspect.currentframe().f_code.co_name}, {e},\n {mt5.last_error()}"
            print(ERRO)
            return ERRO
            
# testes

if __name__ == '__main__':
    
    # login = '1603115'
    # password = '2718lej@JR'
    # symbol = 'WINJ23'
    # start_day, end_day, month, year = 1,28,2,2023
    # conexao = Dados(login, password)
    # conexao.get_symbols(symbol)
    # conexao.get_profit()
    # conexao.get_symbol_info(symbol)
    # conexao.get_symbol_book(symbol)
    # ticks = conexao.get_ticks(symbol, start_day, end_day, month, year)
    thread = MinhaThread().run()
    
    
    
    
    
    
    
    
    # login = '1603115'
    # password = '2718lej@JR'