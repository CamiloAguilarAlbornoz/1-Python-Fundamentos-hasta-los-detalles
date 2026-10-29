# Cortocircuito

# OR y AND como cortocircuito

# OR
True or print('Hola Mundo or') or True # Como la primera opcion se cumple, termina la línea y no ejecuta lo demás, generando un cortocircuito
False or print('Hola Mundo or') or True # Como la primera opción no se cumple, pregunta en la segunda, el print al tener contenido es un Truthy, por lo que lo toma como true, ejecuta el print y no ejecuta lo demás, generando un cortocircuito

# AND
False and print('Hola Mundo and') # Como al menos una es false no ejecuta nada y ejecuta el cortocircuito
True and print('Hola Mundo and') # Como ambos se cumplen entonces ejecuta el cortocircuito

############################## Ejemplo #############################
name = None
name and print(name.upper()) # Como la variable es None, primero evaluo si es Truthy, si cumple, pues ejecuta el print, si no entonces genera un cortocircuito para que el programa no se reviente por pedir un upper a un None
