# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:Sarah Ledesma Verdun
# Curso:2do 2a
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.
print ("===== KIOSCO ESCOLAR =====")
nombre = input("nombre: ")
plata_cliente = int(input("cuanto dinero tiene?(en pesos) "))
print ("tenemos : 1. Agua a $700.      2. alfajor a $900.           3. tostado a $2200")
pedido =  int(input("que le apetece?(1, 2 o 3)"))
productos = ["Agua", "alfajor", "tostado"]
precios = [700, 900, 2200]
print ("usted pidio: ", productos[pedido-1], "y le costara $",precios[pedido-1])
pedido_total = precios[pedido-1]

# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de productos y precios.
# Pedir los datos del cliente.


# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener producto y precio.


# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
