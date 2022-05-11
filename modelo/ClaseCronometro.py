import os
import time

class Cronometro():
    def __init__(self):
    ##Esta clase permite mostrar el tiempo transcurrido
        for hora in range(24):
            for minuto in range(60):
                for segundo in range(60):
                    os.system('cls')
                    print(f'{hora}:{minuto}:{segundo}')
                    time.sleep(1)