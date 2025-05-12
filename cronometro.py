import time
    
def cronometro():
    print("Cronômetro iniciado! Pressione Ctrl+C para parar.")
    tempo_inicial = time.time()  # Marca o tempo inicial
    
    try:
        while True:
            tempo_decorrido = time.time() - tempo_inicial  # Tempo decorrido desde o início
            minutos = int(tempo_decorrido // 60)  # Calcula os minutos
            segundos = int(tempo_decorrido % 60)  # Calcula os segundos
            print(f"{minutos:02}:{segundos:02}", end="\r")  # Exibe no formato MM:SS, com retorno de linha
            time.sleep(1)  # Pausa por 1 segundo para evitar que o programa consuma muitos recursos
    except KeyboardInterrupt:
        print("\nCronômetro interrompido.")
        pass

cronometro()