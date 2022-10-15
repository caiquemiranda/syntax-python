## Classe

Python é uma linguagem que suporta o paradigma de programação orientada a objetos. Como outras linguagens OOP, Python tem classes que são wireframes de objetos definidos. Python suporta herança de classe. Uma classe pode ter muitas subclasses, mas só pode herdar diretamente de uma superclasse.

> Sintaxe:

```{python}
class NomeDaClasse(objeto):
    
    """Esta é uma aula"""
    
    variável_classe
    
    def _init_(self,*args):
        self.args = args
    
    def _repr_(self):
        return "Algo para representar o objeto como uma string"
    
    def other_method(self,*args):
        #faça outra coisa
```

> Exemplo:

```{python}
class Cavalo(objeto):

    """Cavalo representa um Cavalo"""

    espécie = "Equus ferus caballus"

    def _init_(self,color,weight,wild=False):
        self.color = cor
        self.weight = peso
        self.wild = selvagem

    def _repr_(self):
        return "%s cavalo pesando %fe estado selvagem é %b" % (self.color,self.weight,self.wild)

    def make_sound(self):
        imprima "neighh"

    def movimento(auto):
        retornar "andar"
```

> Sintaxe:

```{python}
class NomeDaClasse(SuperClasse):
    # o mesmo que acima
    # use a palavra-chave 'super' para obter de cima
```

> Exemplo:

```{python}
class CavalodeCorrida(Cavalo):
    
    """Um cavalo mais rápido que herda de Cavalo"""
    
    def movimento(auto):
        retornar "executar"
    
    def movimento_lento(self):
        return super(Cavalo,auto).movimento()
    
    def _repr_(self):
        return "%s cavalo de corrida pesando %fe status selvagem é %b" (self.color,self.weight,self.wild)
```

```{python}
>> cavalo3 = RaceHorse("branco",200)
>> print(cavalo3.movement_slow())
"andar"
>> print(cavalo3.movimento())
"corre"
```

## Comentários

### Comentários de linha única

Aumentar o código com descrições legíveis por humanos pode ajudar a documentar as decisões de design.

> Exemplo:

```{python}
# este é um comentário de linha única.
```

### Comentários de várias linhas

Alguns comentários precisam abranger várias linhas, use isso se você tiver mais de 4 comentários de linha única em uma linha.

> Exemplo:

```{python}
'''
isto é
uma multilinha
comentar, eu sou útil para comentar todo
pedaços de código muito rápido
'''
```

## Dicionários

Os dicionários são o tipo de dados associativo integrado do Python. Um dicionário é feito de pares chave-valor onde cada chave corresponde a um valor. Assim como os conjuntos, os dicionários não são ordenados. Algumas notas sobre chaves e valores: A chave deve ser imutável e passível de hash, enquanto o valor pode ser de qualquer tipo. Exemplos comuns de chaves são tuplas, strings e números. Um único dicionário pode conter chaves de vários tipos e valores de vários tipos.

> Sintaxe:

```{python}
dict() #cria um novo dicionário vazio
{} #cria um novo dicionário vazio
```

> Exemplo:

```{python}
>> my_dict = {}
>> content_of_value1 = "abcd"
>> content_of_value2 = "wxyz"
>> my_dict.update({"key_name1":content_of_value1})
>> my_dict.update({"key_name2":content_of_value2})
>> meu_dict
{'key_name1':"abcd", 'key_name2':"wxyz"}
>> my_dict.get("key_name2")
"W x y Z"
```

> Sintaxe:
```{python}
{chave1:valor1,chave2:valor2}
```

> Exemplo:

```{python}
>> my_dict = {"key1":[1,2,3],"key2":"Sou uma string",123:456}
>> my_dict["key1"] #[1,2,3]
>> my_dict[123] #456
>> my_dict["new key"] = "Novo valor"
>> imprimir meu_dict
{"key2":"Sou uma string", "new key":"Novo valor", "key1":[1,2,3],123:456}
```

## Funções

As funções do Python podem ser usadas para abstrair pedaços de código para usar em outro lugar.

> Sintaxe:

```{python}
def nome_da_função(parâmetros):
  # Algum código aqui
```

> Exemplo:

```{python}
def add_two(a, b):
  c = a + b
  retornar c

# ou sem a atribuição provisória a c
def add_two(a, b):
  retornar a + b
```

> Sintaxe:

```{python}
def function_name(parâmetros, named_default_parameter=valor):
  # Algum código aqui
```

> Exemplo:

```{python}
def shout(exclamation="Ei!"):
  print(exclamação)

shout() # Exibe "Ei!"

shout("Cuidado!") # Exibe "Cuidado!"
```
### Objetos de função

As funções Python são objetos de primeira classe, o que significa que podem ser armazenadas em variáveis ​​e listas e podem até ser retornadas por outras funções.

> Exemplo:

```{python}
# Armazenando objetos de função em variáveis:

def diga_olá(nome):
  return "Olá," + nome

foo = say_hello("Alice")
# Agora o valor de 'foo' é "Olá, Alice"

divertido = diga_olá

# Agora o valor de 'fun' é um objeto de função que podemos usar como a 

função original:
bar = diversão("Bob")

# Agora o valor de 'bar' é "Hello, Bob"
```

> Exemplo:

```{python}
# Retornando funções de funções

# Uma função simples
def say_hello(saudável, saudado):
  return "Olá, " + saudação + ", sou " + saudação + "."

# Podemos usar assim:
print say_hello("Alice", "Bob") # Exibe "Olá, Bob, eu sou Alice."

# Também podemos usá-lo em uma função:
def Produce_greeting_from_alice(saudado):
  return say_hello("Alice", saudado)

print Produce_greeting_from_alice("Bob") # Exibe "Olá, Bob, sou Alice."

# Também podemos retornar uma função de uma função aninhando-as:
def Produce_greeting_from(greeter):
  def saudar (cumprimento):
    return say_hello(cumprimento, saudado)
  retorno saudar

# Aqui criamos uma função de saudação para Eva:
Produce_greeting_from_eve = Produce_greeting_from("Eve")

# 'produce_greeting_from_eve' agora é uma função:
print Produce_greeting_from_eve("Alice") # Exibe "Olá, Alice, eu sou Eve."

# Você também pode invocar a função diretamente se quiser:
print Produce_greeting_from("Bob")("Eve") # Exibe "Olá, Eve, eu sou Bob."
```

> Exemplo:

```{python}
# Usando funções em um dicionário em vez de instruções if longas:

# Digamos que temos uma variável chamada 'current_action' e queremos que coisas aconteçam com base em seu valor:

if current_action == 'PAUSE':
  pausa()

elif current_action == 'RESTART':
  reiniciar()

elif current_action == 'RESUME':
  retomar()

# Isso pode ficar longo e complicado se houver muitos valores.
# Em vez disso, podemos usar um dicionário:

resposta_dict = {
  'PAUSA': pausa,
  'REINICIAR': reiniciar,
  'RESUMO': currículo
}

response_dict[current_action]() # Obtém a função correta de response_dict e a chama
```

## len()

O uso de len(some_object) retorna o número de itens de nível superior contidos no objeto que está sendo consultado.

> Sintaxe:

```{python}
len(iterável)
```

> Exemplo:

```{python}
>> minha_lista = [0,4,5,2,3,4,5]
>> len(minha_lista)
7

>> minha_string = 'abcdef'
>> len(minha_string)
6
```
## Compreensão da lista

Maneiras convenientes de gerar ou extrair informações de listas.

> Sintaxe:

```{python}
[variável for variável in condição iterável]
[variável for variável in iterável]
```

> Exemplo:

```{python}
>> lista_x = [1,2,3,4,5,6,7]
>> even_list = [num for num in x_list if (num % 2 == 0)]
>> lista_par
[2,4,6]

>> m_list = ['AB', 'AC', 'DA', 'FG', 'LB']
>> A_list = [duo para duo em m_list if ('A' em duo)]
>> A_lista
['AB', 'AC', 'DA']
```

## Listas

Um tipo de dados Python que contém uma coleção ordenada de valores, que podem ser de qualquer tipo. As listas são o tipo de dados mutável ordenado do Python. Ao contrário das tuplas, as listas podem ser modificadas no local.

> Exemplo:

```{python}
>> x = [1, 2, 3, 4]
>> y = ['spam', 'ovos']
>> x
[1, 2, 3, 4]
>> e
['spam','ovos']

>> y.append('mash')
>> e
['spam', 'ovos', 'mash']

>> y += ['feijão']
>> e
['spam', 'ovos', 'mash', 'feijão']
```

## Rotações

### For Loops

Python fornece uma sintaxe de iteração limpa. Observe os dois pontos e o recuo.

> Exemplo:

```{python}
>> for i no range(0, 3):
>> print(i*2)
0
2
4

>> m_list = ["Senhor", "Lancelot", "Coco"]
>> for item in m_list:
>> print(item)
Senhor
Lancelot
Cocos

>> w_string = "Rápido"
>> for letra in w_string:
>> print(carta)
S
W
eu
f
t
```

### While Loops

Um loop While permite que o código seja executado repetidamente até que uma determinada condição seja atendida. Isso é útil se o número de iterações necessárias para concluir uma tarefa for desconhecido antes do fluxo entrar no loop.

> Sintaxe:

```{python}
while condição:
    //faça alguma coisa
```

> Exemplo:

```{python}
>> looping_needed = True
>>
>> while looping_necessário:
>> # alguma operação em dados
>> if condição:
>> looping_needed = False
```

## print()

Uma função para exibir a saída de um programa. Usar a versão entre parênteses é sem dúvida mais consistente.

> Exemplo:

```{python}
>> # isso funcionará em todas as versões modernas do Python
>> print("algum texto aqui")
"algum texto aqui"

>> # mas isso só funciona em versões do Python inferiores a 3.x
>> print "algum texto aqui também"
"algum texto aqui também"
```

## range()

A função range() retorna uma lista de inteiros, cuja sequência é definida pelos argumentos passados ​​a ela.

> Sintaxe:

```{python}
variações de argumentos:
range(terminal)
range(início, terminal)
range(start, terminal, step_size)
```

> Exemplo:

```{python}
>> range(4)
[0, 1, 2, 3]

>> range(2, 8)
[2, 3, 4, 5, 6, 7]

>> range(2, 13, 3)
[2, 5, 8, 11]
```

## Sets

Conjuntos são coleções de itens únicos, mas não ordenados. É possível converter certos iteráveis ​​em um conjunto.

> Exemplo:

```{python}
>> novo_conjunto = {1, 2, 3, 4, 4, 4,'A', 'B', 'B', 'C'}
>> novo_conjunto
{'A', 1, 'C', 3, 4, 2, 'B'}

>> lista_dup = [1,1,2,2,2,3,4,55,5,5,6,7,8,8]
>> set_from_list = set(dup_list)
>> set_from_list
{1, 2, 3, 4, 5, 6, 7, 8, 55}
```

## Slice

Uma maneira Pythonic de extrair "fatias" de uma lista usando uma notação de colchetes especial que especifica o início e o fim da seção da lista que você deseja extrair. Deixar o valor inicial em branco indica que você deseja começar no início da lista, deixar o valor final em branco indica que deseja ir até o final da lista. Usar um valor negativo referencia o final da lista (de modo que em uma lista de 4 elementos, -1 significa o 4º elemento). O fatiamento sempre produz outra lista, mesmo ao extrair um único valor.

> Exemplo:

```{python}
>> # Especificando um início e um fim:
>> x = [1, 2, 3, 4]
>> x[2:3]
[3]

>> # Especificando início no início e fim no segundo elemento
>> x[:2]
[1, 2]

>> # Especificando iniciar no penúltimo elemento e ir até o final
>> x[-2:]
[3, 4]

>> # Especificando iniciar no início e ir para o penúltimo elemento
>> x[:-1]
[1, 2, 3]

>> # Especificar um argumento step retorna cada n-ésimo item
>> y = [1, 2, 3, 4, 5, 6, 7, 8]
>> s[::2]
[1, 3, 5, 7]

>> # Retorna uma versão invertida da lista ( ou string )
>> x[::-1]
[4, 3, 2, 1]

>> # String reversa
>> my_string = "Aloha"
>> minha_string[::-1]
"aholA"
```

## str()

O uso da função str() permite representar o conteúdo de uma variável como uma string, desde que o tipo de dados da variável forneça uma maneira simples de fazer isso. str() não altera a variável no lugar, ela retorna uma versão 'stringified' dela. Em uma nota mais técnica, str() chama o método especial _str_ do objeto passado para ele.

> Sintaxe:

```{python}
str(objeto)
```

> Exemplo:

```{python}
>> # tais recursos podem ser úteis para concatenar strings
>> minha_var = 123
>> minha_var
123

>> str(minha_var)
'123'

>> my_booking = "Voo da DB Airlines " + str(my_var)
>> minha_reserva
'Voo 123 da DB Airlines'
```

### Strings

Strings armazenam caracteres e possuem muitos métodos de conveniência integrados que permitem modificar seu conteúdo. Strings são imutáveis, o que significa que não podem ser alteradas no lugar.

> Exemplo:

```{python}
>> my_string1 = "esta é uma string válida"
>> my_string2 = 'esta também é uma string válida'
>> my_string3 = 'isto é' + ' ' + 'também' + ' ' + 'uma string'
>> minha_string3
"isso também é uma string"
```
### Tuplas

Um tipo de dados Python que contém uma coleção ordenada de valores, que podem ser de qualquer tipo. Tuplas Python são "imutáveis", o que significa que elas não podem ser alteradas uma vez criadas.

> Exemplo:

```{python}
>> x = (1, 2, 3, 4)
>> y = ('spam', 'ovos')

>> minha_lista = [1,2,3,4]
>> minha_tupla = tupla(minha_lista)
>> minha_tupla
(1, 2, 3, 4)
```

### Atribuição de Tuplas

Tuplas podem ser expandidas em variáveis facilmente.

> Exemplo:

```{python}
nome, idade = ("Alice", 19)
# Agora nome tem o valor "Alice" e idade tem o valor 19

# Você também pode omitir os parênteses:
nome, idade = "Alice", 19
```

### Variáveis

As variáveis são atribuídas a valores usando o operador =, que não deve ser confundido com o sinal == usado para testar a igualdade. Uma variável pode conter quase qualquer tipo de valor, como listas, dicionários, funções.

> Exemplo:

```{python}
>> x = 12
>> x
12
```