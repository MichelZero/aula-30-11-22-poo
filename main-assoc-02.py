##
# autores:
#
# data: 30/11/2022
#
# associação

# importar as classes, professor, Caneta e Computador 
from caneta import Caneta as Ct
from computador import Computador as CP
from professor import Professor as P

# instanciar as classes professor, caneta e computador 
ct1 = Ct("Bic") # instanciando a classe Caneta e passando o parâmetro marca
cp1 = CP("Word") # instanciando a classe Computador e passando o parâmetro editor
p1 = P("Davi") # instanciando a classe Professor e passando o parâmetro nome

p1.ferramenta = ct1 # atribuindo o objeto ct1 da classe Caneta ao atributo ferramenta da classe Professor
# p1.ferramenta.escrever() # escrevendo com caneta... inicialmente o método escrever() da 
# classe Caneta é chamado e retornava um print, foi trocado para return.
#
print(ct1.marca) # Bic

print(f"O professor {p1.nome} está {p1.ferramenta.escrever()} da marca {ct1.marca} ") # O professor Davi está escrevendo com caneta... da marca Bic

print(f"deletando o objeto {p1.nome}") # deletando o objeto Davi 
del p1 # deletando o objeto p1 da classe Professor
print(f"ainda existe o objeto {ct1.marca}") # ainda existe o objeto Bic 

print("finalizando o programa...") # finalizando o programa...