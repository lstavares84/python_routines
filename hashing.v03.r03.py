import random
import time
from datetime import datetime


# Classe para representar um empregado
class Employee:
    def __init__(self, matricula, salario, setor):
        self.matricula = matricula  # Atributo para a matrícula do empregado
        self.salario = salario  # Atributo para o salário do empregado
        self.setor = setor  # Atributo para o setor do empregado

# Classe para representar a tabela hash
class HashTable:
    def __init__(self, M):
        self.M = M  # Tamanho da tabela hash
        self.table = [None] * M  # Inicializa a tabela com M espaços vazios
        self.append_count = [0] * M  # Lista para armazenar a quantidade de 'append' por índice

    def hash_function(self, key):
        return key % self.M  # Calcula o índice na tabela usando a função de hash

    def insert(self, employee):
        index = self.hash_function(int(employee.matricula))  # Calcula o índice usando a função de hash
        if self.table[index] is None:
            self.table[index] = [employee]  # Se o slot estiver vazio, insere o empregado na lista do slot
        else:
            self.table[index].append(employee)  # Caso contrário, adiciona o empregado à lista existente
            self.append_count[index] += 1  # Incrementa a contagem de 'append'

    def search(self, key):
        index = self.hash_function(int(key))  # Calcula o índice usando a função de hash
        if self.table[index] is not None:
            for employee in self.table[index]:  # Procura na lista do slot pelo empregado com a matrícula correspondente
                if employee.matricula == key:
                    return employee  # Retorna o empregado encontrado
        return None  # Retorna None se o empregado não for encontrado

# Função para popular a tabela hash com registros aleatórios
def populate_hash_table(hash_table, num_records):
    records = []
    for _ in range(num_records):
        matricula = str(random.randint(100000000, 999999999))  # Gera uma matrícula aleatória
        salario = round(random.uniform(1000, 10000), 2)  # Gera um salário aleatório
        setor = random.randint(1, 10)  # Gera um setor aleatório
        employee = Employee(matricula, salario, setor)  # Cria um empregado com os valores aleatórios
        hash_table.insert(employee)  # Insere o empregado na tabela hash
        records.append(employee)  # Adiciona o registro à lista de registros
    return records

# Função para executar Iterações de testes
def run_iterations(M_values):
    
    results_collisions = []  # Lista para armazenar o número de colisões em cada Iteração
    results_search_time_hash = []  # Lista para armazenar o tempo médio de busca usando a tabela hash em cada Iteração
    results_search_time_linear = []  # Lista para armazenar o tempo médio de busca usando busca linear em cada Iteração
    results_key_length = []  # Lista para armazenar o tamanho médio das chaves em cada Iteração

    for M in M_values:  # Para cada tamanho de tabela hash (M)
        print(f"Tabela Hash com M = {M}")
        for num_records in num_records_list:  # Para cada número de registros
            print(f"Iteração com {num_records} registros:")
            hash_table = HashTable(M)  # Cria uma nova tabela hash com tamanho M
            records = populate_hash_table(hash_table, num_records)  # Popula a tabela hash com registros aleatórios

            total_collisions = sum(1 for slot in hash_table.table if slot is not None and len(slot) > 1)  # Calcula o número total de colisões
            average_search_time_hash = 0
            average_search_time_linear = 0
            total_key_length = 0

            for _ in range(num_records):  # Para cada registro
                while True:
                    random_slot = random.choice(hash_table.table)  # Seleciona um slot aleatório da tabela hash
                    if random_slot is not None and len(random_slot) > 0:  # Verifica se o slot não está vazio
                        break
                matricula = random.choice(random_slot).matricula  # Seleciona aleatoriamente uma matrícula do slot

                start_time_hash = time.time()  # Marca o início da medição de tempo de busca usando a tabela hash
                hash_table.search(matricula)  # Realiza a busca na tabela hash
                end_time_hash = time.time()  # Marca o fim da medição de tempo de busca usando a tabela hash
                average_search_time_hash += (end_time_hash - start_time_hash) * 1000  # Calcula o tempo de busca em milissegundos

                start_time_linear = time.time()  # Marca o início da medição de tempo de busca usando busca linear
                linear_search(records, matricula)  # Realiza a busca linear
                end_time_linear = time.time()  # Marca o fim da medição de tempo de busca usando busca linear
                average_search_time_linear += (end_time_linear - start_time_linear) * 1000  # Calcula o tempo de busca em milissegundos

            average_search_time_hash /= num_records  # Calcula o tempo médio de busca usando a tabela hash
            average_search_time_linear /= num_records  # Calcula o tempo médio de busca usando busca linear
            total_key_length = sum(hash_table.hash_function(int(employee.matricula)) for slot in hash_table.table if slot is not None for employee in slot)  # Calcula o tamanho total das chaves
            average_key_length = total_key_length / num_records  # Calcula o tamanho médio das chaves

            print(f"Número de Colisões: {total_collisions}")
            print(f"Tempo Médio de Busca por Hash (ms): {average_search_time_hash}")
            print(f"Tempo Médio de Busca por Linear (ms): {average_search_time_linear}")
            print(f"Tamanho Médio das Chaves (em relação ao número de matrícula): {average_key_length}\n")
            
            results_collisions.append(total_collisions)  # Adiciona o número de colisões à lista de resultados
            results_search_time_hash.append(average_search_time_hash)  # Adiciona o tempo médio de busca usando a tabela hash à lista de resultados
            results_search_time_linear.append(average_search_time_linear)  # Adiciona o tempo médio de busca usando busca linear à lista de resultados
            results_key_length.append(average_key_length)  # Adiciona o tamanho médio das chaves à lista de resultados

    # Carlos, eis a garantia do POKA YOKE de que os valores vão estar zerados para a próxima iteração
    total_collisions = 0
    average_search_time_hash = 0
    average_search_time_linear = 0
    total_key_length = 0
    return results_collisions, results_search_time_hash, results_search_time_linear, results_key_length  # Retorna as listas de resultados

