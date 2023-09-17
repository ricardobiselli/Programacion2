"""
Definir un diccionario para las 'Compras' que contenga los siguiente valores:
- Clave "Mario Pedernera", valor de tipo lista: ["cafetera", "TV 50 pulgadas", "mouse gamer"]
- Clave "Ezequiel Castello", valor de tipo lista: ["ipad", "ipod", "iphone"]
- Clave "Pablo Piristrelli", valor de tipo lista: ["Reproductor de CD", "Videograbadora"]
"""

# COMPLETAR - INICIO

Compras = {
    "Mario Pedernera": ["cafetera", "TV 50 pulgadas", "mouse gamer"],
    "Ezequiel Castello":["ipad", "ipod", "iphone"],
    "Pablo Piristrelli":["Reproductor de CD", "Videograbadora"],   
}

# COMPLETAR - FIN

assert (
    (Compras["Mario Pedernera"] == ["cafetera", "TV 50 pulgads", "mouse gamer"])
    and (Compras["Ezequiel Castello"] == ["ipad", "ipod", "iphone"])
    and (Compras["Pablo Piristrelli"] == ["Reproductor de CD", "Videograbadora"])
)
