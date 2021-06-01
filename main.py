'''Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor de x perteneciente a los reales, utilizando los primeros n terminos de la serie de Maclaurin'''

def aproxExp(x,n):
  e = 0
  for i in range(0,n+1):
    factorial=1
    for j in range(1,i+1):
      factorial = factorial*j  
    e += (x**i)/factorial
  return e

print(str(aproxExp(2,1000)))