# Função para busca linear em uma lista de registros
def linear_search(records, key):
    for record in records:  # Para cada registro na lista de registros
        if record.matricula == key:  # Se a matrícula do registro for igual à chave de busca
            return record  # Retorna o registro encontrado
    return None  # Retorna None se o registro não for encontrado


if __name__ == "__main__":

    start_datetime = datetime.now()  # Armazena a data e hora de início da execução
    print("Data e hora de início: {}".format(start_datetime))  # Mostra a data e hora de início da execução
    start_time_total = time.time()  # Registrar o tempo de início da execução

    num_records_list = [5000, 20000, 100000]  # Lista de números de registros para cada Iteração
    M_values = [1000, 10000, 100000]  # Lista de tamanhos da tabela hash para cada Iteração
    #M_values = [997, 9973, 99991]  # Lista de tamanhos da tabela hash para cada Iteração

    results = []  # Lista para armazenar os resultados dos Iterações
    append_count_per_iteration = []  # Lista para armazenar a contagem de 'append' por Iteração


    for iteration in range(5):
        # Executa os iterações de teste e armazena os resultados
        results_collisions, results_search_time_hash, results_search_time_linear, results_key_length = run_iterations(M_values)
        hash_table = HashTable(M_values[0])  # Cria uma tabela hash com tamanho do primeiro Iteração
        records = populate_hash_table(hash_table, num_records_list[0])  # Popula a tabela hash com registros aleatórios
        append_count_per_iteration.append(hash_table.append_count.copy())  # Armazena a contagem de 'append' para o Iteração

        # # Armazena os resultados do Iteração atual
        results.append((iteration + 1, results_collisions, results_search_time_hash, results_search_time_linear, results_key_length))

    end_time_total = time.time()  # Registrar o tempo de término da execução
    end_datetime = datetime.now()  # Armazena a data e hora de término da execução
    total_duration_seconds = end_time_total - start_time_total  # Calcula a duração total da execução em segundos
    total_duration_minutes = total_duration_seconds // 60  # Calcula a duração total em minutos
    total_duration_seconds %= 60  # Calcula os segundos restantes após os minutos

    # Imprime os resultados dos iterações na forma de uma tabela
    print("\n#################### Resultados Finais Comparativos ####################")
    print("{:<8} | {:<15} | {:<12} | {:<10} | {:<32} | {:<35} | {:<31} | {:<20}".format(
        "Iteração", "Num. Registros", "M da Tabela", "Colisões", "Tempo Médio de Busca (Hash) (s)", "Tempo Médio de Busca (Linear) (s)", "Tamanho Médio das Chaves", "Append Count"))
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i, (iteration_num, collisions, search_time_hash, search_time_linear, key_length) in enumerate(results):
        for j, (num_records, M) in enumerate(zip(num_records_list, M_values)):
            append_count = append_count_per_iteration[i][j] if j < len(append_count_per_iteration[i]) else 0
            if search_time_hash[j] == 0:
                difference_percent = 0
            else:
                difference_percent = ((search_time_linear[j] - search_time_hash[j]) / search_time_hash[j]) * 100
            # Imprime os resultados do Iteração atual na tabela formatada
            print("{:<8} | {:<15} | {:<12} | {:<10} | {:<32.3e} | {:<24.3e} ({:.2f}%) | {:<31.2f} | {:<20}".format(
                iteration_num, num_records, M, collisions[j], search_time_hash[j] * 0.001, search_time_linear[j] * 0.001, difference_percent, key_length[j], append_count))

    # Imprime o tempo total de execução e a data e hora de término
    print("\nTempo total de execução: {:.0f}m:{:.0f}s".format(total_duration_minutes, total_duration_seconds))
    print("Data e hora de término: {}".format(end_datetime))  # Mostra a data e hora de término da execução

