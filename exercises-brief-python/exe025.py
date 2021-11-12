s_dia = 86400
s_hora = 3600
s_minuto = 60

segundos = int(input('Digite um número de segundos: '))

dia = segundos / s_dia
segundos = segundos % s_dia

horas = segundos / s_hora
segundos = segundos % s_hora

minutos = segundos / s_minuto
segundos = segundos % s_minuto

print('A duração equivalente é', '%d:%02d:%02d:%02d.' % (dia, horas, minutos, segundos))
