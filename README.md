[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/BdknfvaX)
# Classificador de Triângulos

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

O programa deve 3 números inteiros e imprimir o tipo de triângulo que eles formam.
As respostas possíveis são:

- `Equilátero`: se todos os lados são iguais.
- `Isósceles`: se somente dois lados são iguais.
- `Escaleno`: se todos os lados são diferentes.

No caso dos números não formarem um triângulo, o programa deve imprimir `Não é um triângulo`.

## 👀 Observação

3 números `a`, `b` e `c` formam um triangulo quando todas as desigualdades forem verdadeira:

- `a + b > c`
- `a + c > b`
- `b + c > a`

## 🧪 Testes Automáticos 🧪

Para testar automaticamente o programa **antes** de fazer um commit e enviar o seu trabalho existem algumas formas de fazer isso.

1. executar o módulo `unittest` direto no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python -m unittest
```

2. executar o arquivo `test_main.py` no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python test_main.py
```

3. caso você esteja usando o [VSCode](https://code.visualstudio.com/), você pode abrir a paleta de comandos `CTRL+SHIFT+P` e digitar `Run All Tests`.
4. no seu editor de código, você pode executar o arquivo `test_main.py` e verificar o resultado dos testes no terminal.

## 🤖 Observações Importantes 🤖

- **Não altere o nome dos arquivos**. Os arquivos `test_main.py` e `main.py` precisam ter esses nomes para que os testes funcionem.
- **Não altere o nome das funções**. Os testes dependem que as funções tenham os nomes especificados no enunciado ou já escritos nos arquivos.
- **Não altere o nome dos parâmetros**. Os testes dependem que as funções tenham os parâmetros especificados no enunciado ou já escritos nos arquivos.
- **Antes de fazer um commit**, execute os testes usando um dos métodos acima para verificar se o seu programa está funcionando corretamente.
- **Caso não consiga corrigir os erros**, entre em contato com o professor ou monitores para que eles possam te ajudar.
  Para isso você deve fazer um commit com o seu trabalho incompleto e abrir uma **issue** no repositório do exercício explicando o seu problema.
