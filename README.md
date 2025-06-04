# Analizador Léxico con Autómata Finito Determinista

## 📘 Descripción general
Este proyecto implementa un **analizador léxico** que detecta si los tokens de un archivo de texto (simulando código fuente) son válidos, utilizando un **Autómata Finito Determinista (AFD)** diseñado y programado en Python.  
El sistema reconoce variables, números, cadenas de texto, operadores y símbolos comunes de un lenguaje tipo C/JavaScript.

## 📁 Archivos del proyecto
- `automata_completo_con_cadenas.jff`: Autómata visual en formato JFLAP.  
- `automata_completo_con_cadenas.txt`: Transiciones del AFD en formato de texto.  
- `prueba.txt`: Archivo de entrada con líneas de código a analizar.  
- `verificador_final.py`: Script que carga el AFD y valida los tokens del archivo.  

🔗 Repositorio:  
[https://github.com/edisson2407/automatas1.git](https://github.com/edisson2407/automatas1.git)

## 🔄 Flujo de funcionamiento
1. Se diseña un AFD que reconoce tokens válidos.  
2. Se transcribe como una lista de transiciones en Python.  
3. Se prepara un archivo de prueba con líneas simuladas de código.  
4. El verificador:  
   - Lee cada línea del archivo.  
   - Extrae los tokens mediante expresiones regulares.  
   - Recorre el AFD para validar cada token.  
   - Muestra si cada token es válido (`✅`) o inválido (`❌`).  

## ⚙️ Componentes del código (`verificador_final.py`)
1. **Transiciones:** Lista que define las reglas de cambio de estado del AFD.  
2. **Construcción del AFD:** Diccionario de diccionarios (`dfa`).  
3. **Estados finales:** `{21, 22}`, donde un token es aceptado.  
4. **`extraer_tokens()`**: Usa regex para separar tokens en una línea.  
5. **`validar_token()`**: Simula el recorrido del AFD para validar cada token.  
6. **`validar_archivo()`**: Aplica las funciones anteriores a todo el archivo de entrada.

## 📄 Archivo de prueba (`prueba.txt`)
Contiene líneas como:
```c
x = 5 ;
nombre = "Juan" ;
apellido = "Pérez" ;
edad = 25 ;
peso = 70.5 ;
altura = 1.75 ;
```

Y estructuras más complejas:
```c
if ( edad >= 18 ) {
    puede_votar = true ;
} else {
    puede_votar = false ;
}

suma = 10 + 15 ;
promedio = ( 8 + 9 + 10 ) / 3 ;
resultado = (promedio >= 14) && (promedio <= 20) ;
```

## ✅ Resultados esperados
```text
Línea 1: x = 5 ;
✅ Token válido: 'x'
✅ Token válido: '='
✅ Token válido: '5'
✅ Token válido: ';'

Línea 2: nombre = "Juan" ;
✅ Token válido: 'nombre'
✅ Token válido: '='
✅ Token válido: '"Juan"'
✅ Token válido: ';'

Línea 3: apellido = "Pérez" ;
✅ Token válido: 'apellido'
✅ Token válido: '='
✅ Token válido: '"Pérez"'
✅ Token válido: ';'

Línea 4: edad = 25 ;
✅ Token válido: 'edad'
✅ Token válido: '='
✅ Token válido: '25'
✅ Token válido: ';'

Línea 5: peso = 70.5 ;
✅ Token válido: 'peso'
✅ Token válido: '='
✅ Token válido: '70.5'
✅ Token válido: ';'

Línea 6: altura = 1.75 ;
✅ Token válido: 'altura'
✅ Token válido: '='
✅ Token válido: '1.75'
✅ Token válido: ';'
```

## 🛠️ Posibles mejoras o extensiones
- Soporte para comentarios: `// comentario` o `/* bloque */`.  
- Reconocimiento de tipos de datos como `int`, `float`, `bool`.  
- Reporte detallado de errores con número de línea y tipo de token inválido.

## 🔍 Autómata
El AFD diseñado reconoce tokens válidos según las reglas del lenguaje.  
Fue construido en JFLAP (`.jff`) y transformado en transiciones para su uso en Python.

- Estado inicial: `0`  
- Estados de aceptación: `21`, `22`

📌 *[Aquí puedes insertar una imagen del autómata]*

## 🧾 Definición del lenguaje
El lenguaje definido incluye:

- **Identificadores:** letras, números y `_`, comenzando con letra o `_`.  
- **Números:**  
  - Enteros: `25`, `100`  
  - Decimales: `3.14`, `70.5`  
- **Cadenas:** `"Hola Mundo"`  
- **Operadores:**  
  - Aritméticos: `+`, `-`, `*`, `/`  
  - Comparación: `==`, `!=`, `>=`, `<=`, `<`, `>`  
  - Lógicos: `&&`, `||`  
  - Asignación: `=`  
- **Delimitadores y símbolos:** `;`, `,`, `(`, `)`, `{`, `}`, `[`, `]`

## ✏️ Sintaxis de las instrucciones
```c
// Asignación
variable = valor ;

// Condicional
if (condición) {
    instrucciones
} else {
    instrucciones
}

// Expresiones
suma = 10 + 20 ;
promedio = (a + b) / 2 ;
resultado = (promedio >= 14) && (promedio <= 20) ;

// Bloques y listas
bloque = { [1, 2, 3] } ;
```

## ✅ Conclusión
Este proyecto demuestra cómo aplicar **autómatas finitos deterministas** para validar léxicamente un conjunto de tokens en un lenguaje estructurado.  
Combina teoría formal de lenguajes con implementación práctica en Python.
