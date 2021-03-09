print('\033[1;31;46m Olá vermelho negrito com fundo amarelo! \033[m')
print('\033[30m Não sei por que não ficou branco \033[m')
print('\033[7m invertido do padrão \033[m')
a = 3
b = 6
print('Os valores são \033[31m{}\033[m e \033[33m{}\033[m '.format(a,b))

cor = {'fecha': '\033[m', 'verde': '\033[32m', 'amarelo': '\033[33m'}
print('Uma palavra em {}verde{} e outra em {}amarelo{}'.format(cor['verde'], cor['fecha'], cor['amarelo'], cor['fecha']))
