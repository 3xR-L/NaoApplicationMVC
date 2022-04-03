from conexiones.Conexion import Conexion
import pytest

def test_connectDB():
    try:
        dbt = Conexion()
        print(dbt)
        assert dbt is not None
    except Exception as e:
        print(e)
        assert False
    finally:
        print("Cerrar conexiones")
