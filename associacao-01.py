###
# autores:
# michel silva

# data: 30/11/2022
#
# associação
# criando duas classes A e B, ao instanciar a classe B,
# passamos um objeto da classe A como parâmetro.
# na classe B, criar um método somaTodos que recebe dois
# parâmetros.

# classe A
class A: 
  def __init__(self, a, b, c) -> None:
    self.a = a
    self.b = b
    self.c = c
    

# classe B
class B:
  def __init__(self, d, e) -> None:
    self.d = d
    self.e = e
    
  def somaTodos(self, valorAb, valorAc):
    valorR = self.d + self.e + valorAb + valorAc
    return valorR
  
  
####### main.py  ##############
# criando a associação entre as classes A e B

a1 = A("soma = ", 2, 4) # instanciando a classe A e passando os parâmetros a, b e c
#print(type(a1)) # <class '__main__.A'>
b1 = B(6, 8) # instanciando a classe B e passando os parâmetros d e e
#print(a1) # <__main__.A object at 0x7f9b1c0b4d90>
#print(b1) # <__main__.B object at 0x7f9b1c0b4d30>
print(a1.a, b1.somaTodos(a1.b, a1.c)) # soma =  20
# vamos deletar o objeto a1
print("deletando o objeto a1")
del a1
#print(a1) # NameError: name 'a1' is not defined
print(b1.somaTodos(2, 4)) # 20 # o objeto a1 foi deletado, mas o objeto b1 ainda existe
# porque o objeto b1 não depende do objeto a1 para existir.