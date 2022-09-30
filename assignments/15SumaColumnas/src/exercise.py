def generaMatriz (renglon, columna):
  X=[]
  for r in range(renglon):
    X.append([])
    for c in range(columna):
      y=int(input(""))
      X[r].extend([y])	
  y=sumaColumnas(X)
  return y
  pass

def sumaColumnas (matriz):
  a=b=c=d=0
  Z=[]
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      n=matriz[i][j]
      if j==0:
        a=a+n
      elif j==1:
        b=b+n
      elif j==2:
        c=c+n
      elif j==3:
        d=d+n
      else:
        break
  for k in range(len(matriz[0])):
      if k==0:
        Z.append(a)
      elif k==1:
        Z.append(b)
      elif k==2:
        Z.append(c)
      elif k==3:
        Z.append(d)
      else:
        break
  return Z
  pass

def main():
  renglon=int(input(""))
  columna=int(input(""))
  if renglon<1 or columna<1:
    print("Error")
  else:
    x=generaMatriz(renglon,columna)
    print(x)
  pass

if __name__=='__main__':
    main()
