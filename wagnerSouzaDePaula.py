"""
Faculdade Senac/RS Porto Alegre
CURSO: Análise e Desenvolvimento de Sistemas
DISCIPLINA: Algoritmos e Programação I
PROFESSOR: Ivonei da Silva Marques
ALUNO: Wagner Souza de Paula
"""

"""
Tarefa 3 =-=-=-=-=-=-=-
Competências avaliadas:
> Desenvolver uma solução viável para a atividade
> Saber utilizar classes e métodos
> Saber manipular arquivo texto (leitura e gravação)
"""

# Classe Imobiliária:
"""
Crie uma classe chamada Imobiliaria
  Esta classe deverá ter os seguintes atributos:
  - nome_imobiliaria (string)
  - telefones (lista) >>> (Opcional para desenvolvimento)
  - lst_imoveis_alugar = (lista) (objetos da classe Imovel) (este atributo deve ser privado)
"""

# Classe Imóvel:
"""
Crie a classe Imovel
  Esta classe deverá ter os seguintes atributos:
  - tipo (string) ("CASA" ou "APARTAMENTO")
  - endereco (string)
  - alugado (bool) True:Alugado  False:Disponível
"""

# Menu:
"""
Controle sua aplicação com o seguinte menu:
MENU
0- Finalizar
1- Adicionar Imobiliaria
2- Adicionar Imóvel
3- Relatório de Imobiliárias e seus imóveis
4- Alterar status Alugado/Disponível
Escolha:
"""

# Infos:
"""
Seu código deverá armazenar as informações da imobiliária (instâncias) na lista: lst_imobiliarias
Ao executar seu programa você deverá chamar uma rotina que leia o arquivo "imobiliarias.txt" e
  atualize a lista lst_imobiliarias com os dados lidos deste arquivo.
Ao finalizar seu programa, pelo menu, você deverá salvar os dados da lista lst_imobiliarias para poderem
  ser utilizados novamente.
"""

class Imobiliaria():
    def __init__(self, nome, telefone):
        self.__nome_imobiliaria = nome
        self.__telefones = telefone
        self.__lst_imoveis_alugar = []

    def getNomeImob(self):
        return self.__nome_imobiliaria

    def getTelefone(self):
        return self.__telefones

    def getLstImoveisAlugar(self):
        return self.__lst_imoveis_alugar

    def setLstImoveisAlugar(self,imovel):
        self.__lst_imoveis_alugar.append(imovel)

    def imprimeListaImoveis(self):
        print("\033[1;96mCÓDIGO | TIPO         | ENDEREÇO                       | DISPONIBILIDADE\033[0;0m")
        for i, imoveis in enumerate(self.__lst_imoveis_alugar):
            print(f"{i}      | {imoveis.getTipo().ljust(12)} | {imoveis.getEndereco().ljust(30)} | {imoveis.disponibilidade()}")

    def __str__(self):
        return f"{self.getNomeImob()} | {self.getTelefone()}"

class Imovel():
    def __init__(self, tipo, endereco, alugado):
        self.__tipo = tipo
        self.__endereco = endereco
        self.__alugado = alugado

    def getTipo(self):
        return self.__tipo

    def getEndereco(self):
        return self.__endereco

    def setAlugado(self, alugado):
        self.__alugado = alugado

    def getAlugado(self):
        return self.__alugado #True = Alugado | False = Disponível para locação

    def disponibilidade(self):
        if self.__alugado: return "ALUGADO"
        else: return "DISPONIVEL"

    def __str__(self):
        return f"{self.getTipo()} | {self.getEndereco()} | {self.disponibilidade()}"

menu = """
    ==================================
    | Programa de Gestão imobiliária |
    ==================================
        MENU
        0- Finalizar
        1- Adicionar Imobiliaria
        2- Adicionar Imóvel
        3- Relatório de Imobiliárias e seus imóveis
        4- Alterar status Alugado/Disponível
        Escolha: """

def adicionaImob():
    novaImob = str(input("Informe o nome da imobiliária: ").upper())
    lstTel = []
    lstTel.append(str(input(f"Informe o telefone fixo da {novaImob}: ").upper()))
    lstTel.append(str(input(f"informe outro telefone da {novaImob}: ").upper()))
    imobOb = Imobiliaria(novaImob,lstTel)
    if validaImobiliaria(imobOb):
        lst_imobiliarias.append(imobOb)
        input("Imobiliária cadastrada com sucesso!!!")
    else: input("Imobiliária informada já possui cadastro!!!")

def adicionaImovel():
    nomeImob = str(input("Informe o nome da imobiliária: ").upper())
    for imobiliaria in lst_imobiliarias:
        if imobiliaria.getNomeImob() == nomeImob:
            tipo = str(input("Informe o tipo do imóvel [CASA] ou [APARTAMENTO]: ").upper())
            if tipo == "CASA" or tipo == "APARTAMENTO":
                endereco = str(input(f"Informe o endereço do imóvel do tipo {tipo}: ").replace(";", ",").upper())
                objetoImovel = Imovel(tipo,endereco,False)
                imobiliaria.setLstImoveisAlugar(objetoImovel)
                input("Imóvel cadastrado com sucesso!!!")
            else:
                input("Você informou o tipo errado, deves ser informado apenas CASA ou APARTAMENTO")

