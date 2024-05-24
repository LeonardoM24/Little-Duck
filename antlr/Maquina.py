class MaquinaVirtual:
    def __init__(self):


        # rangos para validar las variables
        self.GIRange = range(1000,6500);   self.GFRange = range(6500,13000)   
        self.LIRange = range(13000,16000); self.LFRange = range(16000,19000)
        self.TIRange = range(19000,32500); self.TFRange = range(32500,46000)
        self.CIRange = range(46000,56000); self.CFRange = range(56000,66000)
        self.CSRange = range(66000,76000)

        # Memorias virtuales
        # Van a ser arreglos de memorias
        self.MGI = [0] * 5500 # memoria global int
        self.MGF = [0.0] * 6500 # memoria global float
        
        self.MLI = [0] * 3000 # memoria Local int
        self.MLF = [0.0] * 3000 # memoria Local float

        self.MTI = [0] * 13500 # memoria Temporal int
        self.MTF = [0.0] * 13500# memoria Temporal float

        self.MCI = [0] * 10000 # memoria Constante int
        self.MCF = [0.0] * 10000 # memoria Constante float
        self.MCS = [''] * 10000 # memoria Constante string

        # Bases para transformar las memorias de los cuadruplos a 
        # valores de nuestros arrelgos
        self.BaseGI = 1000
        self.BaseGF = 6500

        self.BaseLI = 13000
        self.BaseLF = 16000

        self.BaseTI = 19000
        self.BaseTF = 29000

        self.BaseCI = 46000
        self.BaseCF = 56000
        self.BaseCS = 66000

        # Cuadruplos / codigo intermedio
        self.cuadruplos = []

    
    def loadCteMemory(self, memoriaCte):
        for k, v in memoriaCte.items(): # recorrer los items
            # revisar si es entero flotante o string
            if v in self.CIRange: # es un entero
                v = v - self.BaseCI # convertimos a indice del arreglo
                self.MCI[v] = int(k) # la key es el valor de la cte
            elif v in self.CFRange: # es un float
                v = v - self.BaseCF # convertimos a indice del arreglo
                self.MCF[v] = float(k) # la key es el valor de la cte
            elif v in self.CSRange:
                v = v - self.BaseCS # convertimos a indice del arreglo
                self.MCS[v] = k # la key es el valor de la cte

    def loadCuadruplos(self, cuads):
        self.cuadruplos = cuads

    def getValue(self, dir): # conseguir valor guardado en direccion de memoria dir
        if dir in self.GIRange: # global int
            base = self.BaseGI
            return int(self.MGI[dir - base])
        elif dir in self.GFRange: # global float
            base = self.BaseGF
            return float(self.MGF[dir - base])
        elif dir in self.LIRange: # local int
            base = self.BaseLI
            return int(self.MLI[dir - base])
        elif dir in self.LFRange: # local float
            base = self.BaseLF
            return float(self.MLF[dir - base])
        elif dir in self.TIRange: # temporal int
            base = self.BaseTI
            return int(self.MTI[dir - base])
        elif dir in self.TFRange: # temporal float
            base = self.BaseTF
            return float(self.MTF[dir - base])
        elif dir in self.CIRange: # cte int
            base = self.BaseCI
            return int(self.MCI[dir - base])
        elif dir in self.CFRange: # cte Float
            base = self.BaseCF
            return float(self.MCF[dir - base])
        elif dir in self.CSRange: # cte int
            base = self.BaseCS
            return str(self.MCS[dir - base])

    def saveValue(self, dir, v): # guardar v en la direccion de memoria dir
        if dir in self.GIRange: # global int
            base = self.BaseGI
            self.MGI[dir - base] = int(v)
        elif dir in self.GFRange: # global float
            base = self.BaseGF
            self.MGF[dir - base] = float(v)
        elif dir in self.LIRange: # local int
            base = self.BaseLI
            self.MLI[dir - base] = int(v)
        elif dir in self.LFRange: # local float
            base = self.BaseLF
            self.MLF[dir - base] = float(v)
        elif dir in self.TIRange: # temporal int
            base = self.BaseTI
            self.MTI[dir - base] = int(v)
        elif dir in self.TFRange: # temporal float
            base = self.BaseTF
            self.MTF[dir - base] = float(v)
        elif dir in self.CIRange: # cte int
            base = self.BaseCI
            self.MCI[dir - base] = int(v)
        elif dir in self.CFRange: # cte Float
            base = self.BaseCF
            self.MCF[dir - base] = float(v)
        elif dir in self.CSRange: # cte int
            base = self.BaseCS
            self.MCS[dir - base] = str(v)

    def run(self, cuads = None, memoriaCte = None):
        if memoriaCte:
            self.loadCteMemory(memoriaCte)
        if cuads:
            self.loadCuadruplos(cuads)

        IP = 0 # instruction pointer (el cuadruplo que leeremos)
        cuadL = len(self.cuadruplos)
        # CUADRUPLO --> [op,opi,opd,result]
        # op
        #   0 --> +, 1 --> -, 2 --> *, 3 --> /, 4 --> <, 5 --> >, 6 --> !=
        #   7 --> =, 8 --> GoTO, 9 --> GoToF, 10 --> GoToT, 11 --> print()
        #   12 --> EOF (terminar)

        while(self.cuadruplos[IP][0] != 12 and IP < cuadL):
            # guardamos los valores del cuadruplo
            op   = self.cuadruplos[IP][0] # operador
            DopI = self.cuadruplos[IP][1] # direccion operando izquierdo
            DopD = self.cuadruplos[IP][2] # direccion operando derecho
            DR   = self.cuadruplos[IP][3] # direccion resultado

            # Switch para ver que operacion se realizara
            if   op ==  0: # SUMA
                # sacamos el valor del operador derecho
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI + opD
                self.saveValue(DR,r)
            elif op ==  1: # resta
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI - opD
                self.saveValue(DR,r)
            elif op ==  2: # Multiplicacion
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI * opD
                self.saveValue(DR,r)
            elif op ==  3: # Division
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI / opD
                self.saveValue(DR,r)
            elif op ==  4: # Menor que
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI < opD
                self.saveValue(DR,r)
            elif op ==  5: # Mayor que
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI > opD
                self.saveValue(DR,r)
            elif op ==  6: # Diferente que
                opI =  self.getValue(DopI)
                opD = self.getValue(DopD)
                r = opI != opD
                self.saveValue(DR,r)
            elif op ==  7: # asignar
                r =  self.getValue(DopI)
                self.saveValue(DR,r)
            elif op ==  8: # GoTo
                # cambiamos el ip a donde nos dice el GoTo
                # en este caso DR guarda el indice del cuadruplo para hacer el salto
                IP = DR - 1 # el -1 es porque por defecto al final del switch hacemos un + 1
            elif op ==  9: # GoToF
                condicion = self.getValue(DopI) # condicion para ver
                if not condicion: # si no se cumple cambiar ip
                    IP = DR - 1 # el -1 es porque por defecto al final del switch hacemos un + 1
            elif op == 10: # GoToT
                condicion = self.getValue(DopI) # condicion para ver
                if condicion: # si no se cumple cambiar ip
                    IP = DR - 1 # el -1 es porque por defecto al final del switch hacemos un + 1
            elif op == 11: # print
                var = self.getValue(DR)
                print(var,end=' ')
            elif op == 12: # EOF, end of file (termino)
                pass
            IP += 1