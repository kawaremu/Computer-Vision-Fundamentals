test_str = 'ABABABABABABABABABABABABABABABABABAB'
expected = '0XXY9X'  

def encode_rle(message: str):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1): 
  
            if (message[j] == message[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        if(count >= 3):
          encoded_string = encoded_string + str(count) + ch
        elif(count < 3 and count != 1):
          encoded_string = encoded_string + str(0) + ch*count        
        else:
          encoded_string = encoded_string + ch
        i = j + 1       
    return encoded_string
  
  
def compression_rate(raw: str,compressed: str) -> float:
  if len(compressed) > len(raw):
    print("La chaîne compressée est plus longue.")
  elif len(compressed) < len(raw):
    print("La chaîne compressée est plus courte.")
  else:
    print("Les chaînes sont identiques.")
  print('Taux de compression: ' + str(round((len(compressed)/len(raw))*100,2)) +"%")
  return round((len(compressed)/len(raw))*100,2)


raw = input('Veuillez entrer une chaîne de caractères : ')
compressed = encode_rle(raw)
print('Vous avez entré : {} -> Chaîne compressée : {}'.format(raw,compressed))
compression_rate(raw,compressed)