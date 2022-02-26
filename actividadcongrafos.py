#!/usr/bin/env python
# coding: utf-8

# In[94]:


import networkx as net
import csv 
import graphviz
import matplotlib.pyplot as plt
import pandas as pd


# In[95]:


g=net.Graph()  #creacion del grafo


# In[96]:


#vamos a crear los nodos


# In[97]:



 valores= ['353','360','382','386','389','393','396','405','445','459',
          '501','610','650','657','671','673','691','1119','1740','1885'
          ,'2335','2352','2584','2621','2646','2798','2838','2879','2898','2908'
          ,'2909','3002','3019','97152','97153','97184','97185','97236',
          '97290','98249','98746','98748','98851','98852','99653','100024','100040'] #valores de codigos a comparar


# In[98]:


df = pd.read_csv("CrossActividad.csv")  #lectura del archivo cvs
ia=0
for i in valores: #ciclo para relacionar los productos y con su peso
    ia=ia+1
    for a in range(1,df.shape[1]):
        temp=df.iloc[ia,a]
        temp=temp.replace("%","")
        print(i+'  '+df.iloc[0,a] +'   '+ temp)
        valo = int(temp) 
        g.add_edge(i,df.iloc[0,a],weight=valo) #añade nodo al grafo


# In[99]:


#print("vecinos al nodo:" ,gn.neighbors('353'))

#print('Vecino' ,g['353'])


# In[100]:


pos=net.spring_layout(gn) #codigo para dibujar el grafo el grafo
net.draw(g,node_size=20, width=.05,with_labels=True,font_weight='bold')
labels=net.get_edge_attributes(g,'weight')
net.draw_networkx_edge_labels(g,pos,edge_labels=labels)


# In[101]:


d=0  #Eleccion del producto base para recomendar el que tenga mayor peso 0 hasta 46

k= valores[d]
print('Nodo elegido '+ k)
posX=''
posY=''
mayor=0
for i in g.neighbors(valores[d]):
  print(i)
  print(g[k][i])
  peso=int(g[k][i].get('weight'))
  if (peso > mayor):
    mayor=peso
    posX=k
    posY=i

print('-------Producto a recomendar:--------')
print(posY)
print(g[posX][posY])
print(mayor)
print('---------------')


# In[ ]:




