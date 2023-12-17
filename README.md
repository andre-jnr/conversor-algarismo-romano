# Conversor de algarismo romano

Este é um simples conversor de algarismos romanos para inteiros e vice-versa, implementado em Python. Ele inclui uma interface
gráfica básica usando a biblioteca `customtkinter`. Abaixo estão as instruções para entender e utilizar o código.

## Dependências

```
pip install customtkinter
```

## Classe `ConversorRomano`

A classe `ConversorRomano` contém métodos para converter números inteiros para algarismos romanos (`para_romano`) e algarismos
romanos para inteiros (`para_arabico`). Ela utiliza um dicionário (`self.algarismos`) para mapear os símbolos romanos aos seus
valores numéricos.

### Métodos

- `para_romano(numero)`: Converte um número inteiro para algarismos romanos.
- `para_arabico(romano)`: Converte algarismos romanos para um número inteiro.

## Classe `Tela`

A classe `Tela` cria uma interface gráfica para interagir com a funcionalidade de conversão. Ela utiliza a biblioteca
`customtkinter` para criar elementos como rótulos, caixas de seleção e botões.

### Métodos

- `criar_componentes()`: Inicializa e organiza os componentes da interface gráfica.
- `validar_entrada()`: Verifica se a entrada é um número inteiro.
- `converter_para_romano()`: Converte um número inteiro para algarismos romanos e exibe o resultado na interface.
- `converter_para_inteiro()`: Converte algarismos romanos para um número inteiro e exibe o resultado na interface.
- `realizar_conversao()`: Realiza a conversão com base na opção selecionada e chama o método apropriado.

## Utilização

1. Execute o script `Tela.py`.
1. A interface gráfica será exibida.
1. Selecione a conversão desejada (de inteiros para romanos ou de romanos para inteiros).
1. Digite o número inteiro ou os algarismos romanos na caixa de entrada.
1. Clique no botão "Converter".
1. O resultado da conversão será exibido no rótulo.

## Vídeo

- [Assista meu vídeo, onde explico linha por linha.](https://youtu.be/bWEfFRp8-J8)