'''
Passo 1: Função run_iterations(M_values)
Para cada tamanho de tabela hash (M) em M_values:
    Para cada número de registros (num_records) em num_records_list:
        Cria uma instância de HashTable com o tamanho M.
        Chama a função populate_hash_table para preencher a tabela hash com registros aleatórios.
        Calcula o número total de colisões, contando os slots que não estão vazios e têm mais de um elemento.
        Inicializa variáveis para calcular os tempos médios de busca usando a tabela hash e busca linear, bem como o tamanho médio das chaves.
        Para cada registro em num_records:
            Executa um loop infinito para selecionar um slot aleatório não vazio.
            Escolhe aleatoriamente uma matrícula de um registro do slot selecionado.
            Marca o tempo de início da busca usando a tabela hash.
            Chama a função search da tabela hash para buscar o registro pela matrícula.
            Marca o tempo de término da busca usando a tabela hash.
            Calcula o tempo de busca em milissegundos e soma ao average_search_time_hash.
            Marca o tempo de início da busca linear.
            Chama a função linear_search para buscar o registro na lista records.
            Marca o tempo de término da busca linear.
            Calcula o tempo de busca linear em milissegundos e soma ao average_search_time_linear.
        Calcula os tempos médios de busca usando a tabela hash e busca linear dividindo os tempos acumulados pelo número de registros.
        Calcula o tamanho total das chaves somando os valores calculados pela função de hash para cada matrícula.
        Calcula o tamanho médio das chaves dividindo o tamanho total das chaves pelo número de registros.
        Armazena os resultados das colisões, tempos de busca e tamanho das chaves em listas correspondentes.

Passo 2: Função linear_search(records, key)
Recebe a lista de registros records e a chave de busca key como argumentos.
Para cada registro em records:
    Verifica se a matrícula do registro é igual à chave de busca.
    Se for igual, retorna o registro encontrado.
Se nenhum registro for encontrado, retorna None.


Passo 3: Cálculos e Armazenamento de Resultados
Os tempos médios de busca usando a tabela hash e busca linear são calculados dividindo os tempos acumulados pelo número de registros.
O tamanho total das chaves é calculado somando os valores calculados pela função de hash para cada matrícula de empregado.
O tamanho médio das chaves é calculado dividindo o tamanho total das chaves pelo número de registros.
Os resultados são armazenados em listas correspondentes (results_collisions, results_search_time_hash, results_search_time_linear, results_key_length).


Passo 4: Impressão dos Resultados
Os resultados dos Iterações são impressos em uma tabela formatada, exibindo o número de colisões, tempos médios de busca, diferença percentual entre os tempos de busca usando a tabela hash e busca linear, tamanho médio das chaves e contagem de 'append'.
O tempo total de execução é impresso, mostrando a duração em minutos e segundos.

Passo 5: Loop dos Iterações de Teste
Para cada Iteração de teste:
    Chamada da função run_iterations para calcular e armazenar resultados dos Iterações.
    Criação de uma tabela hash com o tamanho do primeiro Iteração e população com registros aleatórios.
    Armazenamento da contagem de 'append' por Iteração em append_count_per_iteration.
    Armazenamento dos resultados do Iteração atual em results.

    
Passo 6: Fim da Execução Principal
Finalização da execução principal do código.

Passo 7: Fim da Execução
Finalização da execução do código.
'''
