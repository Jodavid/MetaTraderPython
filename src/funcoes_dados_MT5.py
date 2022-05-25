import pandas as pd
import numpy as np
import datetime
from datetime import datetime
from datetime import date
import MetaTrader5 as mt5
import time

from funcoes_compra_e_venda import compra_limitada, venda_limitada

def conexao_MT5() :

    '''
    Esta função:
        - Função que realiza a conexão com o MT5.
    Dados de entrada:
        - Não há.
    Dados de saída:
        - Retorno da conexão com o MT5.
    '''
    # Conectando ao MetaTrader 5
    # Utilizando os logins atuais do Software
    if not mt5.initialize():
        print("initialize() falhou")
        mt5.shutdown()
    return('Conectado com sucesso ao MT5')

def dados_do_ativo(simbolo: str, tempo_candle =  mt5.TIMEFRAME_H1) -> pd.DataFrame:

    '''
     Esta função:
        - Função que retorna 1000 dados mais recentes dado o tempo do timeframe.
    Dados de entrada:
        - simbolo: Ativo ou Ação que será analisada para decisao de Compra ou Venda e enviada a Ordem para MT5.
        - tempo_candle: Tempo do candle que será analisado.
    Dados de saída:
        - Retorno da conexão com o MT5.
    '''

    ValoresAtivo = mt5.copy_rates_from_pos(simbolo, tempo_candle, 0, 1000)
    
    ValoresAtivo_PD = pd.DataFrame(ValoresAtivo) 
    ValoresAtivo_PD['time'] = pd.to_datetime(ValoresAtivo_PD['time'], unit='s')

    return ValoresAtivo_PD

def ultimo_preco(simbolo: str) -> float:

    '''
     Esta função:
        - Função que retorna o último preco do fechamento.
    Dados de entrada:
        - simbolo: Ativo ou Ação que será analisada para decisao de Compra ou Venda e enviada a Ordem para MT5.
    Dados de saída:
        - Último preço executado.
    '''

    price = mt5.symbol_info_tick(simbolo).ask

    return price

def envio_ordem(simbolo: str, lote: float, price: float, decisao: str) -> str:

    '''
     Esta função:
        - Função que envia ordem, retorna a ordem enviada.
    Dados de entrada:
        - simbolo: Ativo ou Ação que será analisada para decisao de Compra ou Venda e enviada a Ordem para MT5.
        - lote: Quantidade de papeis ou lote que deve ser comprado ou vendido, se a ordem for enviada.
        - price: Preço que será enviado para a ordem.
        - decisao: Decisão que será tomada, se a ordem for enviada.
    Dados de saída:
        - String informando a ordem executada.
    '''

    if decisao == "COMPRAR":
        StopLoss = price - 0.02
        TakeProfit = price + 0.05
        retorno = compra_limitada(simbolo, lote, price, StopLoss, TakeProfit)
    elif decisao == "VENDER":
        StopLoss = price + 0.02
        TakeProfit = price - 0.05
        retorno = venda_limitada(simbolo, lote, price, StopLoss, TakeProfit)
    else:
        retorno = 'Aguardando o sinal do Mercado'
    
    return retorno

def tempo_timeframe(tempo_candle: str) -> int:

    '''
     Esta função:
        - Função que retorna o tempo do timeframe.
    Dados de entrada:
        - tempo_candle: Tempo do candle que será analisado.
    Dados de saída:
        - String com o tempo do timeframe.
    '''

    if tempo_candle == 'M1':
        tempo = mt5.TIMEFRAME_M1
    elif tempo_candle == 'M5':
        tempo = mt5.TIMEFRAME_M5
    elif tempo_candle == 'M15':
        tempo = mt5.TIMEFRAME_M15
    elif tempo_candle == 'M30':
        tempo = mt5.TIMEFRAME_M30
    elif tempo_candle == 'H1':
        tempo = mt5.TIMEFRAME_H1
    elif tempo_candle == 'H4':
        tempo = mt5.TIMEFRAME_H4
    elif tempo_candle == 'D1':
        tempo = mt5.TIMEFRAME_D1
    elif tempo_candle == 'W1':
        tempo = mt5.TIMEFRAME_W1
    elif tempo_candle == 'MN1':
        tempo = mt5.TIMEFRAME_MN1

    return tempo