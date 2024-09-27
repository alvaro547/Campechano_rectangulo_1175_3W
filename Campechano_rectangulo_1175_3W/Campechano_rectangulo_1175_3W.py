print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Función para calcular el perímetro de un rectángulo
def calcular_perimetro(base, altura):
    """
    Calcula el perímetro de un rectángulo.
    
    Parámetros:
    base (float): La longitud de la base del rectángulo.
    altura (float): La altura del rectángulo.
    
    Retorna:
    float: El perímetro del rectángulo.
    """
    return 2 * (base + altura)

# Función para calcular el área de un rectángulo
def calcular_area(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Parámetros:
    base (float): La longitud de la base del rectángulo.
    altura (float): La altura del rectángulo.
    
    Retorna:
    float: El área del rectángulo.
    """
    return base * altura

# Función principal
def main():
    """
    Función principal que solicita al usuario la base y la altura del rectángulo,
    y luego calcula y muestra el perímetro y el área.
    """
    # Solicitar la base y la altura al usuario
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    
    # Calcular el perímetro y el área
    perimetro = calcular_perimetro(base, altura)
    area = calcular_area(base, altura)
    
    # Mostrar los resultados
    print(f"El perímetro del rectángulo es: {perimetro}")
    print(f"El área del rectángulo es: {area}")

# Ejecutar la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
