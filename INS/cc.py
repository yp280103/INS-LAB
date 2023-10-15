def cc(text,shift):
  result=""
  for i in range(len(text)):
    char = text[i]
    if(char.isupper()):
      result+=chr((ord(char)+shift-65) % 26 + 65)
    else:
       result+= chr((ord(char)+shift-97) % 26 + 97)
  return result
text = input("enter name::")
shift = 1
en=cc(text,shift)
print(en)
de=cc(en,-shift)
print(de)
