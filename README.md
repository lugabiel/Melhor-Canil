# Melhor Petshop 🐶🐶🐶🐶
Aplicação para encontrar a melhor dentre 3 petshops para os cães 🐶 do canil de seu Eduardo.
A petshop melhor é:
* a mais barata;
* e, em caso de empate de preço, a mais próxima do canil do seu Eduardo, dentre as mais baratas.

No universo de Eduardo, existem 3 petshops:
* Meu Canino Feliz: Está distante 2km do canil. Em dias de semana o banho para cães pequenos custa R$20,00 e o banho em cães grandes custa R$40,00. Durante os finais de semana o preço dos banhos é aumentado em 20%.
* Vai Rex: Está localizado na mesma avenida do canil, a 1,7km. O preço do banho para dias úteis em cães pequenos é R$15,00 e em cães grandes é R$50,00. Durante os finais de semana o preço para cães pequenos é R$ 20,00 e para os grandes é R$ 55,00.
* ChowChawgas: Fica a 800m do canil. O preço do banho é o mesmo em todos os dias da semana. Para cães pequenos custa R$30 e para cães grandes R$45,00.

Para desenvolver esta solução existem algumas premissas foram postas:
* É necessário uma estrutura de dados suficente para modelar o problema, neste caso, utilizou-se a classe Petshop. Onde cada instância da classe corresponde a uma das petshops descritos acima, cada uma com seus nomes, preços e espeficidades.
* Como o preço de algumas das petshops é dinâmico, isto é, varia de acordo com o dia da semana, foi necessário também criar uma função capaz de identificar se o dia em que seu Eduardo pretende levar os cães ao petshop é um dia útil ou final de semana. Sendo assim, criou-se a função isWeekday(), baseada no módulo **datetime** nativo da linguagem Python.
* Para avaliar de fato qual petshot é a melhor criou-se a função melhorpetshop() (***oh really?***), ela é capaz de avaliar o nome e o valor do orçamento da melhor petshop a partir da data do serviço, da quantidade de cães (pequenos e grandes) e das informações a respeito das instâncias das petshops. 
* Por fim, foi feito um simples 'parser' analisador de entradas para facilitar a vida de seu Eduardo, onde ele pode inserir o dia e a quantidade de cães que irá levar à petshop. Esta entrada de dados deve ser seguir o formato - <data> <quantidade de cães pequenos> <quantidade cães grandes>.
 
# Como executar o programa? 💻
Este programa foi todo feito utilizando a linguagem Python (v. 3.8). Sendo assim, para executá-lo basta abrir o programa petshopFinder.py, em uma máquina com Python 3 instalado, e seguir as instruções que irão aparecer no terminal. 
Até o momento não existe uma intereface gráfica para esta aplicação e, portanto, ela somente pode ser executada no console (PYTHON IDLE, BASH, POWERSHELL, ETC).
 
 
 
