from abc import ABC, abstractmethod


class usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self):
        return self._nombre.title()

    @staticmethod
    def validar_credenciales(tipo_usuario, email: str, contrasenia: str) -> bool:

        email = input(
            "Ingrese el mail con el que se registró: ")
        contrasenia = input("Ingrese su contraseña: ")
        email_encontrado = False
        for user in tipo_usuario:
            if email == user["email"]:
                email_encontrado = True
                if contrasenia == user["contraseña"]:
                    print("YES!")  # temporal
                    return
                else:
                    print("Contraseña incorrecta")
                    return False

        if not email_encontrado:
            print("Mail no registrado, debe darse de alta en alumnado")
            return False
