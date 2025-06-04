from collections import defaultdict
import re

# TRANSICIONES DEL AUTÓMATA COMPLETO ()
transiciones = [
    ("0", "L", "1"), ("0", "D", "2"), ("0", "+", "5"), ("0", "-", "5"), ("0", "*", "5"),
    ("0", "/", "5"), ("0", "=", "6"),                     # solo "="
    ("0", "!", "19"), ("0", ">", "50"), ("0", "<", "52"),
    ("0", "(", "7"), ("0", ")", "7"), ("0", ";", "23"),
    ("0", '"', "30"), ("0", "{", "32"), ("0", "}", "32"),
    ("0", "[", "33"), ("0", "]", "33"), ("0", "&", "34"),
    ("0", "|", "36"), ("0", ",", "54"), ("0", "_", "1"),

    ("1", "L", "1"), ("1", "D", "1"), ("1", "_", "1"), ("1", " ", "21"),
    ("2", "D", "2"), ("2", ".", "3"), ("2", " ", "21"),
    ("3", "D", "4"), ("4", "D", "4"), ("4", " ", "21"),
    ("5", " ", "21"), ("6", " ", "21"), ("7", " ", "21"),
    ("19", "=", "20"), ("20", " ", "22"),
    ("23", " ", "21"),
    ("30", "ANY", "30"), ("30", '"', "31"), ("31", " ", "21"),
    ("32", " ", "21"), ("33", " ", "21"),
    ("34", "&", "35"), ("35", " ", "21"),
    ("36", "|", "37"), ("37", " ", "21"),
    ("50", "=", "51"), ("51", " ", "21"),
    ("52", "=", "53"), ("53", " ", "21"),
    ("54", " ", "21")
]

dfa = defaultdict(dict)
for from_state, symbol, to_state in transiciones:
    dfa[int(from_state)][symbol] = int(to_state)

final_states = {21, 22}

def extraer_tokens(linea):
    # Detecta cadenas, separa símbolos y palabras, y divide comas correctamente
    tokens = re.findall(r'"[^"]*"|[A-Za-z_]\w*|[<>!=]=|&&|\|\||\d+\.\d+|\d+|[{}[\]();=+\-*/<>,]', linea)
    return tokens


def validar_token(token):
    token = token.strip()

    # Validación directa para operadores dobles
    if token in ["==", "!=", ">=", "<=", "&&", "||"]:
        return True, f"✅ Token válido: '{token}'"

    # Validación directa para "="
    elif token == "=":
        state = dfa[0]["="]
        if " " in dfa[state]:
            state = dfa[state][" "]
            return (state in final_states), f"✅ Token válido: '{token}'"
        else:
            return False, f"❌ Token inválido: '{token}' en estado q{state}'"

    # Validación general carácter por carácter
    state = 0
    i = 0
    while i < len(token):
        char = token[i]
        if char.isalpha():
            symbol = "L"
        elif char.isdigit():
            symbol = "D"
        elif char == " ":
            symbol = " "
        elif char == '"':
            symbol = '"'
        elif char in "+-*/=!();{}[]&|.,_><":
            symbol = char
        else:
            symbol = "ANY"

        if symbol in dfa[state]:
            state = dfa[state][symbol]
            i += 1
        elif "ANY" in dfa[state] and char != '"':
            state = dfa[state]["ANY"]
            i += 1
        else:
            return False, f"❌ Token inválido: '{token}' en estado q{state}'"

    if " " in dfa[state]:
        state = dfa[state][" "]
    return (state in final_states), f"✅ Token válido: '{token}'" if state in final_states else f"❌ Token inválido al finalizar: '{token}'"

def validar_archivo(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        for num_linea, linea in enumerate(f, 1):
            print(f"\n🧾 Línea {num_linea}: {linea.strip()}")
            tokens = extraer_tokens(linea)
            for token in tokens:
                resultado, mensaje = validar_token(token)
                print(mensaje)

# Nombre del archivo a validar
archivo = "prueba.txt"

if __name__ == "__main__":
    validar_archivo(archivo)
