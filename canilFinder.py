from datetime import date
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
            
def isWeekday():
    dia = date(2021, 1, 31)
    if dia.weekday() < 6:
        return 1
    else:
        return 0

canil_C = canil(nome='chowchagas',distancia=800,dinamico=False,preco = [30,45])
canil_B = canil(nome='vai rex'   ,distancia=1700,dinamico=True ,preco = [15,50,20,55])
canil_A = canil(nome='meu canino feliz',distancia=2000,dinamico=True,preco = [20,40,20*1.2,40*1.2])
canisDisponiveis = [canil_A,canil_B,canil_C]
print('--------------------')
print('canis disponiveis:  ')
for can in canisDisponiveis:
    can.canilInfo()
print('--------------------')

entrada = input('insira uma data')
print(entrada)
print(isWeekday())


