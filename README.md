### 1. Clonar o Repositório

```bash
git clone (https://github.com/indiarasabarreto/whatsapp_automation_project.git)
cd whatsapp_automation_project
```

### 2. Criar e Ativar um Ambiente Virtual

É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

```bash
python3 -m venv venv
source venv/bin/activate  # No Linux/macOS
# venv\Scripts\activate   # No Windows
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Iniciar o Servidor da API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000/`.

Você pode acessar a documentação interativa da API (Swagger UI) em `http://127.0.0.1:8000/docs`.

### Testando a API

Para testar o endpoint `/webhook`, você pode usar ferramentas como `curl` ou Postman. Exemplo usando `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/webhook" \
     -H "Content-Type: application/json" \
     -d '{"from_number": "+5511999999999", "message_body": "Qual o horário de funcionamento?"}'
```

Ou para testar uma pergunta que não está nas FAQs:

```bash
curl -X POST "http://127.0.0.1:8000/webhook" \
     -H "Content-Type: application/json" \
     -d '{"from_number": "+5511999999999", "message_body": "Gostaria de saber sobre promoções."}'
```

## Estrutura do Projeto

*   `whatsapp_automation_project/`
    *   `app/`
        *   `main.py`: Contém a lógica principal da API, endpoints e o banco de dados de FAQs em memória.
    *   `requirements.txt`: Lista as dependências do Python.
    *   `README.md`: Este arquivo, descrevendo o projeto.

## Próximos Passos e Melhorias Potenciais

Este MVP pode ser expandido com as seguintes funcionalidades:

*   **Integração Real com WhatsApp:** Utilizar APIs oficiais do WhatsApp (ex: Twilio, Meta Cloud API) para envio e recebimento de mensagens.
*   **Banco de Dados Persistente:** Substituir o banco de dados em memória por um banco de dados relacional (PostgreSQL, MySQL) ou NoSQL para armazenar FAQs e logs de conversas.
*   **Interface de Gerenciamento:** Desenvolver um painel web para gerenciar FAQs, visualizar conversas e configurar o chatbot.
*   **Processamento de Linguagem Natural (NLP):** Integrar com bibliotecas de NLP (ex: NLTK, SpaCy) ou serviços de IA (ex: Dialogflow, Rasa) para um entendimento mais sofisticado das mensagens.
*   **Atendimento Humano:** Implementar a lógica de encaminhamento para um agente humano, com notificação e histórico da conversa.

## Autor

**Indiara dos Santos Sá Barreto**
*   [GitHub](https://github.com/indiarasabarreto/whatsapp_automation_project.git)
*   [LinkedIn](https://www.linkedin.com/in/indiara-sa-barreto/)

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (Recomendado criar um arquivo LICENSE no repositório.)