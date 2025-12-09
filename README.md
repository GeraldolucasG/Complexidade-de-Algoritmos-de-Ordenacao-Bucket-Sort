# 📚 Projeto 02: Avaliação da Complexidade do Algoritmo Bucket Sort

## 🎓 Disciplina
Estrutura de Dados

## 👥 Integrantes
* **Geraldo Lucas** | RA: 22407967
* **Davi Luis** | RA: 22404416

---

## 🎯 Objetivo

O objetivo deste projeto foi investigar a eficiência e a complexidade computacional do algoritmo de ordenação **Bucket Sort** (Ordenação por Baldes). Implementamos o algoritmo em Python, medimos seu desempenho com diferentes volumes e tipos de dados (Inteiros, Strings e Objetos) e comparamos os resultados práticos com sua complexidade teórica (O(n+k) no caso médio).

## 📚 Referências Bibliográficas (Base Teórica)

As seguintes fontes serviram de requisito e base teteórica para o desenvolvimento deste projeto:

Felippe Pires Ferreira. Avaliação da Complexidade de Algoritmos de Ordenação. Material didático da disciplina de Estrutura de Dados. 2025.

FILHO, Paulo de Tarso de Carvalho Bayma. Análise comparativa de algoritmos de ordenação com foco na complexidade computacional e na Notação Big O... Revista Caderno Pedagógico, Curitiba, v. 22, n. 11, p. 01-14, 2025.

PEDROSO, Alexandre da Silva; CINTRA, Fausto Gonçalves. Estudo Analítico do Desempenho de Algoritmos de Ordenação. Revista EduFatec: educação, tecnologia e gestão, v. 2, n. 5, ago./dez. 2022.

DEV, Media. Algoritmos de ordenação: análise e comparação. Disponível em: https://www.devmedia.com.br/algoritmos-de-ordenacao-analise-e-comparacao/28261. Acesso em: 08 Dez. 2025.


## 💡 Algoritmo Escolhido: Bucket Sort

O Bucket Sort é um algoritmo de **não-comparação** que se destaca pela sua alta eficiência em cenários específicos.

* **Funcionamento:** O algoritmo divide o conjunto de dados em um número finito de "baldes" (buckets), distribui os elementos nos baldes, ordena cada balde individualmente (utilizando **Insertion Sort** na nossa implementação) e, por fim, concatena os baldes.
* **Complexidade Teórica (O(n+k)):**
    * **Caso Médio / Melhor Caso:** O(n+k), onde n é o número de elementos e k é o número de baldes. Essa eficiência quase linear é alcançada quando a entrada tem uma distribuição uniforme.
    * **Pior Caso:** O(n^2), se todos os elementos caírem no mesmo balde (devido à complexidade do Insertion Sort interno).

---

## 🧪 Metodologia Experimental

O algoritmo foi implementado em Python e testado utilizando o módulo `time` para medição precisa em milissegundos (ms), conforme os requisitos do projeto.

| Cenário de Teste | Descrição |
| :--- | :--- |
| **Implementação** | Implementação recursiva com suporte a ordenação Crescente (`reverse=False`) e Decrescente (`reverse=True`). |
| **Tipos de Dados** | Números Inteiros (simulando distribuição uniforme), Strings e Objetos (classe `Aluno` ordenada pelo atributo `ra`). |
| **Tamanhos (N)** | Listas de 1.000, 5.000, 10.000, 20.000 e 50.000 elementos. |

## 📊 Resultados e Análise

O gráfico gerado pelo `matplotlib`, demonstra o relacionamento entre o tamanho da entrada (N) e o tempo de execução (ms).


**Conclusão da Análise:**
O formato da curva obtida nos testes práticos (Inteiros e Strings) mostra um crescimento quase linear. O tempo de execução não aumenta significativamente com o volume de dados, validando a complexidade O(n+k) do Bucket Sort para os dados que possuem uma boa distribuição.

---

## ⚙️ Como Executar o Código

Para rodar o projeto, é necessário ter o Python 3 instalado e as seguintes bibliotecas:

```bash
pip install matplotlib