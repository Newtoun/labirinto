from Estado import Estado
from Gabarito import Gabarito
from LabirintoAutomatico import labirintoAutomatico


matriz = labirintoAutomatico(11,9)
inicio = matriz.ponto_Inicial
fim = matriz.ponto_Final
print("ini: {} fim: {}".format(inicio,fim))
matriz.imprime_Matriz() 



estadoInicial = Estado(matriz.matriz, inicio, fim, 0, [])
resposta = Gabarito.busca_Informada(estadoInicial)



if resposta == 0:
    print("Labirinto não tem solução")
else: 
    print(resposta)