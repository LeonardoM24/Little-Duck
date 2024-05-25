# Leonardo Mojica Amezquita A0057196

# imports con lo necesario para 
# antlr4 y la gramatica
from antlr4 import *
from Grammar_duckLexer import Grammar_duckLexer
from Grammar_duckParser import Grammar_duckParser, semantica

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import DefaultErrorStrategy, BailErrorStrategy
from antlr4.error.Errors import ParseCancellationException

from Maquina import MaquinaVirtual as VM 


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException(f"Syntax error at line {line}, column {column}: {msg}")



# Funcion para leer el archivo
# regresa un dict con status que puede ser OK (todo salio bien)
# o ERROR, ademas regresa "content" que tiene el contenido del error
# o el contenido del archivo que se leyo con exito
def readFile(path):
    fileContent = "" # variable que guardara el contenido del archivo
    if not path.endswith('.txt'):
        return {"status":"ERROR", "content": "Must be a .txt file"}
    
    try:
        with open(path, "r") as file: # abrimos el archivo en modo lectura
            fileContent = file.read() # leemos el archivo para guardarlo en la variable
        return {"status":"OK", "content": fileContent}  # se leyo con exito
    except FileNotFoundError:
        return {"status":"ERROR", "content": "ERROR: File not found."} # no se encontro el archivo
    except Exception as e:
        return {"status":"ERROR", "content": "ERROR: " + str(e)} # cualquier otro error


if __name__ == '__main__': # programa main

    # Se pide un path con el archivo a analizar con la gramatica
    print("program path: ")
    input_path = input("> ")

    file = readFile(input_path) 

    if file["status"] == "ERROR":
        print(file["content"])
    elif file["status"] == "OK":    
        content = file["content"]
        lexer = Grammar_duckLexer(InputStream(content)) # pasamos el doc por el lexer
        stream = CommonTokenStream(lexer) # pasamos el resultado del lexer al stream
        parser = Grammar_duckParser(stream) # pasamos el stram al parser
        # Agrega tu ErrorListener personalizado al parser
        parser.removeErrorListeners() # Elimina los listeners de error predeterminados
        parser.addErrorListener(MyErrorListener()) # Agrega tu listener personalizado
        try:
            tree = parser.prog()
            #print(semantica.cuadruplos)
            #print(semantica.dirCTE)
            #print(tree.toStringTree(recog=parser))
                    # Creamos la maquina virtual
            mv = VM()
            mv.run(semantica.cuadruplos,semantica.dirCTE)
        except ParseCancellationException as e:
            print(e)


        

