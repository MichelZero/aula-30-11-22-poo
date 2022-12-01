###
# autores:
#
# data: 30/11/2022

class Computador:
  def __init__(self, editor) -> None:
    self.__editor = editor
    
  #get
  @property
  def editor(self):
    return self.__editor
  
  def escrever(self):
    print("Editor está escrevendo...")