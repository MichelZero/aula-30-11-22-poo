#
class Professor:
  def __init__(self, nome) -> None:
    self.__nome = nome
    self.__ferramenta = None
  
  #gets
  @property
  def nome(self):
    return self.__nome
  
  @property
  def ferramenta(self):
    return self.__ferramenta
  
  #setters
  @ferramenta.setter
  def ferramenta(self, valor):
    self.__ferramenta = valor