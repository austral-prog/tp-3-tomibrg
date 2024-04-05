def check_vowels():
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
    name = input('Ingrese nombre: ')
    name = name.lower()

    vow_a = 'a' in name
    vow_e = 'e' in name
    vow_i = 'i' in name
    vow_o = 'o' in name
    vow_u = 'u' in name

    print(name.title())
    print(f'Contiene a: {vow_a}')
    print(f'Contiene e: {vow_e}')
    print(f'Contiene i: {vow_i}')
    print(f'Contiene o: {vow_o}')
    print(f'Contiene u: {vow_u}')

check_vowels()
