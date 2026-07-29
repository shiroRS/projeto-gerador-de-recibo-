itens = {
    1: ("calca", 190),
    2: ("camisa", 80),
    3: ("tenis", 400),
    4: ("meia", 20),
}

                              #nome

while True:
    nome=input("Digite seu nome: ").strip()
    if nome=="":
        print("O nome não pode estar vazio.".upper())
        print(50*"-")
    else:
        break

print(50*"-")

                             #cpf

while True:
    print(f"Digite seu nome: {nome}")
    cpf=input("Digite seu CPF: ").strip()
    if cpf=="":
        print("O CPF não pode estar vazio.".upper())
    if len(cpf) != 11:
        print("O CPF deve ter 11 dígitos.".upper())
        print(50*"-")
    else:
        break
        
print(50*"-")

                             #produto

prdodutos_escolhidos=[]
total=0

while True:
    print(f"Digite seu nome: {nome}")
    print(f"Digite seu CPF: {cpf}")
    print("escolha um produto:")

    for id, (nome_produto, price) in itens.items():
        print(f"{id}: {nome_produto} - R${price:.2f}")

    try:
        produto = int(input("Digite o número do produto: "))

        if produto not in itens:
            print("Produto inválido. Por favor, escolha um produto válido.".upper())
            continue

        prdodutos_escolhidos.append(itens[produto])
        total+=itens[produto][1]

        continuar=input("deseja continuar comprando? (s/n)")

        if continuar !="s":
            break


    except ValueError:
        print("Por favor, digite um número válido.".upper())
        continue
    

print(50*"-")

                            #forma de pagamento

while True:
    print(f"Digite seu nome: {nome}")
    print(f"Digite seu CPF: {cpf}")
    print("produtos:  ")
    for nome_produto, preco in prdodutos_escolhidos:
        print(f"   -{nome_produto} - R${preco:.2f}")

    print(f"valor total  :R${total:.2f}")  

    pagamento = input("Digite a forma de pagamento (dinheiro/cartão/pix): ").lower()

    if pagamento != "dinheiro" and pagamento != "cartao" and pagamento != "pix":
        print("Forma de pagamento inválida. Por favor, escolha entre dinheiro, cartão ou pix.".upper())
        print(50*"-")
        continue
    else:
       break


if produto ==1:
    produto = itens[1][0]
    preco = itens[1][1]
elif produto ==2:
    produto = itens[2][0]
    preco = itens[2][1]
elif produto ==3:
    produto = itens[3][0]
    preco = itens[3][1]
elif produto ==4:
    produto = itens[4][0]
    preco = itens[4][1]


                          #recibo   



from datetime import datetime

data = datetime.now().strftime("%d/%m/%Y   %H.%M,%S")

                #feito por IA, precisa de uma impressora termica e instalar o driver dela (fiz com IA pq eu n sabia mexer com essa biblioteca)

import win32print #caso tenha ficado amarelo essa linha é completamente normal, funcioma msm assim (causa desconhecido por mim)

printer_name = "Generic / Text Only"  # Nome da sua impressora

texto = "\n"
texto += "=" * 50 + "\n"
texto += "                 RECIBO\n"
texto += "=" * 50 + "\n\n"

texto += f"Nome do Cliente : {nome}\n"
texto += f"CPF             : {cpf}\n"
texto += "Produtos:\n"

for nome_produto, preco in prdodutos_escolhidos:
    texto += f" - {nome_produto} - R${preco:.2f}\n"

texto += f"\nValor pago          : R${total:.2f}\n"
texto += f"Forma de Pagamento  : {pagamento}\n"
texto += f"Data e Hora         : {data}\n"

if pagamento=="pix":
    texto +=("        QR code")
    texto += (r"""
+----------------------+
| ## ## #### ## ## ## |
| ##    ##   ##    ## |
| ###### ## ###### ## |
| ## ## #### ## ## ## |
| ## ###### ###### ## |
| ##    ## ## ##    ##|
| #### #### #### #### |
| ## ## ## #### ## ## |
+----------------------+
""")

texto += "-" * 50 + "\n"
texto += "Declaro ter recebido a importância acima\n"
texto += "referente ao produto descrito neste recibo.\n"
texto += "-" * 50 + "\n\n"

texto += f"____________________ {nome} ____________________\n"
texto += "Assinatura do Recebedor\n\n"

texto += "=" * 50 + "\n"
texto += "Obrigado pela preferência!\n"
texto += "=" * 50 + "\n\n"

hPrinter = win32print.OpenPrinter(printer_name)

try:
    win32print.StartDocPrinter(hPrinter, 1, ("Recibo", None, "RAW"))
    win32print.StartPagePrinter(hPrinter)

    win32print.WritePrinter(hPrinter, texto.encode("cp850"))

    win32print.EndPagePrinter(hPrinter)
    win32print.EndDocPrinter(hPrinter)

finally:
    win32print.ClosePrinter(hPrinter)





                    #feito por mim (executa no terminal)


# print("\n")
# print("=" * 50)
# print("                 RECIBO")
# print("=" * 50)

# print(f"Nome do Cliente    : {nome}")
# print(f"CPF                : {cpf}")
# print("produtos:  ")
# for nome_produto, preco in prdodutos_escolhidos:
#     print(f" -{nome_produto} - R${preco:.2f}")
    
# print(f"valor pago   :R${total:.2f}")  
# print(f"Forma de Pagamento : {pagamento}")
# print(f"Data e Hora        : {data}")

# print("-" * 50)
# print("Declaro ter recebido a importância acima")
# print("referente ao produto descrito neste recibo.")
# print("-" * 50)

# print("\n")
# print(f"____________________{nome}____________________")
# print("Assinatura do Recebedor")

# print("=" * 50)
# print("        Obrigado pela preferência!")
# print("=" * 50)
# print("\n")