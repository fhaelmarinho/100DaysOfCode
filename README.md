# 100DaysOfCode

![100days-course](https://github.com/user-attachments/assets/17077a94-288d-43b4-add9-29845b9adbb7)


Por incentivo de um amigo decidi participar do desafio hashtag#100DaysOfCode e compartilhar meu progresso diariamente, desde algoritmos bastante simples a projetos intermediários e avançados.
A ideia proposta é cri### 🚀 Desafio 100 Dias de Código - Dia 10/100 💻

No décimo dia do **Desafio dos 100 Dias de Código**, desenvolvi uma **API simples utilizando Flask** para realizar operações com dados de um arquivo CSV. Este projeto foi uma excelente oportunidade para explorar o desenvolvimento de APIs RESTful e a manipulação de dados com a biblioteca `pandas`.

---

### 📝 Objetivo do projeto

O objetivo principal foi criar uma API que:
1. **Exponha dados de um arquivo CSV**:
   - O arquivo advertising.csv contém informações de vendas e outros dados relacionados.
2. **Forneça um endpoint para calcular o total de vendas**:
   - A API lê os dados do CSV, calcula o total de vendas e retorna o resultado em formato JSON.
3. **Permita fácil acesso aos dados**:
   - A API pode ser acessada por outros sistemas ou usuários para obter informações de forma programática.

Este projeto simula uma funcionalidade comum em sistemas de análise de dados, onde APIs são usadas para expor informações de forma estruturada.

---

### 🧩 Como o código foi construído?

#### 1. **Importação de bibliotecas**
```python
from flask import Flask, jsonify
import pandas as pd
```
- **`Flask`**:
  - Usado para criar a API e definir os endpoints.
- **`pandas`**:
  - Usado para manipular os dados do arquivo CSV.

---

#### 2. **Inicialização do aplicativo Flask**
```python
app = Flask(__name__)
```
- O objeto `app` é criado a partir da classe `Flask`.
- Ele será usado para definir os endpoints e executar o servidor.

---

#### 3. **Definição do endpoint raiz (`/`)**
```python
@app.route('/', methods=['GET'])
def home():
    return "API está funcionando!"
```
- Este é o endpoint raiz da API.
- Quando acessado via método HTTP `GET`, ele retorna a mensagem `"API está funcionando!"`.
- Serve como um ponto de verificação para garantir que a API está ativa.

---

#### 4. **Definição do endpoint `/total_vendas`**
```python
@app.route('/total_vendas', methods=['GET'])
def get_total_vendas():
    tabela = pd.read_csv('advertising.csv')
    total_vendas = tabela['Vendas'].sum()
    return jsonify({'Total Vendas': total_vendas})
```
- Este endpoint é acessado via método HTTP `GET` e realiza as seguintes operações:
  1. **Leitura do arquivo CSV**:
     - O arquivo `advertising.csv` é lido usando a função `pd.read_csv`.
  2. **Cálculo do total de vendas**:
     - A coluna `Vendas` do CSV é somada usando o método `sum()`.
  3. **Retorno do resultado**:
     - O total de vendas é retornado em formato JSON usando a função `jsonify`.

---

#### 5. **Execução do servidor**
```python
app.run()
```
- O método `run()` inicia o servidor Flask, permitindo que a API seja acessada localmente (por padrão, em `http://127.0.0.1:5000`).

---

### 🛠️ Como funciona?

1. **Início do servidor**:
   - O servidor Flask é iniciado com o comando `python day10.py`.
   - A API fica disponível localmente em `http://127.0.0.1:5000`.

2. **Acesso ao endpoint raiz (`/`)**:
   - Quando o usuário acessa `http://127.0.0.1:5000/`, a API retorna a mensagem:
     ```
     API está funcionando!
     ```

3. **Acesso ao endpoint `/total_vendas`**:
   - Quando o usuário acessa `http://127.0.0.1:5000/total_vendas`, a API:
     - Lê o arquivo `advertising.csv`.
     - Calcula o total de vendas.
     - Retorna o resultado em formato JSON, por exemplo:
       ```json
       {
           "Total Vendas": 12345.67
       }
       ```

---

### 📌 Aprendizados

- **Criação de APIs com Flask**:
  - Aprendi a criar endpoints e retornar dados em formato JSON.
- **Manipulação de dados com `pandas`**:
  - Trabalhei com leitura de arquivos CSV e cálculos simples.
- **Integração de bibliotecas**:
  - Integrei `Flask` e `pandas` para criar uma API funcional e eficiente.
- **Estrutura de APIs RESTful**:
  - Entendi como estruturar endpoints para expor funcionalidades específicas.

---

### 🚀 Próximos passos

Nos próximos dias, pretendo:
1. Adicionar mais endpoints para realizar outras operações com os dados do CSV, como médias ou filtros.
2. Melhorar o tratamento de erros, por exemplo, verificando se o arquivo CSV existe antes de tentar lê-lo.
3. Implementar autenticação na API para restringir o acesso a usuários autorizados.

---

💡 **Dica**: Este projeto é uma ótima introdução ao desenvolvimento de APIs e manipulação de dados com Python. Ele pode ser expandido para incluir funcionalidades mais avançadas, como autenticação, filtros dinâmicos e integração com bancos de dados. 🚀 #100DaysOfCode #Python #APIs3. **Acesso ao endpoint `/total_vendas`**:
   - Quando o usuário acessa `http://127.0.0.1:5000/total_vendas`, a API:
     - Lê o arquivo `advertising.csv`.
     - Calcula o total de vendas.
     - Retorna o resultado em formato JSON, por exemplo:
       ```json
       {
           "Total Vendas": 12345.67
       }
       ```

---

### 📌 Aprendizados

- **Criação de APIs com Flask**:
  - Aprendi a criar endpoints e retornar dados em formato JSON.
- **Manipulação de dados com `pandas`**:
  - Trabalhei com leitura de arquivos CSV e cálculos simples.
- **Integração de bibliotecas**:
  - Integrei `Flask` e `pandas` para criar uma API funcional e eficiente.
- **Estrutura de APIs RESTful**:
  - Entendi como estruturar endpoints para expor funcionalidades específicas.

---

### 🚀 Próximos passos

Nos próximos dias, pretendo:
1. Adicionar mais endpoints para realizar outras operações com os dados do CSV, como médias ou filtros.
2. Melhorar o tratamento de erros, por exemplo, verificando se o arquivo CSV existe antes de tentar lê-lo.
3. Implementar autenticação na API para restringir o acesso a usuários autorizados.

---

💡 **Dica**: Este projeto é uma ótima introdução ao desenvolvimento de APIs e manipulação de dados com Python. Ele pode ser expandido para incluir funcionalidades mais avançadas, como autenticação, filtros dinâmicos e integração com bancos de dados. 🚀 #100DaysOfCode #Python #APIs
Então vamos lá. Bora codar 🚀

Day 0 - Hello World</br>
Day 1 - Receber dados e salvar em uma lista</br>
Day 2 - Cálculo de tempo e cobrança de estacionamento</br>
Day 3 - Conversor de PDF para DOCX</br>
Day 4 - Gerador de QR Code</br>
Day 5 - Removedor de background </br>
Day 6 - Sistema bancário com as principais operações </br>
Day 7 - Script de envio de mensagens pelo whatsapp</br>
Day 8 - Chapéu Seletor de Hogwarts</br>
Day 9 - Conversor de moedas BRL --> [USD/ EUR/ BTC]</br>
Day 10 - Criação de API com Flask com endpoint para calcular de vendas