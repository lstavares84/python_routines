Passo 1: Preparação Inicial
Verifica se o nó de início (start) e o nó de destino (end) estão presentes na tabela de distâncias. Se não estiverem, imprime uma mensagem de erro e retorna None. (Linhas de código 4-9)


Passo 2: Inicialização das Variáveis
Inicializa as variáveis g e f para representar a distância acumulada e a distância total estimada entre as cidades. Essas variáveis são definidas como infinito para todos os nós, exceto o nó de início, que é definido como 0. (Linhas de código 12-19)
Inicializa a variável parents para armazenar os nós pais de cada nó durante o processo. Inicialmente, todos são definidos como None. (Linha de código 21)
Inicializa outras variáveis, como closed para armazenar caminhos já testados, open_set para armazenar caminhos a serem testados e algumas variáveis para rastrear os caminhos com a menor distância e o menor custo. (Linhas de código 23-29)


Passo 3: Loop Principal para Encontrar o Caminho Mais Curto
Entra em um loop enquanto houver caminhos a serem testados (open_set). (Linha de código 31)


Passo 4: Seleção do Próximo Nó a Ser Analisado
Seleciona o nó atual (current) com a menor distância total estimada (f) entre as cidades. Isso ajuda a explorar primeiro os caminhos mais promissores. (Linha de código 34-36)


Passo 5: Verificação de Destino
Verifica se o nó atual é o nó de destino (end). Se for, calcula o caminho completo do fim até o início usando os nós pais. (Linhas de código 38-57)


Passo 6: Cálculo das Distâncias e Custos ao Longo do Caminho
Calcula a distância total percorrida e o custo total ao longo do caminho. Isso envolve iterar sobre os nós no caminho e usar as informações da tabela de preços do diesel para calcular o custo. (Linhas de código 61-74)


Passo 7: Atualização dos Caminhos com Menores Distância e Custo
Verifica se o caminho atual tem a menor distância total ou o menor custo total até agora. Se sim, atualiza as variáveis correspondentes. (Linhas de código 77-84)


Passo 8: Impressão da Solução Parcial
Imprime a solução parcial para o usuário. Este passo está comentado no código original e pode ser descomentado se desejar exibir os resultados intermediários. (Linhas de código 85-98)


Passo 9: Saída do Loop
Sai do loop assim que o destino é encontrado. (Linha de código 100)


Passo 10: Impressão da Solução Final
Após a conclusão do loop principal, imprime a solução final, incluindo o caminho mais curto em termos de distância e custo, do nó de início ao nó de destino. (Linhas de código 102-114)


Passo 11: Execução das Combinações
O código principal executa combinações de nós de início e destino para calcular os caminhos mais curtos e custos para diferentes pares de cidades. (Linhas de código 116-133)


Passo 12: Verificação de Diferenças
Verifica se os caminhos mais curtos em termos de distância e custo são diferentes. Isso é feito para garantir que os resultados sejam consistentes. (Linha de código 135-139)
Este algoritmo de Dijkstra é usado para encontrar o caminho mais curto entre pares de cidades em um grafo ponderado, considerando as distâncias e os custos associados ao preço do diesel. Ele fornece informações detalhadas sobre os caminhos mais curtos e seus custos associados.