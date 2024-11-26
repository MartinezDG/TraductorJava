#Proyecto

Este proyecto transforma un codigo en especifico python a su equivalencia en codigo java lo imprime en consola de ubuntu y guarda un archivo .java

##Instrucciones

Abrir la carpeta en ubuntu con el comando, en su ubicacion donde se guarde:
cd javaTraductorJava/

###Ejemplo:
gael@LAPTOP-NOOB:~/asmprograms$ cd javaTraductorJava/

##Ejecutar el comando:
python3 main.py

###Ejemplo:
gael@LAPTOP-NOOB:~/asmprograms/javaTraductorJava$ python3 main.py

##Se imprimirá en consola el código traducido de python a su equivalencia en codigo java y además lo guardará en un archivo .java:

gael@LAPTOP-NOOB:~/asmprograms/javaTraductorJava$ python3 main.py
File Name> cartaMorse.txt
ANTLR runtime and generated code versions disagree: 4.9.3!=4.7.2
ANTLR runtime and generated code versions disagree: 4.9.3!=4.7.2
line 2:4 missing '{' at 'result'
line 6:0 extraneous input '<EOF>' expecting {'}', 'print', 'def', 'return', ID}
public class TraductorPythonAJava {
    public static void main(String[] args) {
    public static int multiplica(int a, int b) {
        result = a*b-a;
        return result;
        System.out.println(multiplica(5,6));
    }
    }
}

Traducción guardada en: TraductorPythonAJava.java
gael@LAPTOP-NOOB:~/asmprograms/javaTraductorJava$



