'''
5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  
'''

import time
import random

# Simula o estado das lâmpadas
def verificar_lampadas():
    # Simulação: aleatoriamente decide quais lâmpadas estão acesas e quais estão apagadas
    # Aqui, 'True' significa acesa e 'False' significa apagada.
    # O estado real pode ser controlado manualmente ou de outra forma.
    return [random.choice([True, False]) for _ in range(3)]

def main():
    # Simulação dos interruptores
    interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"]
    
    print("Ligando o Interruptor 1...")
    # Liga o interruptor 1
    time.sleep(5)  # Espera por 5 segundos (simula tempo em que o interruptor 1 fica ligado)
    
    print("Desligando o Interruptor 1 e ligando o Interruptor 2...")
    # Desliga o interruptor 1 e liga o interruptor 2
    # Desliga o Interruptor 1 e liga o Interruptor 2
    # Aqui pode ser simulado ou feito manualmente, dependendo do ambiente real

    print("Verificando o estado das lâmpadas...")
    lampadas = verificar_lampadas()

    # Simulação do resultado de verificar as lâmpadas
    estado_lampadas = {
        "Lampada 1": lampadas[0],
        "Lampada 2": lampadas[1],
        "Lampada 3": lampadas[2]
    }

    print("Estado das lâmpadas:", estado_lampadas)

    # Determina qual lâmpada está acesa e qual está quente ou fria
    acesa = [lampada for lampada, estado in estado_lampadas.items() if estado]
    fria = [lampada for lampada, estado in estado_lampadas.items() if not estado]

    # Resultados
    print("A lâmpada acesa é controlada pelo Interruptor 2.")
    print("A lâmpada fria e apagada é controlada pelo Interruptor 3.")
    print("A lâmpada quente e apagada é controlada pelo Interruptor 1.")

if __name__ == "__main__":
    main()
