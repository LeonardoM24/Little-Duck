class CuboSemantico:
    def __init__(self) -> None:
        # =============================================
        # ==============Cubo semantico=================
        # =============================================
        # 0 = float, 1 = int
        # 0 = + , 1 = -, 2 = *, 3 = /, 4 = <, 5 = >, 6 = !=, 7 = =
        # ejemplo cubo[0][1][2] = float, int, multiplicacion
        self.cuboSemantico = [[],[],[]]
        # Inicializar el cubo semántico
        self.cuboSemantico = [[[0 for _ in range(8)] for _ in range(2)] for _ in range(2)]

        # Configurar las reglas
        # Si ambos operandos son int, el resultado es int para todas las operaciones
        for op in range(4):
            self.cuboSemantico[1][1][op] = 1

        # Si el operador es 4, 5 o 6, el resultado es int sin importar los operandos
        for op in range(4, 7):
            self.cuboSemantico[0][0][op] = 1
            self.cuboSemantico[0][1][op] = 1
            self.cuboSemantico[1][0][op] = 1
            self.cuboSemantico[1][1][op] = 1

        # agregar la operacion 7
        self.cuboSemantico[0][0][7] = 0  # float = float guarda 0
        self.cuboSemantico[1][1][7] = 1  # int = int guarda 1
        self.cuboSemantico[0][1][7] = 0  # float = int guarda 0
        self.cuboSemantico[1][0][7] = 1  # int = float guarda 1
        # =============================================
        # ==============Cubo semantico=================
        # =============================================

class DirectorioFunciones():
    def __init__(self) -> None:
        # ==========Directorio de funciones============
        self.dirFunc = {}

        self.currFunc = "" # funcion actual
        self.tempIDS = []  # arreglo de memoria de lista de vars
        self.currID = ""   # id actual
        self.currType = "" # tipo de la variable actual
    
    # checar si la funcion ya existe, true = ya existe, false = nuevo
    def checkFunc(self, id):
        if self.dirFunc.get(id) != None: # variable ya existe
            return True
        return False
    
    # checar si la variable ya existe, true = ya existe, false = nuevo
    def checkVar(self, id, func):
        #checar si existe la funcion
        if not self.checkFunc(func): # no existe la funcion
            return True # la funcion no existe
        if self.dirFunc[func][1].get(id) != None: # variable ya existe
            return True
        return False

    def addFunc(self, id, type):
        if self.checkFunc(id): # funcion ya existe
            raise ValueError(f"Function {id} already declared")      
        self.dirFunc[id] = [type,{}] # agregamos nuestra funcion al dir de funciones y creamos el dir de variables

    def addVar(self, id, type, func):
        if self.checkVar(id,func): # variable ya existe
            raise ValueError(f"Variable {id} already declared in this scope. function name: {func}")
        self.dirFunc[func][1][id] =[type]
    
    def addListVar(self, listIDS, type, func):
        for id in listIDS:
            try:
                self.addVar(id, type, func)
            except ValueError as e:
                raise e

    def addVarTempList(self, id):
        self.tempIDS.append(id)
    
    def delDV(self, func): # borrar/limpiar del directorio de variables de la funcion
        self.dirFunc[func][1] = {}
    
    def delFunc(self, id):
        self.dirFunc.pop(id) # borrar la funcion (ya no la usamos)