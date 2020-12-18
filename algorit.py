import numpy as np
entrada = input("ingrese la palabra: ")
pali = np.array([entrada])
pali = np.append(pali, entrada)

def palindromo():
  if (pali[0]) == (pali[0])[::-1]:
    print("palindromo")
  else:
    print("no es palindromo")

palindromo()