'''Peça ao usuário a temperatura da água (em graus Celsius). Determine o estado físico da água 
(sólido, líquido ou gasoso). Regras:
• Temperatura <= 0°C: Sólido
• 0°C < Temperatura < 100°C: Líquido
• Temperatura >= 100°C: Gasoso 
'''

temperatura = float(input("Digite a temperatura da água em °C: "))

if temperatura <= 0:
    print("Sólido")
elif 0 < temperatura < 100:
    print("Líquido")
elif temperatura >= 100:
    print("Gasoso")
else:
    print("Temperatura da água inválida")

