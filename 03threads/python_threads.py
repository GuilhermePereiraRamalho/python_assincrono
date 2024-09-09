import datetime
import math
import threading
import multiprocessing


def main():
    qrd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processamento matemático com {qrd_cores} core(s)")

    inicio = datetime.datetime.now()

    threads = []
    for n in range(1, qrd_cores+1):
        ini = 50_000_000 * (n-1) / qrd_cores
        fim = 50_000_000 * n / qrd_cores
        print(f"Core {n} processando de {ini} até {fim}")
        threads.append(
            threading.Thread(
                target=computar,
                kwargs={"inicio": ini, "fim": fim},
                daemon=True
            )
        )
    
    [th.start() for th in threads]
    [th.join() for th in threads]

    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")


def computar(fim, inicio = 1):
    pos = inicio
    fator = 1000 * 1000

    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    main()


"""
Terminou em 11.87 segundos. - padrão
Terminou em 9.94 segundos. - com threads
"""