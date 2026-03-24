# Crie um programa que peça ao usuário para digitar
# as dimensões de um retangulo(largura e altura).
# Em seguida, o programa deve calcular e mostrar a 
# área e o perimetro desse retangulo

largura = float(input("Digite a largura do Retângulo: "))
altura = float(input("Digite a altura do Retângulo: "))

perimetro = 2 * (largura + altura)

print(f"O peímetro desse retângulo é: {perimetro}")