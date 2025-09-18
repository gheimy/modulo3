# 🐍 Tareas de Introducción a Python

Este repositorio contiene tres tareas básicas para practicar conceptos fundamentales de Python: variables, expresiones, funciones, entrada/salida de datos y uso de módulos.

## ✅ Objetivos Generales

- Usar **variables** y realizar **operaciones matemáticas simples**.
- Usar **módulos estándar** de Python (como `math`).
- Practicar la función `print()` para mostrar resultados.
- Usar **funciones** definidas por el usuario.
- Leer **entrada del usuario** con `input()`.
- Usar métodos de **formato de texto** (`.rjust()`).

## 📘 Código 1: Calcular el Cuadrado de un Número

### Objetivo:
- Practicar el uso de variables y operaciones aritméticas simples.

### Instrucciones:
1. Crear una variable `num` con el valor `4`.
2. Calcular su cuadrado y guardarlo en una nueva variable llamada `cuadrado`.
3. Imprimir el resultado con `print()`.

### Pista:
- Usa `num ** 2` o `num * num`.

### Salida esperada:
16

## 📗 Código 2: Calcular el Área de un Círculo

### Objetivo:
- Aprender a importar módulos (`math`) y usar expresiones con variables.

### Instrucciones:
1. Importa el módulo `math`.
2. Declara una variable `radio_circulo = 5`.
3. Calcula el área del círculo usando la fórmula:  
   Area = π * r²
4. Imprime el resultado con `print()`.

### Pista:
- Usa `math.pi` y `radio_circulo ** 2`.

### Salida esperada:
El área del círculo es: 78.53981633974483

## 📙 Código 3: Alinear Texto a la Derecha

### Objetivo:
- Trabajar con entrada de texto y alineación de cadenas.

### Instrucciones:
1. Pedir al usuario que escriba una línea de una canción usando `input()`.
2. Alinear el texto a la derecha usando `.rjust(80)`.
3. Imprimir el texto alineado.

### Pista:
- Usa: `linea.rjust(80)`

### Ejemplo de salida:
                                               Let it be, let it be


## 🧪 Pruebas Automatizadas

Puedes ejecutar el siguiente archivo para verificar que tu código está correcto:

```bash
python test_codigo1.py para el codigo1
python test_codigo2.py para el codigo2
python test_codigo3.py para el codigo3

## 📂 Entrega

1. Crea un archivo llamado `M3-tareas-python-basico-nombre`.
2. Crea tres archivos:
   - `codigo1_cuadrado.py`
   - `codigo2_area_circulo.py`
   - `codigo3_alinear_texto.py`
3. Incluye este `README.md` explicativo en el repositorio.
4. Verifica que todos los archivos funcionen correctamente.
5. Comparte el enlace del repositorio en la entrega de proyecto esta semana.

