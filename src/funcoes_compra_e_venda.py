import MetaTrader5 as mt5

def compra_limitada(simbolo: str, lote: float, price: float, StopLoss: float, TakeProfit: float, Comentario: str = "Ordem do AutoBot")-> str:
    
    '''
    Esta função:
        - Função que realiza a compra de uma ação através de Ordem Limitada.
    Dados de entrada:
        - simbolo: string com o nome da ação.
        - lote: Quantidade de ações a ser comprada.
        - price: Preço de compra.
        - StopLoss: Preço de Stop Loss.
        - TakeProfit: Preço de Take Profit.
        - Comentario: Comentário da ordem.
    Dados de saída:
        - Retorno do envio da Ordem.
    '''

    request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": simbolo,
            "volume": lote,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": StopLoss,
            "tp": TakeProfit,
            "deviation": 20,
            "magic": 2022,
            "comment": Comentario,
            "type_time": mt5.ORDER_TIME_DAY,
            "type_filling": mt5.ORDER_FILLING_IOC
            }

    mt5.order_send(request)

    return('Uma ordem de Compra foi enviada')

def venda_limitada(simbolo: str, lote: float, price: float, StopLoss: float, TakeProfit: float, Comentario: str = "Ordem do AutoBot")-> str:
    
    '''
    Esta função:
        - Função que realiza a venda de uma ação através de Ordem Limitada.
    Dados de entrada:
        - simbolo: string com o nome da ação.
        - lote: Quantidade de ações a ser vendida.
        - price: Preço de venda.
        - StopLoss: Preço de Stop Loss.
        - TakeProfit: Preço de Take Profit.
        - Comentario: Comentário da ordem.
    Dados de saída:
        - Retorno do envio da Ordem.
    '''

    request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": simbolo,
            "volume": lote,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": StopLoss,
            "tp": TakeProfit,
            "deviation": 20,
            "magic": 2022,
            "comment": Comentario,
            "type_time": mt5.ORDER_TIME_DAY,
            "type_filling": mt5.ORDER_FILLING_IOC
            }

    mt5.order_send(request)

    return('Uma ordem de Venda foi enviada')