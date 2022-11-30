#
class Caneta:
  def __init__(self, marca) -> None:
    self.__marca = marca
    
  #get
  @property
  def marca(self):
    return self.__marca
  
  def escrever(self):
    return "escrevendo com caneta..."