##
# autores:
#
# data: 30/11/2022
#
# associação
# importar as classes
from caneta import Caneta as Ct
from computador import Computador as CP
from professor import Professor as P

ct1 = Ct("Bic")
cp1 = CP("Word")
p1 = P("Davi")

p1.ferramenta = ct1
# p1.ferramenta.escrever()
print(ct1.marca)

print(f"O professor {p1.nome} está {p1.ferramenta.escrever()} da marca {ct1.marca} ")

print(f"deletando o objeto {p1.nome}")
del p1
print(f"ainda existe o objeto {ct1.marca}")