def relatorio():
    print("---RELATÓRIO DE IMÓVEIS POR IMOBILIÁRIA---")
    for imobiliaria in lst_imobiliarias:
        print(f"IMÓVEIS DA \033[1;34mIMOBILIÁRIA {imobiliaria}\033[0;0m")
        print(imobiliaria.imprimeListaImoveis())
    input("Relatório Gerado com Sucesso!!!")

def alugaDesocupa():
    selecao = input("""
    [1] para Alugar ou 
    [2] para desocupar
    Escolha: """)
    nomeImob = input("Informe o nome da imobiliária: ").upper()
    if selecao == '1':
        for imobiliaria in lst_imobiliarias:
            if imobiliaria.getNomeImob() == nomeImob:
                print(f"IMÓVEIS DA IMOBILIÁRIA {imobiliaria}")
                print(imobiliaria.imprimeListaImoveis())
                endereco = input("Informe o endereco do imóvel para ALUGAR: ").upper()
                for imovel in imobiliaria.getLstImoveisAlugar():
                    if imovel.getEndereco() == endereco:
                        if not imovel.getAlugado():
                            imovel.setAlugado(True)
                            input("Imóvel ALUGADO com sucesso!")
                        else:
                            input("Este imóvel não pode ser alugado pois NÃO ESTÁ DISPONÍVEL.")
    if selecao == '2':
        for imobiliaria in lst_imobiliarias:
            if imobiliaria.getNomeImob() == nomeImob:
                print(f"IMÓVEIS DA IMOBILIÁRIA {imobiliaria}")
                print(imobiliaria.imprimeListaImoveis())
                endereco = input("Informe o endereco do imóvel PARA DESOCUPAR: ").upper()
                for imovel in imobiliaria.getLstImoveisAlugar():
                    if imovel.getEndereco() == endereco:
                        if imovel.getAlugado():
                            imovel.setAlugado(False)
                            input("Imóvel DESOCUPADO com sucesso!")
                        else:
                            input("Este imóvel não pode ser DESOCUPADO pois NÃO ESTÁ ALUGADO.")

def clearScreen():
    print("\n"*25)

def validaImobiliaria(imobTmp): #APENAS VALIDEI O NOME DAS IMOBILIÁRIAS PARA NAO FICAREM REPETIDAS (PRINCIPALMENTE QUANDO FOR IMPORTAR OS DADOS DO ARQUIVO TXT)
    if lst_imobiliarias:
        for imobiliaria in lst_imobiliarias:
            if imobiliaria.getNomeImob() == imobTmp.getNomeImob():
                return False
    return True

def finalizar():
    arquivo = open("imobiliarias.txt","w") # USEI WRITE ('W' PORQUE SE EU USASSE APPEND ('A'), IRIA DUPLICAR OS DADOS CADASTRADOS (AO FINALIZAR O PROGRAMA, MANTERIA OS DADOS DO ARQUIVO ORIGINAL E ACRESCENTARIA O QUE FOI IMPORTADO MAIS OS DADOS LANÇADOS).
    for imobiliaria in lst_imobiliarias:
        for imovel in imobiliaria.getLstImoveisAlugar():
            imobiliariaTmp = imobiliaria.getNomeImob()
            telefoneTmp = imobiliaria.getTelefone()
            tipoTmp = imovel.getTipo()
            enderecoTmp = imovel.getEndereco()
            disponivelTmp = imovel.disponibilidade()
            arquivo.write(str(imobiliariaTmp) +";"+ str(telefoneTmp)+";"+str(tipoTmp)+";"+str(enderecoTmp)+";"+str(disponivelTmp)+"\n")
    arquivo.close()

def main():
    selecao = input(menu)
    if selecao == '0':
        finalizar()
        print("Exportando dados do sistema...")
        print("Dados exportados com sucesso!!!")
        print("Finalizando programa...")
        print("Programa finalizado!!!")
        exit()
    if selecao == '1': adicionaImob()
    if selecao == '2': adicionaImovel()
    if selecao == '3': relatorio()
    if selecao == '4': alugaDesocupa()
    clearScreen()
    main()

lst_imobiliarias = []

arquivo = open("imobiliarias.txt","r")
for linha in arquivo:
    lista = linha.strip().split(";")
    imobTmp = Imobiliaria(lista[0],lista[1])
    if validaImobiliaria(imobTmp):
        lst_imobiliarias.append(imobTmp)
    if str(lista[4]) == 'ALUGADO':
        disponivelTmp = True
    elif str(lista[4]) == 'DISPONIVEL':
        disponivelTmp = False
    imovelTmp = Imovel(lista[2], lista[3], disponivelTmp)
    for imobiliaria in lst_imobiliarias:
        if imobiliaria.getNomeImob() == lista[0]:
            imobiliaria.setLstImoveisAlugar(imovelTmp)
arquivo.close()

main()