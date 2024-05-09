# Leonardo Mojica Amezquita A0057196


import os # se usa os para revisar el path

# imports con lo necesario para 
# antlr4 y la gramatica
from antlr4 import *
from Grammar_duckLexer import Grammar_duckLexer
from Grammar_duckParser import Grammar_duckParser




# Funcion para leer el archivo
# regresa un dict con status que puede ser OK (todo salio bien)
# o ERROR, ademas regresa "content" que tiene el contenido del error
# o el contenido del archivo que se leyo con exito
def readFile(path):
    fileContent = "" # variable que guardara el contenido del archivo
    try:
        with open(path, "r") as file: # abrimos el archivo en modo lectura
            fileContent = file.read() # leemos el archivo para guardarlo en la variable
        return {"status":"OK", "content": fileContent} # se leyo con exito
    except FileNotFoundError:
        return {"status":"ERROR", "content": "ERROR: File not found."} # no se encontro el archivo
    except Exception as e:
        return {"status":"ERROR", "content": "ERROR: " + str(e)} # cualquier otro error


if __name__ == '__main__': # programa main

    # Se pide un path con el archivo a analizar con la gramatica
    print("program path: ")
    input_path = input("> ")

    file = readFile(input_path) 

    if file["status"] == "OK":
        print(file)
    else:
        print(file["content"])
    
    # lexer = Grammar_duckLexer(InputStream(file)) # pasamos el doc por el lexer
    # stream = CommonTokenStream(lexer) # pasamos el resultado del lexer al stream
    # parser = Grammar_duckParser(stream) # pasamos el stram al parser

    # tree = parser.prog()

    # print(tree.toStringTree(recog=parser))


