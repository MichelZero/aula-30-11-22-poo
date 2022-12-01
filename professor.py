###
# autores:
#
# data: 30/11/2022

# criar uma classe Professor com os atributos nome e ferramenta.
# ferramenta é um objeto da classe Caneta ou Computador.
# a classe professor de iniciar com o atributo ferramenta como None e 
# nome vinculado ao parâmetro nome.

class Professor:
  def __init__(self, nome) -> None:
    self.__nome = nome
    self.__ferramenta = None # atributo ferramenta como None
  
  #gets
  @property
  def nome(self): # get nome 
    return self.__nome # retorna o nome do professor 
  
  @property
  def ferramenta(self): # get ferramenta
    return self.__ferramenta # retorna o objeto da classe Caneta ou Computador 
  
  #setters
  @ferramenta.setter # set ferramenta 
  def ferramenta(self, valor): # recebe um objeto da classe Caneta ou Computador
    self.__ferramenta = valor # atribui o objeto da classe Caneta ou Computador ao atributo ferramenta