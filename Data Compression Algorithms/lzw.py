
class CompressionLZW:
  def __init__(self,uncompressed:str,dict_size=256) -> None:
      self.__uncompressed = uncompressed
      self.__dict_size = dict_size
      self.__dictionary = self.generate_dictionary()
      
  def generate_dictionary(self) -> dict:
    """
    Crée un dictionnaire D (tableau de chaines) de taille 256+n. n étant la longueur de la
    chaine en entrée. Le code de chaque caractère est son indice dans le tableau D. le
    dictionnaire est initialisé avec les caractères de la table ascii de 0 à 255 et initialisé à une
    chaine vide au-delà du 256ème caractère.
    """
    return {chr(i):i if i <= 256 else "" for i in range(self.__dict_size)}
  
    
  def get_dictionary(self) -> dict:
    return self.__dictionary
  
  
  def compress_string(self) -> str:
    """
    La fonction prend en entrée une chaine de caractères, applique la compression LZW et
    retourne la chaine codée.
    """
    w = ""
    compressed = [] #This will contain a list of integers
    for c in self.__uncompressed:
      wc = w + c 
      if wc in self.__dictionary:
        w = wc
      else:
        compressed.append(self.__dictionary[w])
        self.__dictionary[wc] = self.__dict_size
        self.__dict_size += 1
        w = c
    
    if w:
      compressed.append(self.__dictionary[w])
    print('{} -> {}'.format(self.__uncompressed,' '.join([str(element) for element in compressed])))
    return compressed
      
      
  
if __name__ == "__main__":
  user_string = input('Veuillez introduire une chaîne de caractères : ')
  compression = CompressionLZW(user_string).compress_string()
  
