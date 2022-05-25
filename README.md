# MetaTrader e Python <img src="[Logo python](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Python_logo_and_wordmark.svg/1200px-Python_logo_and_wordmark.svg.png)" align="right" height="139"/>

## Visão geral

Nestes repositório encontra-se estudo com MetaTrader 5 e Python, para criação de EA (Expert Advisors);

## Links Úteis:

* MetaTrader 5: https://www.metatrader5.com/pt/download
* Biblioteca MetaTrader 5 para python: https://pypi.org/project/MetaTrader5/
* Documentação da Biblioteca: https://www.mql5.com/pt/docs/integration/python_metatrader5
* Documentação da Bibliote TA-Lib (indicadores de ativos): https://pypi.org/project/TA-Lib/

Apesar de conseguir instalar o MetaTrader no *Linux*, a biblioteca só é válida para *Windows*.

Dessa forma, o que é executado nesse repositório, é utilizando o SO *Windows*.

## Instalação do MetaTrader 5

Faça a instalação do MetaTrader 5, como um software comum.

## Instalação da biblioteca

No terminal execute:

``` python
# Instalação da biblioteca do MetaTrader
pip install MetaTrader5
```

Se tudo ocorreu como esperado,
estamos apto a criar os códigos,
e foi utilizado como editor o Visual Studio Code (https://code.visualstudio.com/download).


## Arquivo para execução 

### Codigo de Envio de Ordem através dos indicadores

scr/main.py: A função run() definida no arquivo main.py é responsável pela execução do Bot. Ela depende das variáveis Ativo (str), lote (float); 

``` python
# Exemplo de uso (conta brasileira): 
	- Execute o script:
  	python src/main.py PETR3F 1
```

``` python
# Exemplo de uso (conta Simulacao MetaTrader): 
	- Execute o script:
  	python src/main.py USDSEK 0.01
```

## Alterações do TimeFrame

O timeframe pode ser alterado no arquivo `config_dev.yaml`.

As opções para o timeframe são:

*  'M1'     : mt5.TIMEFRAME_M1
*  'M5'     : mt5.TIMEFRAME_M5
*  'M15'    : mt5.TIMEFRAME_M15
*  'M30'    : mt5.TIMEFRAME_M30
*  'H1'     : mt5.TIMEFRAME_H1
*  'H4'     : mt5.TIMEFRAME_H4
*  'D1'     : mt5.TIMEFRAME_D1
*  'W1'     : mt5.TIMEFRAME_W1
*  'MN1'    : mt5.TIMEFRAME_MN1