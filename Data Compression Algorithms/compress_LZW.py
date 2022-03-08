class CompressionLZW:
  def __init__(self,uncompressed:str,dict_size=256) -> None:
      self.__uncompressed = uncompressed
      self.__dict_size = dict_size
      self.__dictionary = self.generate_dictionary()
      
      
  def generate_dictionary(self) -> list:
    """
    Crée un dictionnaire D (tableau de chaines) de taille 256+n. n étant la longueur de la
    chaine en entrée. Le code de chaque caractère est son indice dans le tableau D. le
    dictionnaire est initialisé avec les caractères de la table ascii de 0 à 255 et initialisé à une
    chaine vide au-delà du 256ème caractère.
    """
    return [chr(i) if i <= 256 else "" for i in range(0,self.__dict_size)]
  
  
  def get_dictionary(self) -> list:
    return self.__dictionary
  
  def index_in_dictionary(self,researched_string : str) -> int:
    """ 
    Une fonction qui prend en entrée une chaine de caractère et le dictionnaire D. 
    La fonction retourne l’indice de la chaine dans le dictionnaire.
    """
    return self.__dictionary.index(researched_string)
  def update_dictionary(self,input_string:str) -> None:
    """
    Une fonction qui prend en entrée une chaine de caractère et le dictionnaire D. La
    fonction insère la chaine dans le dictionnaire.
    """
    if input_string not in self.__dictionary:
      self.__dictionary.append(input_string)
  
  def compress_string(self) -> list:
    """
    La fonction prend en entrée une chaine de caractères, applique la compression LZW et
    retourne la chaine codée.
    """
    w = ""
    result = []
    for c in self.__uncompressed:
      print('w = {},c = {}'.format(w,c))
      if w + c in self.__dictionary:
        w = w + c
      else:
        result.append(self.index_in_dictionary(w))
        self.update_dictionary(w+c)
        w = c
        
    if w: #we do this because there is a remaining char to add 
      result.append(self.index_in_dictionary(w))
    print('{} -> {}'.format(self.__uncompressed,' '.join([str(element) for element in result])))
    return ' '.join([str(element) for element in result])
    
      

      
if __name__ == "__main__":
  user_string = input('Veuillez introduire une chaîne de caractères : ')
  compression = CompressionLZW(user_string).compress_string()
