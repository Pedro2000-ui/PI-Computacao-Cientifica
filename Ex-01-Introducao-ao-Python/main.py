#  Fazer um módulo que converte
#  Pé -> Metros -> Pé: Entrada do usuário que define a conversão
#  1 pé = 0,3048 metros
#  1 metro = 3,281 pés

import os
import conversor

while True:
  conversor.mensagem()
  while True:
    print("[1] - Pé -> Metros \n[2] - Metros -> Pé")
    opcao = int(input("Escolha a opção desejada: "));
    if(opcao == 1 or opcao == 2):
      break;
    print("Opção inválida!")
  
  valor = float(input("Digite o valor a ser convertido: "));
  conversor.converter(opcao, valor)

  continuar = int(input("\nPara realizar outra conversão digite [1]\n"))
  if(continuar != 1):
    print("\nAté a próxima!")
    break;
  os.system('clear')