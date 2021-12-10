#FERNANDO ANGEL NAHUAT CAAMAL-19070020
#EDUARDO ALEJANDRO TUYU CANCHE-19070019
#DANIEL RICARDO MENA GONZÁLEZ-19070021
#LUIS ANGEL GASPAR BALAM CAAMAL-19070043
import sys
import ply.yacc as yacc
from lexer import tokens

VERBOSE = 1
#----------------------------------------------------------------------------------------------
#-------------------------------------------- Apartados para metodos de interpretacion de codigo a leer
def p_program(p):
	'program : declaration_list'

	pass


def p_declaration_list(p):
	'''declaration_list : declaration_list  declaration
                        | declaration
						
						
                        
    '''
	pass
#---------------------------- Metodo para hacer un modelado de declaraciones
#lista de sentencias SELECCIONAR ACTUALIZAR INSERTAR ELIMINAR 
def p_declaration(p):
	'''declaration : sele fro wher PUNTOYCOMA
	               | upd se wher PUNTOYCOMA
				   | inser value PUNTOYCOMA
				   | del wher PUNTOYCOMA
				   | sele fro PUNTOYCOMA
				   
				   '''
				   
	pass



#-------------------------------------- Declaracion de partes de una sentencia sql

#forma de la sentencia SELECT * O SELEC GATO, HOLA FROM
def p_sele(p):
	'''sele : SELECT variab
	                     | SELECT TIMES
	                     
	                     
						 
	'''
	pass


#sentencia WHERE con valor comparado eje : WHERE GATO=12
def p_wher(p):
	'''wher : WHERE vcom 
	            
	'''
	pass
#FORMA DE LA EXPRESION QUE SRIVE PARA ELIMINAR
def p_del(p):
	'''del : DELETE FROM VARIABLE
	'''
	pass
# FORMA FROM PARA REFERIRNOS A UNA TABLA
def p_fro(p):
	'''fro : FROM VARIABLE	 
	'''
	pass
#FORMA DE LA SENTENCIA UPDATE EJEMPLO : UPDATE TABLA
def p_upd(p):
	'''upd : UPDATE variab
				 
	'''
	pass
#FORMA DE LA SENTENCIA SET ejemplo : set gato=1 , perro= "french"
def p_se(p):
	'''se : SET vawva
	'''
	pass


#forma de la sentencia INSERT INTO TABLA
def p_inser(p):
	'''inser : INSERT INTO variab
	'''
	pass

#FORMA DE LA SENTENCIA SQL PARA ASIGNAR VALORES---> VALUES("valor1","valor2",3) 
def p_value(p):
	'''value : VALUES PARE_IZ  val PARE_DE 
	'''
	pass




#-------------------------------------- Declaracion de Atributos formas en las cuales los dato se usan en sql
#variables normales y separadas por comas ej : auto, gato, perro
def p_variab(p):
  '''variab : variab COMA VARIABLE
		   | VARIABLE
		   | COMA VARIABLE 
            
     '''
  pass
#este significa que una variable es igual a un valor ej : valor=123 o valor="hola"
def p_vawva(p):
	'''vawva : vawva COMA VARIABLE SIMBOLO_IGUAL NUMERO 
			 |  VARIABLE SIMBOLO_IGUAL NUMERO
			 | COMA VARIABLE SIMBOLO_IGUAL NUMERO
			 | vawva COMA VARIABLE SIMBOLO_IGUAL CADENA
			 | VARIABLE SIMBOLO_IGUAL CADENA
			 | COMA VARIABLE SIMBOLO_IGUAL CADENA
	'''
	pass
#valores de cadenas y numeros separados por comas ej : 123, "hola", 455

def p_val(p):
	'''val :  val COMA CADENA 
	        | CADENA 
			| COMA CADENA
			| val COMA NUMERO
	        | NUMERO
			| COMA NUMERO
			
	         
	'''
#variables que son comparados con numeros y cadenas eje: valor >= 123 o valor<123
def p_vcomp(p):
	'''vcom : vcom andor variab relop NUMERO
	        | variab relop NUMERO 
			| andor variab relop NUMERO
			| vcom andor variab relop CADENA
			| variab relop CADENA
			| andor variab relop CADENA
	'''
	pass



#insert into vehiculos values ("10804.80" , 2019 , "YBB-1041" , "2000","2");
#-------------------------------------- Expresiones de Comparación ----------------------------
def p_relop(p):
	'''relop : MENOR
			 | MENOR_O_IGUAL
			 | MAYOR
			 | MAYOR_O_IGUAL
			 | DIFERENTE
			 | DISTINTO
			 | ISEQUAL
			 | SIMBOLO_IGUAL
	'''
	pass



def p_andor(p):
	'''andor : AND
	         | OR 
	'''
	pass

#def p_sumres(p):
#	'''sumres : SUMA 
#			 | RESTA
#	'''
#	pass
	



def p_empty(p):
	'empty :'
	pass
#--------------------- Metodo para detectar errores durante la compilacion y en el analisis de tokens-------------
def p_error(p):
	if VERBOSE:
		if p is not None:
			print("\x1b[1;33m" + "\t ERROR: Syntax error - Unexpected token" + chr(27) + "[0m")
			print("\n" + "\t\tLinea: " + str(p.lexer.lineno) +"\t ---> " ,"Error sintactico de tipo {:4} en el valor {:4}".format(
            str(p.type), str(p.value)))
		else:
			print(chr(27) + "[1;31m" + "\t Error durante la compilación: “Error de sintáxis”" + chr(27) + "[0m")
			print("\t\tLine:  " + str(p))

	else:
		raise Exception('syntax', 'error')

parser = yacc.yacc()



#---------------------------------------------- Lectura del archivo .sql
codigo = 'prueba.sql'
scriptfile = open(codigo, 'r', encoding= 'UTF-8')
scriptdata = scriptfile.read()

#---------------------- Formato de impresion en consola y asigancion del analizador sintactico al archivo .sql--------------------------

print ("\u001b[32m"+"\nINICIA ANALISIS SINTACTICO"+"\u001b[32m")

print("\n" + "\u001b[31;1m" + "REPORTE DE ERRORES:  ------------------------------------------- >")

parser.parse(scriptdata, tracking=False)

print ("\u001b[32m"+"\nFINAL ANALISIS SINTACTICO"+"\u001b[32m")