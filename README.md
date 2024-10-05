# Sistema de Gestão de Estoque e Vendas

Este projeto é um sistema de gestão de estoque e vendas, implementado em Python. Ele permite o cadastro de produtos, a realização de vendas com descontos e atualizações automáticas no estoque, além da geração de recibos e relatórios de vendas e movimentações.

## Funcionalidades

### 1. Cadastro de Produto
Permite o cadastro de produtos no estoque com os seguintes atributos:
- Nome
- Código
- Categoria
- Quantidade em estoque
- Preço
- Descrição
- Fornecedor

### 2. Registro de Venda
Ao realizar uma venda, o sistema:
- Verifica a existência do produto e a disponibilidade no estoque.
- Atualiza automaticamente a quantidade no estoque.
- Permite aplicar descontos ao valor total.
- Gera um recibo contendo o nome do produto, quantidade vendida, desconto aplicado e o valor total.

### 3. Atualização Automática do Estoque
Cada vez que uma venda é realizada, a quantidade em estoque do produto é reduzida automaticamente, conforme a quantidade vendida.

### 4. Emissão de Recibo
Após cada venda, o sistema emite um recibo com os seguintes dados:
- Nome do produto
- Quantidade vendida
- Percentual de desconto aplicado
- Valor total (após desconto)
- Data e hora da venda

### 5. Descontos e Promoções
Permite aplicar descontos ao realizar a venda de um produto. O desconto é informado como um percentual do valor total.

### 6. Relatório de Vendas
Gera um relatório detalhado de todas as vendas realizadas, incluindo:
- Produto vendido
- Quantidade
- Valor total
- Desconto aplicado
- Data e hora da venda

### 7. Relatório de Estoque
Exibe a quantidade atual de todos os produtos no estoque.

### 8. Histórico de Movimentações
Registra e exibe todas as movimentações de estoque, como adições e remoções após vendas, com detalhes de quais produtos foram alterados e em que quantidade.

## Estrutura das Classes

### Classe 'Produto'
Representa um produto no estoque, contendo atributos como:
- 'nome': Nome do produto.
- 'codigo': Código único de identificação do produto.
- 'categoria': Categoria do produto.
- 'quantidade_estoque': Quantidade disponível no estoque.
- 'preco': Preço unitário do produto.
- 'descricao': Breve descrição do produto.
- 'fornecedor': Nome do fornecedor do produto.

### Métodos da Classe 'Produto'
- 'adicionar_estoque(quantidade)': Adiciona uma quantidade ao estoque do produto.
- 'remover_estoque(quantidade)': Remove uma quantidade do estoque, com verificação de disponibilidade.
- 'exibir_detalhes()': Exibe todos os detalhes do produto.
- 'exibir_estoque()': Exibe o nome e a quantidade em estoque do produto.

### Classe 'Venda'
Representa uma venda realizada no sistema, com os seguintes atributos:
- 'produto': Produto vendido.
- 'quantidade': Quantidade do produto vendida.
- 'desconto': Percentual de desconto aplicado.
- 'valor_total': Valor total da venda após o desconto.
- 'data': Data e hora da venda.

### Métodos da Classe 'Venda'
- 'calcular_valor_total()': Calcula o valor total da venda com base no preço e desconto.
- 'exibir_recibo()': Exibe o recibo com os detalhes da venda.

### Classe 'Estoque'
Gerencia o estoque e as vendas, com os seguintes métodos:
- 'adicionar_produto(produto)': Adiciona um novo produto ao estoque, verificando se o código é único.
- 'registrar_venda(codigo, quantidade, desconto)': Registra uma venda, atualiza o estoque e gera um recibo.
- 'consultar_produtos()': Exibe todos os produtos cadastrados no estoque com seus detalhes.
- 'consultar_estoque()': Exibe a quantidade disponível de cada produto.
- 'relatorio_vendas()': Gera um relatório com todas as vendas realizadas.
- 'historico_movimentacoes_estoque()': Exibe o histórico de movimentações de estoque, como adições e vendas.

## Como Usar

### 1. Clonando o Repositório
Primeiro, clone o repositório para sua máquina local:
'''bash'''
git clone https://github.com/seu-usuario/nome-do-repositorio.git
