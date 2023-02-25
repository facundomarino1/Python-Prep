x='Homework02'
print('Hi, Im testing Facundos', x)

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
var1=(7)
print(var1)
# 2) Imprimir el tipo de dato de la constante 8.5
print(type(8.5))
# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(var1))
# 4) Crear una variable que contenga tu nombre
var2='facundo'
# 5) Crear una variable que contenga un número complejo
var3=3+5j
# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(var3))
# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
var4=3.1416
print(var4)
# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
var5='True'
var6=True
# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print('var5 es',type(var5),' y var6 es', type(var6))
# 10) Asignar a una variable, la suma de un número entero y otro decimal
var7=5+5.5
print(var7)
# 11) Realizar una operación de suma de números complejos
var8=1+1j
var9=var8+var3
print(var9)
# 12) Realizar una operación de suma de un número real y otro complejo
var10=var7+var9
print(var10)
# 13) Realizar una operación de multiplicación
var11=5*5
print(var11)
# 14) Mostrar el resultado de elevar 2 a la octava potencia
var12=2**8
print(var12)
# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
var13=27/4
print(var13)
# 16) De la división anterior solamente mostrar la parte entera
var14=27//4
print(var14)
# 17) De la división de 27 entre 4 mostrar solamente el resto
var15=27%4
print(var15)
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
var16=4*var14+var15
print(var16)
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var17='hola'+'mundo'
print(var17)
# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
var18='2'
var19=2
var20=(var18==var19)
print(var20, '2 texto no es igual a 2 número')
# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
var21=int(var18)
var22=(var21==var19)
print(var22)
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
a=float(3.8)
b=str('3.8')
print(a, b)
# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
var23=3
var23-=1
print(var23)
# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
var24=1<<2
print(var24)
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
var25=2+2
print(var25)
# 26) Realizar una operación válida entre valores de tipo entero y string
var26=2*'prueba'
print(var26)