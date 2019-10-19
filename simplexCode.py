import numpy as np
import matplotlib.pyplot as plt

leitura=open("in.txt",'r')
file_data = leitura.readlines()
leitura.close

plt.grid(True)
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("PPL resolução em Modo Gráfico")

restricao =[]
funcaoObj = []
xRestSemSinal = []

sinalValor = []
contSinal = 0
contNumber = 0
encontraSina1 = False

for i in range(len(file_data)):
    restricao.append(file_data[i].split())
    
for i in range(len(restricao)):
    encontraSinal = False 
    xRestSemSinal1 = []
    sinalValor1 = []
    
    for j in range(len(restricao[i])):
            if i == 0:
               funcaoObj.append(restricao[i][j])
            else:   
                if restricao[i][j] == '=' or restricao[i][j] == '>' or restricao[i][j] == '<'or restricao[i][j] == '<=' or restricao[i][j] == ">=":
                    encontraSinal = True
                if encontraSinal == True:
                    sinalValor1.append(restricao[i][j])
                else:    
                    xRestSemSinal1.append(restricao[i][j])

    if len(sinalValor1)>0:
        sinalValor.append(sinalValor1)
    if len(xRestSemSinal1) >0:
        xRestSemSinal.append(xRestSemSinal1)
   
##achando valor da funcao obj
pontosFunGr = []

valorMultObj = int(1)
for i in range(len (funcaoObj)):
    valorMultObj *= int(funcaoObj[i])
    
funcaoObj.append("=")
funcaoObj.append(valorMultObj)

for i in range(len (funcaoObj) - 2):
    pontosFunGr.append(int(funcaoObj[len (funcaoObj)-1]/int(funcaoObj[i])))

print(pontosFunGr)

arrayPonGr = []
for i in range(len(xRestSemSinal)):
    arrayPonAux = []
    for j in range(len(xRestSemSinal[i])):
        print(xRestSemSinal[i][j])
        if(int(xRestSemSinal[i][j])!=0):
          arrayPonAux.append(int (sinalValor[i][len (sinalValor[i])-1])/int(xRestSemSinal[i][j]))
        else:
           arrayPonAux.append(0)
    if len(arrayPonAux)>0:
        arrayPonGr.append(arrayPonAux)
           

print(funcaoObj)
x = np.linspace(pontosFunGr[0],0,pontosFunGr[1]+1)

plt.plot(x, 'r--')
print(arrayPonGr)

for i in range(len(arrayPonGr)):
    if(len(arrayPonGr[i])<2):
        arrayPonGr[i].insert(0,0)
print(arrayPonGr)

for i in range(len(arrayPonGr)):
    x = np.linspace(int(arrayPonGr[i][0]),0,int(arrayPonGr[i][1]+1))
    plt.plot(x)
##criar retas  pra depois plotar 
##posso ver onde comeca a reta e onde termina a maior ou menor itercessao
    


print(arrayPonGr)
print(valorMultObj)
print(funcaoObj)
print(xRestSemSinal)
print(sinalValor)
plt.show()

