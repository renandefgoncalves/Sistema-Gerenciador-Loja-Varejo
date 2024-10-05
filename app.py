import datetime

class Produto:
    # Classe que define os produtos com atributos básicos
    def __init__(self, nome, codigo, categoria, quantidade_estoque, preco, descricao, fornecedor):
        self.nome = nome.lower()  # Converte o nome para minúsculas para garantir a unicidade
        self.codigo = codigo
        self.categoria = categoria
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        self.descricao = descricao
        self.fornecedor = fornecedor

    # Método para adicionar quantidade ao estoque
    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    # Método para remover quantidade do estoque, com verificação se a quantidade é suficiente
    def remover_estoque(self, quantidade):
        if quantidade > self.quantidade_estoque:
            raise Exception("Quantidade em estoque insuficiente!")
        self.quantidade_estoque -= quantidade

    # Exibe todos os detalhes do produto
    def exibir_detalhes(self):
        print(f"Produto: {self.nome.capitalize()}, Código: {self.codigo}, Categoria: {self.categoria}, "
              f"Estoque: {self.quantidade_estoque}, Preço: {self.preco}, "
              f"Descrição: {self.descricao}, Fornecedor: {self.fornecedor}")

    # Exibe apenas o nome e a quantidade em estoque do produto
    def exibir_estoque(self):
        print(f"Produto: {self.nome.capitalize()}, Estoque: {self.quantidade_estoque}")


class Venda:
    # Classe para gerenciar o registro das vendas
    def __init__(self, produto, quantidade, desconto=0):
        self.produto = produto
        self.quantidade = quantidade
        self.data = datetime.datetime.now()  # Armazena a data e hora da venda
        self.desconto = desconto
        self.valor_total = self.calcular_valor_total()

    # Método para calcular o valor total da venda com desconto
    def calcular_valor_total(self):
        return (self.produto.preco * self.quantidade) * (1 - self.desconto / 100)

    # Exibe os detalhes da venda
    def exibir_recibo(self):
        print(f"\n=== Recibo de Venda ===\nProduto: {self.produto.nome.capitalize()}\n"
              f"Quantidade: {self.quantidade}\nDesconto: {self.desconto}%\n"
              f"Valor Total: R${self.valor_total:.2f}\nData: {self.data.strftime('%d/%m/%Y %H:%M:%S')}\n")


