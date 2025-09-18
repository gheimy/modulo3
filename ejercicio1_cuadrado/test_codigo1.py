# test_code.py

#funcion para revisar el cuadrado
def test_linea_cuadrado():
    with open('codigo1.py', 'r') as f:
        contenido = f.read()
    
    linea_esperada = "cuadrado = num ** 2"
    assert linea_esperada in contenido, "La línea esperada no está presente en el código."

# Ejecutar el test
if __name__ == "__main__":
    test_linea_cuadrado()
    print("✅ Test pasado: La cuadrada esperada está presente.")