from datetime import datetime
import autowhatspy
import os
import time



with open('teste1.txt','w') as file:
    file.write(input('Digite a mensagem:'))
with open('teste2.txt','w') as file:
    file.write(input('informe o nome do contato:'))

path = os.path.dirname(os.path.realpath(__file__))+'\\'

msg = path+'teste1.txt'
ctt = path+'teste2.txt'
gdv=path+'geckodriver.exe'
gdv_log = 'geckolog.txt'
user_pfl = path+"vvdkjme9.WhatsPy-Test-User"

while True:
    autowhatspy.message_to_contacts(msg,ctt,gdv,gdv_log,user_pfl)
    print('pass')
    break

try:
    with open('teste1.txt','r') as file:
        print('mensagem enviada: '+file.read())
    os.remove('teste1.txt')
    os.remove('teste2.txt')

except:
    print('erro')