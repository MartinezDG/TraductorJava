from grammarMorseListener import grammarMorseListener
from grammarMorseParser import *

class TraduceMorseCode(grammarMorseListener):
    def __init__(self):
        self.output_lines = []  # Lista para almacenar las líneas de código traducidas

    # Al iniciar un archivo, agrega la declaración de la clase Java y el main
    def enterMorse_line(self, ctx:grammarMorseParser.Morse_lineContext):
        self.output_lines.append("public class TraductorPythonAJava {")
        self.output_lines.append("    public static void main(String[] args) {")

    # Al terminar el archivo, cierra el main y la clase
    def exitMorse_line(self, ctx:grammarMorseParser.Morse_lineContext):
        self.output_lines.append("    }")
        self.output_lines.append("}")

    # Traducción de 'print' en Python a 'System.out.println' en Java
    def enterPrint_stmt(self, ctx:grammarMorseParser.Print_stmtContext):
        expression = ctx.expression().getText()  # Obtener la expresión completa
        self.output_lines.append(f"        System.out.println({expression});")

    # Traducción de 'def' en Python a la declaración de un método en Java
    def enterFunc_def(self, ctx:grammarMorseParser.Func_defContext):
        func_name = ctx.ID().getText()
        params = [param.getText() for param in ctx.param_list().ID()]
        java_params = ", ".join([f"int {param}" for param in params])  # Asume que todos los params son int
        self.output_lines.append(f"    public static int {func_name}({java_params}) {{")

    # Traducción de 'return' en Python a 'return' en Java
    def enterReturn_stmt(self, ctx:grammarMorseParser.Return_stmtContext):
        expression = ctx.expression().getText()
        self.output_lines.append(f"        return {expression};")

    # Traducción de la asignación en Python a Java
    def enterAssign_stmt(self, ctx:grammarMorseParser.Assign_stmtContext):
        variable = ctx.ID().getText()  # Obtener el nombre de la variable
        expression = ctx.expression().getText()  # Obtener la expresión que se asigna
        self.output_lines.append(f"        {variable} = {expression};")

    # Cierra el método
    def exitFunc_def(self, ctx:grammarMorseParser.Func_defContext):
        self.output_lines.append("    }")

    # Método para guardar la salida en un archivo
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write('\n'.join(self.output_lines))
