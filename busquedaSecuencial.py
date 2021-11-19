#!/usr/bin/python
#coding: utf-8

# Filename  : ShellSort.py
# Autor     : Joshua Ayala
# Website   : https://github.com/JoshuaAyala/busquedaSecuencialPython.py
# pep8: 100%

import random

def busqueda(lista, numero):
	x=0
	for i in range(0, len(lista)):
		x+=1
		if(lista[i]==numero):
			return "[+] El número se encuentra en la lista en la posición: ", x
		elif(x==len(lista)):
			return ("[!] El número no se encuentra en la lista.")
lista = []

l = int(input("Hasta qué numero deseas generar numeros aleatorios?\n>: "))
for x in range(0, 50):
	lista.append(random.randint(1,l))

n = int(input("¿Qué número deseas buscar?\n>: "))
print("\n+- Lista: ", lista, "\n\n", busqueda(lista, n))