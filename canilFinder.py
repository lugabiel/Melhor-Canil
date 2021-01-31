from datetime import date
    
def isWeekday(epoca):
    day = epoca
    if day.weekday() < 6:
        return True
    else:
        return False

class canil:
    def __init__(self, nome=None, distancia=None, dinamico=None, preco=[None, None]):
        self.name     = nome
        self.distance = distancia # distancia em metros
        self.price    = preco     # price = [smallDoge, biiigDoge, FDSsmallDoge, FDSbigDoge]
        self.dynamic  = dinamico  # indica se o preco eh dinamico para FDS
        
    def canilInfo(self):
        print('Nome:  '+self.name)
        print('Distancia: ',self.distance)
        if self.dynamic == True:
            print('--Precos em dia util')
            print('Preco pequenos caes: ',self.price[0],'R$')
            print('Preco grandes caes:  ' ,self.price[1],'R$')
            print('--Precos no Final de Semana')
            print('Preco pequenos caes: ',self.price[2],'R$')
            print('Preco grandes caes:  ' ,self.price[3],'R$',f'\n')
        else:
            print('--Preco fixo todos os dias')
            print('Preco pequenos caes: ',self.price[0],'R$')
            print('Preco grandes caes:  ' ,self.price[1],'R$',f'\n')
    def orcamento(self,qntDogP,qntDogG,dUtil):
        if self.dynamic == True and dUtil == True:
            total = qntDogP*self.price[2] + qntDogG*self.price[3]
        else:
            total = qntDogP*self.price[0] + qntDogG*self.price[1]
        return total

canil_C = canil(nome='chowchagas',distancia=800,dinamico=False,preco = [30,45])
canil_B = canil(nome='vai rex'   ,distancia=1700,dinamico=True ,preco = [15,50,20,55])
canil_A = canil(nome='meu canino feliz',distancia=2000,dinamico=True,preco = [20,40,20*1.2,40*1.2])

def melhorCanil(diaDhoraH,dogP,dogG):
    diaUtil = isWeekday(diaDhoraH)
    orcamentos = []
    orcamentos.append([canil_A.orcamento(dogP,dogG,diaUtil),canil_A.distance,canil_A.name])
    orcamentos.append([canil_B.orcamento(dogP,dogG,diaUtil),canil_B.distance,canil_B.name])
    orcamentos.append([canil_C.orcamento(dogP,dogG,diaUtil),canil_C.distance,canil_C.name])
    nearestCanil  = 50000
    smallestPrice = 50000
    melhorCan = (None,None)
    while orcamentos:
        orc = orcamentos.pop()
        if orc[0] == smallestPrice:
            if orc[1] < nearestCanil:
                melhorCan, smallestPrice, nearestCanil = (orc[2],orc[0]), orc[0],orc[2]
        if orc[0] < smallestPrice:
            melhorCan, smallestPrice, nearestCanil = (orc[2],orc[0]), orc[0],orc[2]
    return melhorCan                  
print('Insira dados para obter o melhor orçamento: <data> <quantidade de cães pequenos> <quantidade cães grandes>')
print('Onde <data> tem o formato: dd/mm/aaaa')
print('Exemplo: 03/08/2018 3 5')
entrada = input(f'insira e pressione enter: \n')
data, pequenosDogos, grandesDogos = entrada.split(' ')
dia, mes, ano = data.split('/')
qntDogosP = int(pequenosDogos)
qntDogosG = int(grandesDogos)
diaInput = date(int(ano),int(mes),int(dia))
canilInfo = melhorCanil(diaInput,qntDogosP,qntDogosG)
print('Melhor canil: ', canilInfo[0],'- Valor total:  ', canilInfo[1], 'R$')