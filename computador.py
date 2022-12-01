###
# autores:
#
# data: 30/11/2022

# criar a classe Computador com o editor de texto.

class Computador:
  def __init__(self, editor) -> None:
    self.__editor = editor
    
  #get
  @property 
  def editor(self): # get editor
    return self.__editor # retorna o editor de texto
  
  def escrever(self): # método escrever 
    print("Editor está escrevendo...") # escrevendo no editor de texto