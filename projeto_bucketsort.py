import time
import random
import string
import matplotlib.pyplot as plt
import math
import sys

# Aumenta o limite de recursão para listas muito grandes (se o Insertion Sort fosse recursivo)
sys.setrecursionlimit(200000)

# --- FUNÇÃO AUXILIAR: INSERTION SORT ---
# Bucket Sort geralmente usa um algoritmo simples para ordenar os baldes
# O Insertion Sort é a escolha comum por ser eficiente em pequenas listas.
def insertion_sort(bucket, reverse=False):
    for i in range(1, len(bucket)):
        chave = bucket[i]
        j = i - 1
        
        while j >= 0:
            # Lógica para Crescente vs Decrescente
            if not reverse:
                # Crescente: se o elemento atual for menor que o anterior, troca
                condicao = chave < bucket[j]
            else:
                # Decrescente: se o elemento atual for maior que o anterior, troca
                condicao = chave > bucket[j]
                
            if condicao:
                bucket[j + 1] = bucket[j]
                j -= 1
            else:
                break
        bucket[j + 1] = chave
    return bucket

# --- 2. IMPLEMENTAÇÃO DO BUCKET SORT ---
def get_key(item):
    """Retorna o valor numérico para ordenação de diferentes tipos de dados."""
    if isinstance(item, int):
        return item
    if isinstance(item, Aluno):
        return item.ra  # Ordena pelo RA do Aluno
    # Para strings, retorna a soma dos valores ASCII dos 5 primeiros caracteres
    if isinstance(item, str):
        return sum(ord(c) for c in item[:5])
    return 0
    
def bucket_sort(lista, reverse=False, num_buckets=10):
    if not lista:
        return []

    # 1. Encontrar o valor máximo e mínimo para normalização
    max_val = get_key(lista[0])
    min_val = get_key(lista[0])
    
    # Encontra o min e max para todos os itens, usando a chave
    for item in lista:
        key = get_key(item)
        if key > max_val: max_val = key
        if key < min_val: min_val = key

    # Garante uma diferença mínima para evitar divisão por zero
    if max_val == min_val:
       
        return insertion_sort(lista, reverse)
        
    # 2. Criar os baldes (Buckets)
    buckets = [[] for _ in range(num_buckets)]
    
    # Range para o cálculo do índice do balde
    bucket_range = (max_val - min_val) / num_buckets

    # 3. Distribuição dos elementos nos baldes
    for item in lista:
        key = get_key(item)
        # Calcula o índice: normaliza o valor para o intervalo [0, num_buckets - 1]
        index = math.floor((key - min_val) / bucket_range)

        # O valor máximo pode cair no index 'num_buckets', forçamos o último balde
        if index == num_buckets:
            index = num_buckets - 1
            
        buckets[index].append(item)
        
    # 4. Ordenar individualmente os baldes e concatenar
    lista_ordenada = []
    for bucket in buckets:
        # Usa o Insertion Sort para ordenar o balde
        lista_ordenada.extend(insertion_sort(bucket, reverse=False)) 

    # 5. Tratamento para ordenação Decrescente
    if reverse:
        return lista_ordenada[::-1]
        # O Bucket Sort (e o Insertion Sort dentro do balde) foi feito crescente.
        # Para decrescente, basta inverter a lista final, que já está ordenada.
    return lista_ordenada

# --- CLASSE PARA TESTE COM OBJETOS (ALUNO) ---
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

# Método para representação visual
def __repr__(self):
        return f"{self.nome} ({self.ra})"

# --- FUNÇÕES DE TESTE E MEDIÇÃO ---
def gerar_lista_inteiros(tamanho, limite=100000):
    # Gera inteiros em um range conhecido, ideal para Bucket Sort
    return [random.randint(0, limite) for _ in range(tamanho)]

def gerar_lista_strings(tamanho):
    # Gera strings aleatórias de 5 letras
    return [''.join(random.choices(string.ascii_uppercase, k=5)) for _ in range(tamanho)]

def gerar_lista_objetos(tamanho):
    # Gera objetos da classe Aluno
    return [Aluno(f"Aluno{i}", random.randint(1000, 9999)) for i in range(tamanho)]

def medir_tempo(algoritmo, lista, reverse=False):
    inicio = time.time()
    algoritmo(lista, reverse)
    fim = time.time()
    return (fim - inicio) * 1000 # Retorna em milissegundos

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    tamanhos = [1000, 5000, 10000, 20000, 50000] # Tamanhos variados
    tempos_int = []
    tempos_str = []
    
    print(f"{'='*40}")
    print(f"PROJETO 02 - BUCKET SORT")
    print(f"Alunos: Geraldo Lucas & Davi Luis")
    print(f"{'='*40}\n")

    # 1. Teste de Correção (Crescente/Decrescente e Tipos)
    print(">>> Verificando funcionamento correto...")
    lista_teste = [5, 22, 9, 11, 5, 6, 25] 
    print(f"Original: {lista_teste}")
    print(f"Crescente: {bucket_sort(lista_teste, reverse=False)}")
    print(f"Decrescente: {bucket_sort(lista_teste, reverse=True)}")

    
    lista_obj = gerar_lista_objetos(5)
    print(f"Objetos originais (RAs): {[a.ra for a in lista_obj]}")
    print(f"Objetos ordenados por RA (Cresc): {bucket_sort(lista_obj)}")
    print("-" * 30)
    
    # 2. Experimentos de Tempo
    print(">>> Iniciando medições de tempo (ms)...")
    for t in tamanhos:
        # Inteiros
        lista_int = gerar_lista_inteiros(t)
        tempo = medir_tempo(bucket_sort, lista_int)
        tempos_int.append(tempo)
        print(f"Inteiros - {t} elementos: {tempo:.4f} ms")

        # Strings
        lista_str = gerar_lista_strings(t)
        tempo_str = medir_tempo(bucket_sort, lista_str)
        tempos_str.append(tempo_str)
        print(f"Strings  - {t} elementos: {tempo_str:.4f} ms")
    
    # 3. Geração de Gráficos
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
