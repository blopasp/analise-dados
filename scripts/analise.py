import pandas as pd
import os

# variável
path_output = "output"
path_input_file = "input/Salaries.csv"

# modos de manipular arquivos em python
# "w" -> escrita
# "r" -> leitura
# "a" -> adicionar

# Criar função para alimentar respostas com arquivo txt
def gravar_respostas(path:str, filename:str, string:str, modo:str = "w", encoding:str = "utf-8"):
    # with abre uma conexão até q se encerre os comando dentro
    # do bloco with
    """
    Função utilizada para gravar texto em um arquivo txt
    Args:
        path (str): caminho do diretório
        filename (str): nome do arquivo
        string (str): texto a para ser criado
        modo (str, optional): modo de manipulacao do arquivo. Defaults to "w".
    """
    filename_path = os.path.join(path, filename)
    
    with open(filename_path, modo, encoding=encoding) as file:
        file.write(string)

# Padrão iniciar a solução e chamada das funcões dessa forma
# com if __name__ == "__main__":
if __name__ == "__main__":
    # Criando cabeçalho para o arquivo de respostas
    # \n -> quebra de linha
    string = "Respostas dos Exercícios\n\nAutor: Pedro\n\n"
    filename = "Respostas.txt"
    gravar_respostas(path_output, filename, string)

    # Carregar base de dados
    df = pd.read_csv(path_input_file, delimiter = ",")
    df.head()
    df.info()
    df.describe()
   
    # tratar base de dados
    # Ex1- Quais colunas tem nesta base?
    string = f"Resposta Ex1:\n"
    # gravando cabeçalho da questão
    gravar_respostas(path_output, filename, string, modo = "a")
    for col in df.columns:
        string = "\t"+col+"\n"
        # gravando coluna
        gravar_respostas(path_output, filename, string, modo = "a")
    gravar_respostas(path_output, filename, "\n", modo = "a")
        
    # 2


    # 3

    # 4

    # 5

    # 6

    # 7

    # 8

    # 9

    # 10