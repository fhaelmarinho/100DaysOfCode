# ✨ Desafio 100 Dias de Código - Dia 2/100 💻

'''
A taxa de entrada do estacionamento é 2;
A primeira hora completa ou parcial custa 3;
Cada hora completa ou parcial subsequente (após a primeira) custa 4.
Você entrou no estacionamento no horário E e saiu no horário L. Nesta tarefa, os horários são representados como strings no formato "HH:MM" (onde "HH" é um número de dois dígitos entre 0 e 23, que representa as horas, e "MM" é um número de dois dígitos entre 0 e 59, que representa os minutos).
'''

import datetime

def parking_bill(E, L):

    entrace_hour = datetime.datetime.strptime(E, '%H%M') # função que converte string em objeto datetime
    exit_hour = datetime.datetime.strptime(L, '%H%M')   # função que converte string em objeto datetime

    total = exit_hour - entrace_hour #calcula a diferença de tempo

    total_time = total.total_seconds()/3600 #Divisão do total de segundos para pegar hora

    if total_time <= 1:
        total = 2 + 3
    else:
        total = 2 + 3 + int((total_time - 1)* 4)

    return total


# Chamada da função com valores de exemplo
E = "0900"
L = "1130"

print(parking_bill(E, L))