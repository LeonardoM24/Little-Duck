
class Semantica:
    def __init__(self) -> None:
        # =============================================
        # ==============Cubo semantico=================
        # =============================================
        # 0 = float, 1 = int, 2 = string
        # 0 = + , 1 = -, 2 = *, 3 = /, 4 = <, 5 = >, 6 = !=, 7 = =
        # ejemplo cubo[0][1][2] = float, int, multiplicacion
        self.tiposTag = ["float", "int", "string"]
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

        # ==========Directorio de funciones============
        self.dirFunc = {}
        # dirFunc = { "func" : ["type", {"var1":["type", memoria]}]}
        self.progName = ""


        self.currFunc = "" # funcion actual
        self.tempIDS = []  # arreglo de memoria de lista de vars
        self.currID = ""   # id actual
        self.currType = "" # tipo de la variable actual

        # ==========direcciones de memoria ===========
        self.rangoMGlobalI = 6499; self.rangoMGlobalF = 12999  # valor maximo variable global
        self.rangoMLocalI  = 15999; self.rangoMLocalF = 18999 # valor maximo variable local
        self.rangoMTempI   = 32499; self.rangoMTempF = 45999 # valor maximo variable temporal
        self.rangoMCteI    = 55999; self.rangoMCteF = 65999; self.rangoMCteS = 75999 # valor maximo para constantes

        # limite inferior
        self.minMGlobalI = 1000; self.minMGlobalF = 6500
        self.minMLocalI  = 13000; self.minMLocalF = 16000
        self.minMTempI   = 19000; self.minMTempF = 29000
        self.minMCteI    = 46000; self.minMCteF = 56000; self.currMCteS = 66000

        # contador para asignar memoria
        self.currMGlobalI = 1000; self.currMGlobalF = 6500
        self.currMLocalI  = 13000; self.currMLocalF = 16000
        self.currMTempI   = 19000; self.currMTempF = 29000
        self.currMCteI    = 46000; self.currMCteF = 56000; self.currMCteS = 66000

        # ==========Pilas, operaciones============
        self.dirCTE         = {} # para guardar constante y direccion de memoria 
        self.currCuadruplo  = 0 # indice del siguiente cuadruplo
        self.cuadruplos     = [] # arreglo de cuadruplos
        self.pilaTipos      = [] # pila con los tipos
        self.pilaSaltos     = [] # pila de los saltos
        self.pilaVariables  = [] # pila con las direcciones de memoria de varibles
        self.pilaOperadores = [] # pila con operadores

    
    # checar si la funcion ya existe, true = ya existe, false = nuevo
    def checkFunc(self, id):
        if self.dirFunc.get(id) != None: # variable ya existe
            return True
        return False
    
    # checar si la variable ya existe, true = ya existe, false = nuevo
    def checkVar(self, id, func = None):
        if func == None:
            func = self.currFunc
        #checar si existe la funcion
        if not self.checkFunc(func): # no existe la funcion
            return True # la funcion no existe
        if self.dirFunc[func][1].get(id) != None: # variable ya existe
            return True
        return False

    # checar si una constante ya existe en nuestro dirvar
    def checkCTE(self, cte):
        if self.dirCTE.get(cte) != None:
            return True
        return False

    def addFunc(self, id, type):
        if self.checkFunc(id): # funcion ya existe
            raise ValueError(f"Function {id} already declared")      
        self.dirFunc[id] = [type,{}] # agregamos nuestra funcion al dir de funciones y creamos el dir de variables

    def addVar(self, id, type, func):
        if self.checkVar(id,func): # variable ya existe
            raise ValueError(f"Variable {id} already declared in this scope. function name: {func}")
        
        if type == "int":
            t = 1
        elif type == "float":
            t = 0
        
        # revisamos si es una variable global o local
        if self.dirFunc[func][0] == "program": # estamos en el directorio del programa
            # checamos si tenemos espacio
            if t == 1: # int
                if self.currMGlobalI > self.rangoMGlobalI: # ya llenamos la memoria
                    raise ValueError(f"cant save {id}. Out of memory")
                self.dirFunc[func][1][id] = [t,self.currMGlobalI]
                self.currMGlobalI += 1 # actualizamos el contador de memoria
            elif t == 0: # float
                if self.currMGlobalF > self.rangoMGlobalF: # ya llenamos la memoria
                    raise ValueError(f"cant save {id}. Out of memory")
                # dar dirección de memoria de variable global flotante
                self.dirFunc[func][1][id] = [t,self.currMGlobalF]
                self.currMGlobalF += 1 # actualizamos el contador de memoria
        else: # estamos en una función, agregando variables locales
            #checar si tenemos espacio
            if t == 1:
                if self.currMLocalI > self.rangoMLocalI:
                    raise ValueError(f"cant save {id}. Out of memory")
                self.dirFunc[func][1][id] = [t, self.currMLocalI]
                self.currMLocalI += 1 # actualizamos el contador de memoria
            elif t == 0:
                if self.currMLocalF > self.rangoMLocalF:
                    raise ValueError(f"cant save {id}. Out of memory")
                # dar dirección de memoria de variable local        
                self.dirFunc[func][1][id] = [t, self.currMLocalF]
                self.currMLocalF += 1 # actualizamos el contador de memoria

    
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

    def addPilaVar(self, id, cte = False , func = None, tipo = None): # añadir a la pila de variable
        if func == None:
            func = self.currFunc
        
        if not cte and not self.checkVar(id,func): # la variable ya existe
            raise ValueError(f"variable {id} not declared")

        # sacar la dirección de memoria de esa variable  
        dirM = self.getDireccionMemoria(id,cte,func)
        if tipo == None:
            tipo = self.getTipo(id,cte,func) # sacamos el tipo
        self.pilaVariables.append(dirM) # lo ponemos a la pila de var
        self.pilaTipos.append(tipo) # ponemos el tipo
    
    def getTipo(self, id, cte = False,func = None):
        if func == None:
            func = self.currFunc
        
        if not cte: # variable
            tipo = self.dirFunc[func][1][id][0]
        else: # es una constante
            m = self.getDireccionMemoria(id, cte=True)
            if m in range(self.minMCteI, self.rangoMCteI + 1): # es entero
                tipo = 1
            elif m in range(self.minMCteF, self.rangoMCteF + 1):
                tipo = 0
            else: # m in rantge(self.minMCteS, self.rangeMCteS + 1): # string
                tipo = 2
        return tipo

    def addPilaOp(self, op):
        # +  --> 0
        # -  --> 1
        # *  --> 2
        # /  --> 3
        # <  --> 4
        # >  --> 5
        # != --> 6
        # =  --> 7
        # goTo -> 8
        # goToF -> 9
        # goToT -> 10
        # print -> 11
        self.pilaOperadores.append(op)
    
    def addCuadruplo(self, op, OpI = None, OpD = None, TI = None, TD = None):

        if(op == 12): # EOF
            cuadruplo = [op,None,None,None]
            pass
        # revisar que tipo me da haciendo uso de mi cuadro semantico
        elif (op == 7): # cuadruplo de asignación.
            cuadruplo = [op, OpD,None,OpI]
        elif op in [0,1,2,3,4,5,6] : # operaciones que generan un resultado temporal
            
            # revisar el type del resultado temporal
            tipoT = self.cuboSemantico[TI][TD][op]

            if tipoT == -1:
                raise ValueError(f"mismatch type, cant do {op} to type {self.tiposTag[TI]} and {self.tiposTag[TD]} ")
            elif tipoT == 0:   # float
                # revisar si hay espacio en memoria temporal
                if self.currMLocalF > self.rangoMTempF:
                    raise MemoryError(f"Out of temp memory")
                # "creamos" la variable temporal
                temp = self.currMTempF
            elif tipoT == 1: # int
                # revisar si hay espacio en memoria temporal
                if self.currMLocalI > self.rangoMTempI:
                    raise MemoryError(f"Out of temp memory")
                # "creamos" la variable temporal
                temp = self.currMTempI
                self.currMTempI += 1 #actualizamos valor de memoria temporal
            cuadruplo = [op,OpI,OpD, temp]
            self.pilaVariables.append(temp)
            self.pilaTipos.append(tipoT)
        elif op in [8,9,10]: # cuadruplo GOTO, 8 GOTO, 9 F, 10 T
            # no se crea memoria temporal para un GOTO
            cuadruplo = [op,OpI,None,OpD] 
            # (GoToT,OpI,,OpD) OpI = comparacion, OpD = indice de salto
            # (GoToF,OpI,,OpD)
            # (GoTo,,,OpD)     en GoTo salto directo por lo que OpI = None
        elif op == 11: # cuadruplo de print
            cuadruplo = [op,None,None,OpI]
        self.currCuadruplo += 1 # el siguiente cuadruplo estara en curr + 1
        self.cuadruplos.append(cuadruplo) # guardamos cuadruplo
    
    def addCTE(self, cte, type): # para agregar constantes

        if type == "int":
            t = 1
        elif type == "float":
            t = 0
        elif type == "string":
            t = 2
        
        # checar si ya existe la constante
        if not self.checkCTE(cte): # si no existe la cte, la creamos
            # ver si es int o float
            if t == 1: # es int
                if self.currMCteI > self.rangoMCteI: # checamos si tenemos espacio en memoria
                    raise ValueError("Run out of memory for constant int ")
                currMCte = self.currMCteI
                self.currMCteI += 1   
            elif t == 0: # es float
                if self.currMCteF > self.rangoMCteF: # checamos si tenemos espacio en memoria
                    raise ValueError("Run out of memory for constant float ")
                currMCte = self.currMCteF
                self.currMCteF += 1
            elif t == 2: # string
                
                if self.currMCteS > self.rangoMCteS: # checamos si tenemos espacio
                    raise ValueError("Run out of memory for constant string ")
                currMCte = self.currMCteS
                self.currMCteS += 1
            # guardamos en el dir
            self.dirCTE[cte] = currMCte

    def getDireccionMemoria(self,id, cte, func = None):
        if func == None:
            func = self.currFunc
        
        if not cte: # es una variable
            dirM = self.dirFunc[func][1][id][1]
        else: # es una constante
            dirM = self.dirCTE[id]
        return dirM
    
    def setGoTo(self, i, salto): # i = indice del cuadruplo, a donde debe saltar
        self.cuadruplos[i][3] = salto
    
