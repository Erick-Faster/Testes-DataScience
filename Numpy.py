# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 02:13:26 2020

@author: erick
"""

import numpy as np

'''
[100] - Biblioteca Nmpy
'''
a1 = np.array(['Jolyne', 'Josuke', 'Jotaro']) 

a2 = np.array((['Jolyne', 'Josuke', 'Jotaro'], [1,2, 3])) #2 listas na array. Deve usar 2 parenteses

#Verifica tamanho da array
a1.shape
a2.shape #(x, y) -> Tenho x listas (linhas) com y elementos (colunas)

a3 = np.array(([1,2,3],[4,5,6]))

a3.max() #Retorna o valor maximo da matriz
a3.ndim #Retorna numero de dimensoes

a4 = np.arange(20) #Cria array de 0 a 20
a4 = np.arange(0,100,10) #(inicio,fim,passo)

a5 = np.linspace(0,10,20) #(inicio, fim, qtde de elementos até o fim)

a6 = np.zeros((20,20)) #Cria matriz soh de zeros
a7 = np.ones((20,20)) #Cria matriz soh de 1
a8 = np.eye(10) #Cria matriz identidade
a9 = np.diag((1,2,3,4,5,6,7,8,9)) #Cria matriz identidade com numeros customizados
a10 = np.empty((10,5)) #Cria matriz vazia (c valores mega pequenos (??))

a11 = np.tile([[1,2,3], [3,4,5]], 3) #Adiciona matriz a direita
a12 = np.tile(a3, (3,3)) #Adiciona matriz abaixo

'''
[101]Tipagem
'''

a1 = np.array([1,2,3,4],dtype='float') #Converte os arquivos para Float
a1.dtype #verifica tipo

a1 = a1.astype(int) #Converte pra int

a2 = np.arange(20)+1 #Monta matriz e soma +1 para cada elemento em tempo de execucao

a3 = a2.copy() #Copia em outra alocacao de memoria

a4 = np.array([True, False, True, False])
a5 = np.array([True, True, False, False])
np.logical_and(a4,a5) #Retorna operador AND
np.logical_or(a4,a5) #Retorna operador OR

'''
[102]Performance
'''

#Rodar no Console. Calcula tempo de execucao
%timeit #Testa a msm linha
%%timeit #Testa um bloco de codigo. Executa com shift + enter

'''
[103]Indexacao de Arrays
'''

a = np.array([1,2,11,6,8,18,2])
a[-1] #Ultimo elemento
a[0:3] #Slice
a[0:3:2] #Passo 2
a[:4] #Slice ate o 4
a[2:] #Slice iniciando do 2
a[:] #Pega tudo
a[::2] #Slice com passo 2

x = np.array([3,6,8,4])
y = np.array([11,8,3])
z = np.concatenate([x,y])

'''
[104]Matrizes Multidimensionais
'''

x = np.array(([1,2,3],[4,5,6], [7,8,9]))

z = x[:2,:2]
z = x[:2,1:]
z = x[1:,:2]
z = x[1:,1:]
z = x[2,:]
z = x[:,0]

x[1:,:2] = 0 #transforma parte da matriz em 0

'''
[105]Matrizes
'''

x = np.matrix([[1,2],[3,4]]) #Reparar nos colchetes
x.shape

y = x.T #Matriz Transposta. Inverte linhas e colunas

'''
[106]Transpose e Reshaping
'''

A = np.array(([1,2,3], [4,5,6]))

B = np.transpose(A) #Transposta

A.ravel() #Transforma tudo numa array, da esquerda pra direita
A.T.ravel() #Msm coisa, de cima pra baixo

X = np.random.randint(1,10, size=(4,4))
np.any(X == 1) #Verifica se qqr elemento eh igual a 0
np.any(X[:2, :2] == 8)

np.all(X > 0) #Verifica se todos os valores sao maiores que zero

Y = np.arange(1,16)
Y.reshape(3,5) #Transforma array em matriz (x,y)

Z = np.array(([2,7,3], [1,8,6]))
Z.sort(axis=1) #Ordenar por linha
Z.sort(axis=0) #Ordenar por coluna