from datetime import datetime

message = 'Error en base de datos'
date = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # año-mes-dia hora:minuto:segundo

with open('logs.txt', mode='a') as log:
    log.write(f'[{date}] {message}\n')

with open('logs.txt', mode='r') as log:
    print(log.read())