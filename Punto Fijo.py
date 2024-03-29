# Método de Punto fijo

# %% Reset
# from IPython import get_ipython
# get_ipython().magic('reset -sf')

# %% Funciones
import Funsiones_PuntoFijo as f

# %% Entradas
print("\nMétodo de Punto fijo\n")
Po = float(input("Ingrese el valor de la primera aproximación(Po)\n"))
TOL = float(input("Ingrese el valor de la tolerancia(TOL)\n"))

if TOL != 0.0:
    tipErr = int(input("Escoja el tipo de error, 1:E_abs, 2:E_rel,3:E_%\n"))
else:
    print("\nTipo de error: porcentual")
    
No = int(input("Ingrese el numero máximo de iteraciones(No)\n"))
guardar = input("¿Quiere guardar el resultado? y/n\n")

# %% Declaración de variables
i = 1
E = 100.0
alfa = 1.0
epsilon = 6.123233995736766e-17
AproxIni = Po

# %% Consideraciones iniciales
if TOL == 0.0:
    TOL = epsilon
    tipErr = 3

if tipErr < 1.0 or tipErr > 3.0:
    tipErr = 2

#Tipo de error(Mensaje)    
if tipErr == 1:
    Err = "_abs"
elif tipErr == 2:
    Err = "_rel"
elif tipErr == 3:
    Err = "_%"

# %% Método de Punto fijo
while E> epsilon and i<=No:
    p = f.g(Po)
    
    if p != 0.0:
        E = f.Errores(tipErr,p,Po)
    
    delta = abs(p-Po)
    alfa = abs(E/alfa)
    
    #Impresión y almacenamiento de resultados
    if abs(p-Po) < TOL:
        print("-------------------------------------------------------------")
        print("Proceso exitoso")
        print("Po =",AproxIni)
        print("p =",p)
        print("f(p) =",f.f(p))
        print("Error"+Err+" =",E)
        print("Alfa =",alfa)
        print("Delta =",delta)
        print("TOL =",TOL)
        print("No =",i)
        print("-------------------------------------------------------------")
        
        #Archivo de texto con los datos
        if guardar == "y":        
            resultado_PuntoFijo = open("resultado_PuntoFijo.txt","a")
            resultado_PuntoFijo.write("Po = "+str(AproxIni)+"\n")
            resultado_PuntoFijo.write("p = "+str(p)+"\n")
            resultado_PuntoFijo.write("Error"+Err+" = "+str(E)+"\n")
            resultado_PuntoFijo.write("Alfa = "+str(alfa)+"\n")
            resultado_PuntoFijo.write("Delta = "+str(delta)+"\n")
            resultado_PuntoFijo.write("TOL = "+str(TOL)+"\n")
            resultado_PuntoFijo.write("No = "+str(i)+"\n")
            resultado_PuntoFijo.write("-------------------------------------------------------------\n")
            resultado_PuntoFijo.close()
        break
    
    i += 1
    Po = p
    alfa = E
    
if i > No:
    print(f"\nEl método ha fallado luego de la iteración No ={i+1}")    