class Estoque:
    # Classe que gerencia o estoque de produtos e as vendas
    def __init__(self):
        self.produtos = []
        self.vendas = []
        self.historico_movimentacoes = []

    # Adiciona um novo produto ao estoque, verificando se o código é único
    def adicionar_produto(self, produto):
        if self.verificar_codigo_existente(produto.codigo):
            print(f"Erro: Já existe um produto com o código {produto.codigo}. Cadastro não realizado.")
        elif self.verificar_nome_existente(produto.nome):
            print(f"Erro: Já existe um produto com o nome '{produto.nome}'. Cadastro não realizado.")
        else:
            self.produtos.append(produto)
            print(f"Produto {produto.nome.capitalize()} adicionado com sucesso.")

    # Verifica se o código do produto já existe no estoque
    def verificar_codigo_existente(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return True
        return False

    # Verifica se o nome do produto já existe no estoque, ignorando diferenças de maiúsculas/minúsculas
    def verificar_nome_existente(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                return True
        return False

    # Função para registrar a venda e atualizar o estoque
    def registrar_venda(self, codigo, quantidade, desconto=0):
        produto = self.obter_produto_por_codigo(codigo)
        if produto is None:
            print("Produto não encontrado!")
            return
        try:
            produto.remover_estoque(quantidade)
            venda = Venda(produto, quantidade, desconto)
            self.vendas.append(venda)
            self.historico_movimentacoes.append(
                f"Venda: {quantidade} unidades de {produto.nome.capitalize()} - Estoque atualizado para {produto.quantidade_estoque}.")
            venda.exibir_recibo()
        except Exception as e:
            print(e)

    # Função para obter um produto pelo código
    def obter_produto_por_codigo(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    # Consulta todos os produtos com todos os detalhes
    def consultar_produtos(self):
        if not self.produtos:  # Verifica se há produtos cadastrados
            print("Nenhum produto cadastrado.")
        for produto in self.produtos:
            produto.exibir_detalhes()

    # Consulta o estoque mostrando apenas nome e quantidade em estoque
    def consultar_estoque(self):
        if not self.produtos:  # Verifica se há produtos cadastrados
            print("Nenhum produto cadastrado.")
        for produto in self.produtos:
            produto.exibir_estoque()

    # Exibe o relatório de vendas
    def relatorio_vendas(self):
        if not self.vendas:
            print("Nenhuma venda registrada.")
        else:
            print("\n=== Relatório de Vendas ===")
            for venda in self.vendas:
                print(f"Produto: {venda.produto.nome.capitalize()}, Quantidade: {venda.quantidade}, "
                      f"Desconto: {venda.desconto}%, Valor Total: R${venda.valor_total:.2f}, "
                      f"Data: {venda.data.strftime('%d/%m/%Y %H:%M:%S')}")

    # Exibe o histórico de movimentações de estoque
    def historico_movimentacoes_estoque(self):
        if not self.historico_movimentacoes:
            print("Nenhuma movimentação registrada.")
        else:
            print("\n=== Histórico de Movimentações ===")
            for movimentacao in self.historico_movimentacoes:
                print(movimentacao)


def cadastrar_produto(estoque):
    # Função para cadastrar um novo produto com tratamento de exceções e validação de entradas
    while True:
        nome = input("Digite o nome do produto: ").strip().lower()  # Converte o nome para minúsculas
        if nome:  # Verifica se o nome não está vazio
            break
        print("O nome do produto não pode estar vazio.")

    # Tratamento para garantir que o código é um número inteiro e único
    while True:
        try:
            codigo = input("Digite o código do produto: ").strip()
            if not codigo.isdigit() or not codigo:
                print("O código do produto deve ser um número inteiro e não pode estar vazio.")
                continue
            codigo = int(codigo)
            if not estoque.verificar_codigo_existente(codigo):
                break
            else:
                print("Código já cadastrado. Insira um código único.")
        except ValueError:
            print("Código inválido! Digite apenas números inteiros.")

    # Tratamento para garantir que a categoria não está vazia
    while True:
        categoria = input("Digite a categoria do produto: ").strip()
        if categoria:
            break
        print("A categoria do produto não pode estar vazia.")

    # Tratamento para garantir que a quantidade é um número inteiro
    while True:
        try:
            quantidade = input("Digite a quantidade em estoque: ").strip()
            if not quantidade:
                print("A quantidade não pode estar vazia.")
                continue
            quantidade_estoque = int(quantidade)
            break
        except ValueError:
            print("Quantidade inválida! Digite apenas números inteiros.")

    # Tratamento para garantir que o preço é um número decimal
    while True:
        try:
            preco = input("Digite o preço do produto: ").strip()
            if not preco:
                print("O preço do produto não pode estar vazio.")
                continue
            preco = float(preco)
            break
        except ValueError:
            print("Preço inválido! Digite um número válido.")

    # Tratamento para garantir que a descrição não está vazia
    while True:
        descricao = input("Digite a descrição do produto: ").strip()
        if descricao:
            break
        print("A descrição do produto não pode estar vazia.")

    # Tratamento para garantir que o fornecedor não está vazio
    while True:
        fornecedor = input("Digite o fornecedor do produto: ").strip()
        if fornecedor:
            break
        print("O fornecedor do produto não pode estar vazio.")

    # Retorna um objeto Produto com os dados fornecidos
    return Produto(nome, codigo, categoria, quantidade_estoque, preco, descricao, fornecedor)


def menu():
    # Função principal que exibe o menu do sistema de gestão de estoque
    estoque = Estoque()  # Instancia o objeto Estoque
    while True:
        # Exibe o menu de opções
        print('''
███████╗░██████╗████████╗░█████╗░░██████╗░██╗░░░██╗███████╗
██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗██║░░░██║██╔════╝
█████╗░░╚█████╗░░░░██║░░░██║░░██║██║██╗██║██║░░░██║█████╗░░
██╔══╝░░░╚═══██╗░░░██║░░░██║░░██║╚██████╔╝██║░░░██║██╔══╝░░
███████╗██████╔╝░░░██║░░░╚█████╔╝░╚═██╔═╝░╚██████╔╝███████╗
╚══════╝╚═════╝░░░░╚═╝░░░░╚════╝░░░░╚═╝░░░░╚═════╝░╚══════╝\n''')
        print("1. Cadastrar Produto")
        print("2. Registrar Venda")
        print("3. Consultar Produtos")
        print("4. Consultar Estoque")
        print("5. Relatório de Vendas")
        print("6. Histórico de Movimentações")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        # Opção para cadastrar um produto
        if opcao == '1':
            produto = cadastrar_produto(estoque)  # Chama a função de cadastro de produto, passando o estoque
            estoque.adicionar_produto(produto)  # Adiciona o produto ao estoque
        # Opção para registrar uma venda
        elif opcao == '2':
            codigo = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite a quantidade vendida: "))
            desconto = float(input("Digite o percentual de desconto (0 se não houver): "))
            estoque.registrar_venda(codigo, quantidade, desconto)
        # Opção para consultar todos os produtos com detalhes
        elif opcao == '3':
            estoque.consultar_produtos()  # Chama a função de consulta de produtos
        # Opção para consultar o estoque (nome e quantidade)
        elif opcao == '4':
            estoque.consultar_estoque()  # Chama a função de consulta de estoque
        # Opção para exibir o relatório de vendas
        elif opcao == '5':
            estoque.relatorio_vendas()  # Exibe o relatório de vendas
        # Opção para exibir o histórico de movimentações
        elif opcao == '6':
            estoque.historico_movimentacoes_estoque()  # Exibe o histórico de movimentações
        # Opção para sair do sistema
        elif opcao == '7':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, por favor escolha uma opção válida.")


# Inicia o sistema chamando o menu
menu()
