print("Bem vindo a loja, cadastre seu produto")

nome = input("Digite seu nome ")
senha = input("Crie uma senha ")



produtos = [
    {"titulo": "222", "preco": 10},
]

def cadastro():
    cadastrarProduto()
    escolha = input("Deseja cadastrar algum produto ? (SIM ou NAO) ")
    escolha.upper()
    if(escolha == "SIM"):
        cadastro
        while (escolha == "SIM"):
               cadastro
    elif(escolha == "NAO"):
        chamarProcura()
        
    else:
        print("por favor insira uma opção válida")
    
     

def cadastro():
    t = input("Qual o nome do produto?")
    p = input("Qual o valor desse produto ?")
    cadastrarProduto(t,p)

def cadastrarProduto(titulo, preco):
    global produtos
    
    titulo = str(titulo)
    preco = int(preco)
        
    produtos += [{"titulo": titulo, "preco": preco}]
    
   

    

cadastrarProduto("mateus", 5)
cadastrarProduto("jonas", 10)

def procurar(procura):
    global produtos
    procura = procura.upper()
    
    i = 0 
    encontrado = False
    
    while i < len(produtos):
        procurado = produtos[i]["titulo"].upper()
        preco = produtos[i]["preco"]
        
        if procura == procurado:
            print(f"{procurado} encontrado!")
            print(f"Preço : {preco}")
            encontrado = True
            break
        
        
        i += 1
    
    if not encontrado:
        print("Produto não encontrado.")
        
def chamarProcura():
    chamado = input("Digite o produto que cadastrou: ")
    procurar(chamado)

cadastro()

chamarProcura()