#FERNANDO ANGEL NAHUAT CAAMAL-19070020
#EDUARDO ALEJANDRO TUYU CANCHE-19070019
#DANIEL RICARDO MENA GONZÁLEZ-19070021
#LUIS ANGEL GASPAR BALAM CAAMAL-19070043

#librerrias usadas
import ply.lex as lex
import sys
import re
#----------------------
    #palabras reservadas
reserved = {
    'from':'FROM',
    'select':'SELECT',
    'update':'UPDATE',
    'delete':'DELETE',
    'set' :'SET',
    'where':'WHERE',
    'values':'VALUES',
    'insert':'INSERT',
    'into':'INTO',
    'delete':'DELETE',
    'and' : 'AND',
    'or' : 'OR',
    'as' : 'AS',
    "create":"CREATE",
    "primary":"PRIMARY",
    "key":"KEY",
    "not":"NOT",
    "varchar":"VARCHAR",
    "int":"INT",
    "auto_increment":"AUTO_INCREMENT",
    "table":"TABLE",
    "use":"USE",
    "database":"Database",
    "add":"Add",
    "constraint":"Constraint",
    "foreign":"Foreign",
    "references":"References",
    "on":"On",
    "cascade":"Cascade",
    "alter":"Alter"
   


    
  

    
    
}
#tokens
tokens = list(reserved.values())+[
    # Symbols
    'ASSIGN',
    'MOD',
    'SUMA',
    'PLUSPLUS',
    'PLUSEQUAL',
    'RESTA',
    'MINUSMINUS',
    'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'MENOR',
    'MENOR_O_IGUAL',
    'MAYOR',
    'MAYOR_O_IGUAL',
    'SIMBOLO_IGUAL',
    'DIFERENTE',
    'DISTINTO',
    'ISEQUAL',
    'PUNTOYCOMA',
    'COMA',
    'PARE_IZ',
    'PARE_DE',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'PUNTO',
    'QUESTIONMARK',
    'COMILLASIMPLE',
    'COMILLASDOBLES',
    # Others   
    'VARIABLE',  
    'NUMERO',
    'CADENA',
    'CADENA2',
    'ID',
    'COMENTARIOS'
    
    
 
]


#expresiones regulares para que se seleccione el token
t_MOD = r'%'
t_SUMA   = r'\+'
t_RESTA  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_SIMBOLO_IGUAL  = r'='
t_DISTINTO = r'!'
t_MAYOR = r'<'
t_MENOR = r'>'
t_PUNTOYCOMA = ';'
t_COMA  = r','
t_PARE_IZ = r'\('
t_PARE_DE  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_PUNTO = r'\.'
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'
t_QUESTIONMARK = r'\?'

 #expresion regular para numeros
def t_NUMERO(t):
    r'\d+\.+\d+|\d+'
    t.value = str(t.value)
    return t

#expresiones regulares para la busqueda de variable
def t_VARIABLE(t):
    r'[a-zA-Z](\w)*'#expresion
    if t.value in reserved:#comnprueba si el valor se encuentra en las reservadas
        t.type = reserved[t.value]  # Check for reserved words
        return t
    else:
        return t

# Check reserved words
# This approach greatly reduces the number of regular expression rules and is likely to make things a little faster.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved+[t.value]  
        return t
    else:
        t_error(t)

def t_CADENA(t):
    r'\"+[0-9A-Za-z_\-\.@,\s]+\"+'
    return t

def t_CADENA2(t):
    r'\'+([^\'].)*\'+'
    return t

def t_MENOR_O_IGUAL(t):
	r'<='
	return t

def t_MAYOR_O_IGUAL(t):
	r'>='
	return t

def t_ASSIGN(t):
    r'=>'
    return t
def t_COMENTARIOS(t):
    r'\/\*[\s\*a-zA-Z\.0-9]*\*\/|--.+'
    return t

    
def t_DIFERENTE(t):
	r'!='
	return t

def t_ISEQUAL(t):
	r'=='
	return t




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_space(t):
    r'\s+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_error(t):
    print ("Lexical error: " + str(t.value))
    t.lexer.skip(1)

#_____________________________________________________________________
#lista para almacenar los datos
lista1=[]
def test(data, lexer):
	lexer.input(data)
	i = 1
	while True:     
		tok = lexer.token()
		if not tok:
			break

		lista1.append([str(i),str(tok.lineno),str(tok.type),str(tok.value)])
        
		i += 1
        
	
   
    #print(tok)

#_____________________________________________________________________
lexer = lex.lex()
#_____________________________________________________________________
#incio de ejecucuion de codigo
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.sql'
	f = open(fin, 'r')
	data = f.read()
	#print (data)
	#lexer.input(data)
	test(data, lexer)#se llama a la funcion test
	#input()



#for dia in lista1:
    
    
 #print(tabulate([["numero de linea","linea de codigo","tipo de token","valor"],[dia[0],dia[1],dia[2],dia[3]]]))
#_____________________________________________________________________
#impresion de datos
from prettytable import PrettyTable#libreria para el uso de tabla
from prettytable import DOUBLE_BORDER#se llama un estilo para la tabla
table = PrettyTable (["NUMERO DE LINEA", "LINEA DE CODIGO","LEXEMA", "TOKEN"])#se asignan los encabezados
table.set_style (DOUBLE_BORDER)#se asigna el estilo
#contador
c=0
for i in lista1:
    i[2] = re.sub("\!|\_"," ",i[2])#cambia los guiones bajos por espacio-estetica
    if i[3] in reserved :#comprueba si el valor se encuentra en las reservadas para mostrar un texto ques una palabra reservada
     #se agrega el dato de la lista a la tabla
     table.add_row((i[0],i[1],i[3],("Palabra reservada "+i[2])))#se agrega un texto para mostar que es reservada
     print(table[c])#se imprime el valor recien agregado a la tabla
    else:#si el lexema no es reservada
     table.add_row((i[0],i[1],i[3],i[2]))#se agregan los datos a la tabla
     print(table[c])#impresion

    c=c+1#contador que aumenta 

