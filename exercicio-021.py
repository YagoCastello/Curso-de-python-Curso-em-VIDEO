from pygame import mixer
mixer.init()
mixer.music.load('ocarinaoftime.mp3')
mixer.music.play()
x=str(input('Agora você escuta? se sim por favor digite sim como resposta:')).upper().strip()
if x == 'SIM':
    print('{}Esta tudo funcionando bem{}'.format('\033[1;32;45m','\033[m'))
else:
    print('{}Desculpe, ocorreu um problema{}'.format('\033[4;31;46m','\033[m'))

