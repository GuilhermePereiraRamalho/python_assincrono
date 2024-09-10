import datetime
import math
import asyncio


async def main():
    print("Realizando o processamento matemático de forma assíncrona.")

    inicio = datetime.datetime.now()

    #asyncio.run(computar(inicio=1, fim=50_000_000))
    task1 = asyncio.create_task(computar(inicio=1, fim=10_000_000))
    task2 = asyncio.create_task(computar(inicio=10_000_001, fim=20_000_000))
    task3 = asyncio.create_task(computar(inicio=20_000_001, fim=30_000_000))
    task4 = asyncio.create_task(computar(inicio=30_000_001, fim=40_000_000))
    task5 = asyncio.create_task(computar(inicio=40_000_001, fim=50_000_000))

    await asyncio.gather(task1, task2, task3, task4, task5)

    tempo = datetime.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():.2f} segundos.")


async def computar(fim, inicio = 1):
    pos = inicio
    fator = 1000 * 1000

    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == "__main__":
    asyncio.run(main())

"""
Terminou em 11.87 segundos. - padrão
Terminou em 9.94 segundos. - com threads
Terminou em 3.88 segundos. - com multiprocessos
Terminou em 11.09 segundos. - com programação assincrona modo 1
Terminou em 12.80 segundos. - com programação assincrona modo 2
"""