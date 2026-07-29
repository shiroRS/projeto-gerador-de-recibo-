# 🧾 Gerador de Recibo em Python

## 📌 Sobre o projeto

Este projeto consiste em um sistema desenvolvido em **Python** para gerar recibos de compra de forma simples e organizada.

Além da geração do recibo, o projeto agora conta com **impressão direta em impressoras térmicas**, tornando-o uma ótima base para pequenos comércios, feiras e restaurantes.

O programa permite cadastrar o cliente, selecionar diversos produtos, calcular automaticamente o valor total, escolher a forma de pagamento e imprimir o recibo em papel térmico.

---

## ⚙️ Funcionalidades

- ✅ Cadastro do nome do cliente
- ✅ Validação para impedir nome vazio
- ✅ Cadastro do CPF
- ✅ Listagem de produtos disponíveis
- ✅ Seleção de múltiplos produtos
- ✅ Cálculo automático do valor total
- ✅ Escolha da forma de pagamento
  - 💵 Dinheiro
  - 💳 Cartão
  - 📱 Pix
- ✅ Geração automática do recibo
- ✅ Data e hora da compra
- ✅ Campo para assinatura
- ✅ Compatível com impressoras térmicas (58 mm)
- ✅ Impressão direta utilizando a API de impressão do Windows (`pywin32`)
- ✅ QR Code decorativo (ASCII) para pagamentos via Pix

---

## 🛠️ Tecnologias utilizadas

- Python 3
- datetime
- pywin32
- Windows Print API

---

## 📚 Conceitos praticados

Durante o desenvolvimento foram utilizados diversos conceitos da linguagem Python:

- Variáveis
- Listas
- Tuplas
- Dicionários
- Laços (`for` e `while`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Tratamento de exceções (`try` / `except`)
- Funções
- Organização de código
- Impressão utilizando a API do Windows

---

## 🖨️ Compatibilidade

O projeto foi testado com:

- Impressora térmica POS-5890T
- Papel térmico de 58 mm
- Driver Generic / Text Only

---

## 📷 Exemplo de saída

```text
================================
            RECIBO
================================

Cliente: João

CPF: 12345678901

Produtos

- Camisa ............ R$ 80,00
- Tênis ............. R$ 400,00

--------------------------------

Total: R$ 480,00

Pagamento: Pix

Data:
28/07/2026 15:30

--------------------------------

Obrigado pela preferência!

################################
## #### ## ## #### ## #### ## ##
## ##   ## ## ##   ## ##   ## ##
####### #### ####### ####### ###
## ## #### ## #### ## #### ## ##
################################
```

---

## 🚀 Objetivo

Este projeto foi desenvolvido para praticar lógica de programação e conceitos fundamentais de Python, evoluindo posteriormente para um sistema capaz de realizar impressão em impressoras térmicas utilizadas em estabelecimentos comerciais.

Além do aprendizado, o projeto serve como base para futuros sistemas de pedidos e emissão de comprovantes.
