import PySimpleGUI as sg
import random
import configuracion
from pattern.es import verbs, tag, spelling, lexicon
import string

## eje 9, 10, 11

boardConfig1=configuracion.Config1()


def comprobarPalabra(palabra):
	





	if not palabra.lower() in verbs:
		
		if not palabra.lower() in spelling:
			
			
			if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
				
			#print('no existe la palabra')
				sg.Popup('la palabra no existe')
			else:
				print('existe')
				sg.Popup('la palabra existe')
			
		else:
			print('existe')
			sg.Popup('la palabra existe')		
			
	else:
		print('existe')
		sg.Popup('la palabra existe')	















def msj():
	print(button)
	##print(initial_atril[3])
	if boardConfig1[button[0]][button[1]].get_estado() == True:
		print('esta ocupado')
	else:
					#print('libre')
		window[i].update('')
		window[button].update(initial_atril[i])
		#palabra += letra
		p2=palabra[0]
		p2=p2+letra
		palabra[0]=p2
		initial_atril[i]=''
		boardConfig1[button[0]][button[1]].set_estado(True)
						
	
	
	
lista=['a','b','c','d','e','f','g','l','m','n','o','p','q','r','s','t','u','v','w','y','z','x']
initial_atril=[]
for i in range(0,7):
	initial_atril.append(random.choice(lista))

def tablero():
	def render(key):
		return sg.Button('',key=key,size=(4,2))
	print('')
	tablero=[]
	for i in range(10):

		row=[]
		for j in range(10):
			row.append(render(key=(i,j)))
		tablero.append(row)
	return tablero

def atril(lista):
	def render(key,texto=''):
		return sg.Button(texto,key=key,size=(4,2))
	atril=[]
	for i in range(7):
		#print(lista[i])
		teo=lista[i]
		row=[]
		row.append(render(texto=teo,key=i))
		atril.append(row)
	return atril
			


tab=tablero()
atr=atril(initial_atril)
boar_tab=[[sg.Button('CHECK')],[sg.Column(atr),sg.Column(tab)]]

window=sg.Window('hola',default_button_element_size=(10,2)).layout(boar_tab)
#palabra='' ## chequear para el siguiente turno
palabra=['']
i=0
cant=0
T1=True
T2= True

F=0
C=0
#lista=[]
while True:
	letra=''
	l=-1
	button , value = window.Read()
	if button == 'CHECK':
		##obj_tablero.get_word()
		if palabra[0] == '':
			sg.Popup('todavia no formo una palabra')
		else:
		    #print(palabra[0])
		    comprobarPalabra(palabra[0])
	
	if button in (None , 'EXIT'):
		exit()


		
	if type(button) is int:
		
		if initial_atril[button] !='':
			letra= initial_atril[button]
			#palabra += letra
			i=button
		
		
			button , value = window.Read()
			if type(button) is tuple:
				
			
				if cant<1:
					cant=cant+1
					msj()
					F=button[0]
					C=button[1]
	
				else:
				###hoy
					if(button[0]==F)and T1:
						if C<button[1]:
							T2=False
							msj()
							C=button[1]					
					if(button[1]==C)and T2:
						if F<button[0]:
							print(button)
							T1=False
							msj()
							F=button[0]									
		

				l=0

		
		
		
	if type(button) is tuple:
		if l ==-1:
			
			sg.Popup('movimiento incorrecto')
