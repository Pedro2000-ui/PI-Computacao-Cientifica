def mensagem():
  print("\nBem vindo ao Conversor Pé -> Metros -> Pé")

def converter(opcao, valor):
  if(opcao == 1):
    print(valor, "Pé(s) ->", round(valor * 0.3048, 2), "metro(s)")
  else:
    print(valor, "Metro(s) ->", round(valor * 3.281, 2), "Pé(s)")