## Proyecto Little Duck

Leonardo Mojica Amezquita A00571960


<ul align="justify">
<p>
Este proyecto conciste en crear un lenguaje de programación llamado "Little Duck" el cual esta explicado tanto su gramatico y lexico en el documento "A00571960_Documentacion_littleDuck.docx".
<p>

<p>
Este proyecto tiene de alcance el generar un analisis lexico, sintactico y semantico de un programa que cuenta con operadores como +, -, *, /, <, >, !=, ademas de estatutos print(), do while, if else. La sintaxic acepta funciones de tipo void, y el lenguaje en general tiene variables de tipo int y float, y constantes int, float y strings. Despues del analisis semantico se crea un codigo intermedio en formato de cuadruplos, este se manda a una maquina virtual la cual interpreta estos cuadruplos y los ejectua.

    Nota: En esta version, no se crean cuadruplos. Por lo que se puede crear
          funciones pero estas no se ejecutaran.
</p>

</ul>

<h3>Como usar el proyecto</h3>

<ul>
<p>
Este proyecto fue creado usando antlr4, y python.

Para correr este proyecto se debe tener instalado python (el cual puede ser instalado desde la tienda de microsoft o la pagina oficila: https://www.python.org).

Ademas se debe tener instalado antlr4, con el siguiente comando.

```bash
$ pip install antlr4-tools
```

Puede haber problemas con windows a la hora de instalar. Para mas informacion consultar el repo oficial: https://github.com/antlr/antlr4/blob/master/doc/getting-started.md 

Una vez se tenga todo instalado puedes descargar este repo. Debes estar en la carpeta "/antlr" y ejecutar el comando 

```bash
$ python main.py 
```

Deberas escribir el path al archivo .txt con tu codigo en la gramatica little duck, y este se ejecutara.

</p>
</ul>
