import ast

# Cargar el código del estudiante desde un archivo
with open("codigo2.py", "r", encoding="utf-8") as f:
    student_code = f.read()

# Analizar el código como un árbol de sintaxis abstracta
tree = ast.parse(student_code)

# Marcadores para verificar tareas
tarea1_ok = False
tarea2_ok = False
uso_print_ok = False

# Buscar importación de math (Tarea 1)
for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for alias in node.names:
            if alias.name == "math":
                tarea1_ok = True

# Buscar si se define la variable 'radio_circulo' (Tarea 1)
has_radio_variable = any(
    isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "radio_circulo" for t in node.targets
    )
    for node in ast.walk(tree)
)
tarea1_ok = tarea1_ok and has_radio_variable

# Buscar cálculo de área con math.pi y radio_circulo (Tarea 2)
for node in ast.walk(tree):
    if isinstance(node, ast.Assign):
        if isinstance(node.value, ast.BinOp):
            # Verifica si hay una operación con math.pi
            if (
                isinstance(node.value.left, ast.Attribute)
                and isinstance(node.value.left.value, ast.Name)
                and node.value.left.value.id == "math"
                and node.value.left.attr == "pi"
            ):
                tarea2_ok = True

# Buscar uso de print (Tarea 2)
for node in ast.walk(tree):
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == "print":
            uso_print_ok = True

# Resultados
print("🔎 Ejecutando test para 'codigo2.py'...\n")
if tarea1_ok and tarea2_ok and uso_print_ok:
    print("\n✅ Todas las tareas están correctas.")
else:
    print("\n❌ Faltan tareas por completar. Revisa tu código.")
