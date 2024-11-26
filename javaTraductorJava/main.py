from antlr4 import *
from grammarMorseLexer import grammarMorseLexer
from grammarMorseParser import grammarMorseParser
from TraduceMorseCode import TraduceMorseCode

def main():
    in_code = input("File Name> ")
    out_code = "TraductorPythonAJava.java"  # Nombre del archivo de salida con extensión .java

    with open(in_code, 'r') as fileope:
        lexer = grammarMorseLexer(InputStream(fileope.read()))
    stream = CommonTokenStream(lexer)
    parser = grammarMorseParser(stream)
    tree = parser.morse_line()

    traductor = TraduceMorseCode()
    walker = ParseTreeWalker()
    walker.walk(traductor, tree)

    # Imprimir la traducción en consola
    for line in traductor.output_lines:
        print(line)

    # Guardar la traducción en un archivo .java
    traductor.save_to_file(out_code)
    print(f"\nTraducción guardada en: {out_code}")

if __name__ == '__main__':
    main()

