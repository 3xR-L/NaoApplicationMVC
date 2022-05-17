from conexiones.Conexion import Conexion


def setup_module():
    global dbt
    try:
        dbt = Conexion()
    except Exception as e:
        print(e)
        dbt = None


def teardown_module():
    dbt.cerrar()
    print("\nSe cerro la conexion a la base de datos")


class Test_Conexion:
    def test_connectDB(self):
        assert dbt is not None
