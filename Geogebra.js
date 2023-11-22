
// para haller solucion con integrales
l1=Soluciones(g=h)
Interseca(h,f)
Interseca(h,g)
a=IntegralEntre(h,f,x(A),x(F))
b=IntegralEntre(g,f,x(F),x(D))
totalArea=a+b

// definiendo las funciones que intervienen
f(x) = 3*(x-((1)/(2)))^(2)+((1)/(5))
g(x) = -3 (x-((1)/(2)))^(2)+((1)/(2))
h(x)=((9)/(10)) * x
// generando los puntos aleatorios en el rango [0, 1]
l1 = Secuencia((random(),random()),f,1,n,1)
// se guarda en la lista {1, 0} 
// 1 si el punto esta dentro el area requerida
// 0 si el punto no esta en el area requerida
Lista = Secuencia(
    Si( Elemento(y(l1),f) >= 3 * (Elemento(x(l1),f)-((1)/(2)))^(2)+((1)/(5)) &&
        Elemento(y(l1),f) <= -3 * (Elemento(x(l1),f)-((1)/(2)))^(2)+((1)/(2)) &&
        Elemento(y(l1),f) <= (9/10) * Elemento(x(l1),f)
        ,1, 0) 
    ,f, 1, n, 1)
// sirve para graficar los puntos de otro color que estan dentro del area requerida
verificador = secuencia(si(Elemento(Lista, f) == 1, (Elemento( x(l1), f), 
Elemento(y(l1), f) ) , (,) ) , f, 1, n, 1)
// calcula la proporcion para hallar el area
respuesta = ((Suma(Lista)) / (n))
