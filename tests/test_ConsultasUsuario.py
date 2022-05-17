password = "123456"
nombreUsuario = "admin"


def test_ConsultasUsuario_login_correcto():
    print(
        "SELECT * FROM usuarios WHERE usuario = '{}' and password ='{}'".format(
            nombreUsuario, password
        )
    )
