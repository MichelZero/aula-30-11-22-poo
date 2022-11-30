#
#
# associação
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

a1 = A("soma = ", 2, 4)
#print(type(a1))
b1 = B(6, 8)
#print(a1)
#print(b1)
print(a1.a, b1.somaTodos(a1.b, a1.c))