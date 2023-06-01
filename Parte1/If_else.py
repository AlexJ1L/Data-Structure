edad = 19

#Example
if edad >= 18:
    print("Puedes pasar")
else:
     print("No puedes pasar")


#OPCIONES CON elif ----------------->>>>>>>>>

Ingreso = 899

if Ingreso >= 2000:
    print("ESTAS BIEN EN TODO EL MUNDO")

elif Ingreso >= 1000:
    print("ESTAS BIEN EN MEXICO")

elif Ingreso >= 500:
    print("ESTAS BIEN EN COLOMBIA")

elif Ingreso >= 300:
    print("ESTAS BIEN EN ARGENTINA")

elif Ingreso >= 100:
    print("ESTAS BIEN EN ECUADOR")


else:
    print("CLASE BAJA")


#if ANIDADO
ingreso_mensual = 800 #800
gasto_mensual = 400   #400

if ingreso_mensual   > 100: #
    if ingreso_mensual * gasto_mensual >= 32000: 
        print("GANAS BIEN PARA TODO EL MUNDO")
        
    elif ingreso_mensual - gasto_mensual >= 400:
        print ("TIENES UN INGRESO MENSUAL ACEPTABLE")
        
    elif ingreso_mensual + gasto_mensual >= 120:
        print("ESTAS ALGO BIEN")
    else:
     print("ESTAS MUY MAL ECONOMICAMENTE")