import time
import random
import string
import matplotlib.pyplot as plt
import math
import sys


sys.setrecursionlimit(200000)


def insertion_sort(bucket, reverse=False):
    for i in range(1, len(bucket)):
        chave = bucket[i]
        j = i - 1
        
        while j >= 0:
        
            if not reverse:
                
                condicao = chave < bucket[j]
            else:
                
                condicao = chave > bucket[j]
                
            if condicao:
                bucket[j + 1] = bucket[j]
                j -= 1
            else:
                break
        bucket[j + 1] = chave
    return bucket


def get_key(item):
    """Retorna o valor numérico para ordenação de diferentes tipos de dados."""
    if isinstance(item, int):
        return item
    if isinstance(item, Aluno):
        return item.ra  
    if isinstance(item, str):
        return sum(ord(c) for c in item[:5])
    return 0

def bucket_sort(lista, reverse=False, num_buckets=10):
    if not lista:
        return []

    
    max_val = get_key(lista[0])
    min_val = get_key(lista[0])
    
    
    for item in lista:
        key = get_key(item)
        if key > max_val: max_val = key
        if key < min_val: min_val = key

    
    if max_val == min_val:
       
        return insertion_sort(lista, reverse)

    buckets = [[] for _ in range(num_buckets)]
    
    bucket_range = (max_val - min_val) / num_buckets

    for item in lista:
        key = get_key(item)
        
        index = math.floor((key - min_val) / bucket_range)
        
        if index == num_buckets:
            index = num_buckets - 1
            
        buckets[index].append(item)


    lista_ordenada = []
    for bucket in buckets:

        lista_ordenada.extend(insertion_sort(bucket, reverse=False)) 


    if reverse:
        return lista_ordenada[::-1]
    
    return lista_ordenada

class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

def __lt__(self, other):
        """Compara o objeto Aluno atual com 'other' usando o RA."""
        return self.ra < other.ra
    
def __gt__(self, other):
        """Compara o objeto Aluno atual com 'other' usando o RA."""
        return self.ra > other.ra

def __repr__(self):
        return f"{self.nome} ({self.ra})"

def gerar_lista_inteiros(tamanho, limite=100000):
    return [random.randint(0, limite) for _ in range(tamanho)]

def gerar_lista_strings(tamanho):
    return [''.join(random.choices(string.ascii_uppercase, k=5)) for _ in range(tamanho)]

def gerar_lista_objetos(tamanho):
    return [Aluno(f"Aluno{i}", random.randint(1000, 9999)) for i in range(tamanho)]

def medir_tempo(algoritmo, lista, reverse=False):
    inicio = time.time()
    algoritmo(lista, reverse)
    fim = time.time()
    return (fim - inicio) * 1000 


if __name__ == "__main__":
    tamanhos = [1000, 5000, 10000, 20000, 50000] 
    tempos_int = []
    tempos_str = []
    
    print(f"{'='*40}")
    print(f"PROJETO 02 - BUCKET SORT")
    print(f"Alunos: Geraldo Lucas & Davi Luis")
    print(f"{'='*40}\n")

    print(">>> Verificando funcionamento correto...")
    lista_teste = [5, 22, 9, 11, 5, 6, 25] 
    print(f"Original: {lista_teste}")
    print(f"Crescente: {bucket_sort(lista_teste, reverse=False)}")
    print(f"Decrescente: {bucket_sort(lista_teste, reverse=True)}")
    
    lista_obj = gerar_lista_objetos(5)
    print(f"Objetos originais (RAs): {[a.ra for a in lista_obj]}")
    print(f"Objetos ordenados por RA (Cresc): {bucket_sort(lista_obj)}")
    print("-" * 30)

    
    print(">>> Iniciando medições de tempo (ms)...")
    for t in tamanhos:
        lista_int = gerar_lista_inteiros(t)
        tempo = medir_tempo(bucket_sort, lista_int)
        tempos_int.append(tempo)
        print(f"Inteiros - {t} elementos: {tempo:.4f} ms")

       
        lista_str = gerar_lista_strings(t)
        tempo_str = medir_tempo(bucket_sort, lista_str)
        tempos_str.append(tempo_str)
        print(f"Strings  - {t} elementos: {tempo_str:.4f} ms")
    

    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, tempos_int, marker='o', label='Números Inteiros (O(n+k))')
    plt.plot(tamanhos, tempos_str, marker='x', linestyle='--', label='Strings')
    
    plt.title('Desempenho do Bucket Sort: Tamanho vs Tempo')
    plt.xlabel('Tamanho da Entrada (n)')
    plt.ylabel('Tempo de Execução (ms)')
    plt.legend()
    plt.grid(True)
    
    print("\n>>> Gerando gráfico (grafico_complexidade.png)...")
    plt.savefig('grafico_complexidade.png') 
    plt.show() 