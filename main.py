import time
import os 

def cls():
  os.system("clear")


nome_usuario = input('oi, qual seu nome??\n\n')
print('\n\nbelo nome!! \n') #comando para dar nome ao usuario

lista = ['não', 'bom dia','conte uma historia','qual seu nome','ola','chau'] #lista de frases para não entrar fala: não sei dizer

lista_2 = ['sei la'] #lista pata teste(encontrar perfil de usuario)

conversa = 10
while(conversa < 20): #loop com limite de 20 perguntar antes de apresentar frase: estou cansado
  time.sleep(1)

  eu = input('\n(Jarvis) '+ nome_usuario + ', pergunte-me algo:\n\n') # pergunda do loop

  if eu == 'não':
    print('\n ok, adeus então')
    time.sleep(1)
    print('\n\n e sai caminhando triste e cabisbaixo =s')
    break    
    
  if eu == 'ola':
    print('\n(Jarvis): ola')
  if eu =='bom dia':
    print('\n(Jarvis): bom dia')
  if eu == 'conte uma historia':
    f = open('conto.txt') #comando que puxa o texto escrito separado
    conteudo = f.read()
    f.close()
    print(conteudo)
  if eu == 'qual seu nome':
    print('\n(Jarvis): Jarvis oxii !!!')
  if eu not in lista:
    print('\n (Jarvis) não sei dizer')
    
  if eu == 'chau':
    print('\n até logo')
    break

  if eu in lista_2:
    print('\n(Jarvis) você parece alguem ansioso')

  conversa = conversa + 1
  if conversa == 20:
     print('\n (Jarvis) estou cansado, chau!!!')
     time.sleep(1)
     print('\n\n e ele sai andando...')
     time.sleep(1)
  time.sleep(3)   
  cls() 
