import ast

print("🔎 Ejecutando test para 'codigo3.py'...\n")

# Cargar el código del estudiante
with open("codigo3.py", "r", encoding="utf-8") as f:
    student_code = f.read()

# Analizar el código con AST
tree = ast.parse(student_code)

# Marcadores de verificación
uso_input = False
uso_rjust = False
uso_print = False

# Recorrer nodos del árbol
for node in ast.walk(tree):
    # Tarea 1: Buscar uso de input()
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id == "input":
            uso_input = True

    # Tarea 2: Buscar uso de rjust()
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
        if node.func.attr == "rjust":
            uso_rjust = True

    # Tarea 3: Buscar uso de print()
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id == "print":
            uso_print = True

# Imprimir resultados
print("✅ Tarea 1 (uso de input):", "Cumplida" if uso_input else "No cumplida")
print("✅ Tarea 2 (uso de rjust):", "Cumplida" if uso_rjust else "No cumplida")
print("✅ Tarea 3 (uso de print):", "Cumplida" if uso_print else "No cumplida")

# Mensaje final
if uso_input and uso_rjust and uso_print:
    print("\n✅ Todas las tareas están correctas.")
else:
    print("\n❌ Faltan tareas por completar. Revisa tu código.")
