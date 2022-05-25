# Lendo as bibliotecas necessarias
import pandas as pd
import numpy as np
import datetime
from datetime import datetime
from datetime import date
import MetaTrader5 as mt5
import time
# Funcoes para ordem de compra e venda
from funcoes_dos_indicadores import decisao_RSI
from funcoes_dados_MT5 import conexao_MT5, dados_do_ativo, ultimo_preco, tempo_timeframe, envio_ordem

from config import TIMEFRAME_TEMP

import argparse


def run(Ativo: str, lote: float) -> None:
    '''
    Esta funcao:
        -  Realiza a execucao da Analise e Envio da Ordem.
    
    Dados de Entrada:
                    - São repassadas como variáveis de argumento utilizando o argparse
    Dados de saida:
                    - Um resultado indicando que tipo de ação foi realizada.   
    '''
    print("Tempo do TimeFrame: "+ TIMEFRAME_TEMP, end="\n\n")
    tempo = tempo_timeframe(TIMEFRAME_TEMP)

    conexao_MT5()
    dados = dados_do_ativo(Ativo, tempo)
    print(dados.tail(2), end="\n\n")

    last_price = ultimo_preco(Ativo)
    print("Último preço: " + str(last_price), end="\n\n")

    close = np.array(dados['close'])
    decisao = decisao_RSI(close, Periodo = 14)
    print("Decisao: " + decisao, end="\n\n")

    resultado = envio_ordem(Ativo, lote, last_price, decisao)
    print("O que foi realizado: " + resultado, end="\n\n")



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("simbolo", help="Ativo ou Ação que será analisada para decisao de Compra ou Venda e enviada a Ordem para MT5.",
                        type=str, nargs='?', const=1, default = 'PETR3' )
    parser.add_argument("Volume", help="Quantidade de papeis ou lote que deve ser comprado ou vendido, se a ordem for enviada.",
                        type=float, nargs='?', const=1, default = 1 )
    
    
    args = parser.parse_args()
    
    run(Ativo = args.simbolo, lote = args.Volume)