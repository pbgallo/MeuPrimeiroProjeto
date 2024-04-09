peso_bagagem = input("Informe o peso da sua bagagem ")
cliente_vip = input("É cliente VIP?")
if cliente_vip == "p":
    if int(peso_bagagem) > 32:
        print("Cliente VIP com bagagem acima do permitido")
    else:
        print("Cliente VIP com peso permitido")
else:
    if int(peso_bagagem) > 28:
        print("Peso acima do permitido")
    else:
        print("O peso da bagagem está permitido")
