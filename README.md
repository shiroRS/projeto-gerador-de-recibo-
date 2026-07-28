# 🧾 Gerador de Recibo em Python

## 📌 Sobre o projeto

Este projeto consiste em um programa desenvolvido em **Python** que gera um recibo de uma compra através das informações inseridas pelo usuário.

O programa permite informar os dados do cliente, selecionar produtos, adicionar vários itens em uma mesma compra, calcular o valor total e escolher a forma de pagamento. Ao final, é exibido um recibo organizado com os dados da compra, data e hora.

---

## ⚙️ Funcionalidades

* ✅ Cadastro do nome do cliente
* ✅ Validação para impedir nome vazio
* ✅ Cadastro do CPF com verificação de quantidade de dígitos
* ✅ Exibição de produtos disponíveis e seus valores
* ✅ Seleção de um ou mais produtos
* ✅ Cálculo automático do valor total da compra
* ✅ Escolha da forma de pagamento:

  * Dinheiro
  * Cartão
  * Pixm (nao gera QRcode)
* ✅ Geração do recibo contendo:

  * Nome do cliente
  * CPF
  * Produtos escolhidos
  * Valor total
  * Forma de pagamento
  * Data e hora
  * Campo para assinatura

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* Biblioteca **datetime** (utilizada para exibir a data e hora do recibo)

---

## 📚 Conceitos praticados

Durante o desenvolvimento do projeto foram utilizados conceitos fundamentais da linguagem Python:

* Variáveis
* Dicionários
* Listas
* Tuplas
* Estruturas de repetição (`while` e `for`)
* Estruturas condicionais (`if`, `elif` e `else`)
* Tratamento de erros com `try` e `except`
* Entrada de dados com `input()`
* Exibição de informações com `print()`

---

## 🎯 Objetivo do projeto

O objetivo deste projeto é praticar lógica de programação em Python, trabalhando com entrada de dados, validações, manipulação de listas e organização de informações para gerar um recibo de compra no terminal.

---

## 📷 Exemplo de saída

```
==================================================
                    RECIBO
==================================================
Nome do Cliente    : João
CPF                : 12345678901

Produtos:
 - camisa - R$80.00
 - tenis - R$400.00

Valor pago         : R$480.00
Forma de Pagamento : pix
Data e Hora        : 28/07/2026 15:30:20

==================================================
        Obrigado pela preferência!
==================================================
```
