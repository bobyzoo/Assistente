from importacoes import *
import codecs
banco = bancoDAO('Assistente')

# banco.maisProxima('Meu nome é Rob')


# arq = codecs.open('texto.txt','r',encoding='utf-8')
# for l in arq:
#     print(l)
#
#     banco.insertFrase(l)
#

# arq = codecs.open('texto.txt','r',encoding='utf-8')
# for l in arq:
#     banco.modoTrain(l)
#     print(30*'*')

banco.procuraResposta('qual é seu nome')