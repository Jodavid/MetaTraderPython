# Biblioteca para indicadores tecnicos
from talib import RSI, EMA, BBANDS
import numpy as np

def decisao_RSI(close: np.array, Periodo: int = 14):

    '''
    Esta função:
        - Função que realiza calculo do RSI e retorna decisao de compra, venda ou nada.
    Dados de entrada:
        - close: Precos de fechamento dos candles.
        - Periodo: Periodo do RSI.
    Dados de saída:
        - Retorno da decisao o RSI.
    '''
    rsi_ind = RSI(close, timeperiod = Periodo)
    array_length = len(rsi_ind)
    last_element = rsi_ind[- 1]
    last_rsi = last_element


    if last_rsi > 70:
        decisao = 'VENDER'
    elif last_rsi < 30:
        decisao = 'COMPRAR'
    else:
        decisao = 'NADA'
    
    return decisao