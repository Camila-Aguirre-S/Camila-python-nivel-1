def eliminar_elemento_funcional():
    while True:
        # Solicitar al usuario ingresar una lista de elementos separados por comas
        lista = input("Ingrese una lista de elementos separados por comas: ").split(",")
        
        # Solicitar al usuario ingresar el elemento a eliminar
        elem_a_eliminar = input("Ingrese el elemento a eliminar: ")
        
        # Crear una nueva lista filtrando los elementos diferentes al elemento a eliminar
        nueva_lista = list(filter(lambda elem: elem != elem_a_eliminar, lista))
        
        # Mostrar la lista sin el numero a eliminar
        print(f"La nueva lista es: {nueva_lista}")
        
        while True:
            # Solicitar al usuario si desea ingresar otra lista
            opcion = input("¿Desea ingresar otra lista? (si/no)")
            
            if opcion.lower() == "si" or opcion.lower() == "no":
                break
            else:
                print("Ha ocurrido un error. Intente de nuevo.")
        
        # Si el usuario ingresa "no", salir del loop
        if opcion.lower() == "no":
            break

eliminar_elemento_funcional()

#funcion Original

#while True:
   # lista = input("Ingrese una lista de elementos separados por comas: ").split(",")
  #  elem_a_eliminar = input("Ingrese el elemento a eliminar: ")
  #  nueva_lista = lista.copy()
    
  #  while elem_a_eliminar in nueva_lista:
  #      nueva_lista.remove(elem_a_eliminar)
    
  #  print(f"La nueva lista es: {nueva_lista}")
    
  #  opcion = input("¿Desea ingresar otra lista? (si/no)")

  #  while opcion not in ["si", "no"]:
  #      print("Ha ocurrido un error. Intente de nuevo.")
  #      opcion = input("¿Desea ingresar otra lista? (si/no)")
    
    # Si el usuario ingresa "no", salir del loop
  #  if opcion.lower() == "no":
    #    break

#Caso de Prueba 1
# Entrada1= 1,2,3,4
# elem_a_eliminar = 4
# salida esperada= 1,2,3