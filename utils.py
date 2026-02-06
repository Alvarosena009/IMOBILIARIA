def validar_entrada(tipo, valor):
    if tipo == 'quartos' and valor not in [1, 2]:
        raise ValueError("Quartos devem ser 1 ou 2.")
    return valor