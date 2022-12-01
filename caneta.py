###
# autores:
#
# data: 30/11/2022

# criar a classe Caneta com a marca. 

class Caneta:
  def __init__(self, marca) -> None:
    self.__marca = marca # atributo marca vinculado ao parâmetro marca
    
  #get
  @property
  def marca(self): # get marca
    return self.__marca # retorna a marca da caneta
  
  def escrever(self): # método escrever 
    return "escrevendo com caneta..." # escrevendo com a caneta 