def slice_simple():
    texto = "Awesome"
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
    texto = texto.lower()
    lim_1 = len(texto)*1/2-1
    lim_2 = len(texto)*1/2+2 
    print(texto[:3])
    print(texto[int(lim_1):int(lim_2)])
    print(texto[:4] + texto[-3:])
slice_simple()
