from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="WhatsApp Automation API", description="MVP para automação de respostas no WhatsApp")

# Modelo para as FAQs (Perguntas e Respostas)
class FAQ(BaseModel):
    question: str
    answer: str
    keywords: List[str]

# Banco de dados em memória para o MVP
faq_db = [
    FAQ(
        question="Qual o horário de funcionamento?",
        answer="Nosso horário de funcionamento é de segunda a sexta, das 08:00 às 18:00.",
        keywords=["horário", "funcionamento", "aberto", "fecha"]
    ),
    FAQ(
        question="Quais são os serviços oferecidos?",
        answer="Oferecemos soluções de automação, desenvolvimento de APIs e consultoria em TI.",
        keywords=["serviços", "oferece", "faz", "trabalha"]
    ),
    FAQ(
        question="Como posso falar com um atendente?",
        answer="Vou te encaminhar para um de nossos especialistas. Por favor, aguarde um momento.",
        keywords=["atendente", "humano", "especialista", "pessoa", "falar com alguém"]
    )
]

# Modelo para a mensagem recebida do WhatsApp (simplificado)
class WhatsAppMessage(BaseModel):
    from_number: str
    message_body: str

@app.get("/")
async def root():
    return {"message": "WhatsApp Automation API is running!"}

@app.post("/webhook")
async def webhook(message: WhatsAppMessage):
    """
    Endpoint que recebe as mensagens do WhatsApp e processa a resposta automática.
    """
    incoming_msg = message.message_body.lower()
    response_text = "Desculpe, não entendi sua pergunta. Gostaria de falar com um atendente?"

    # Lógica simples de busca por palavras-chave
    for faq in faq_db:
        if any(keyword in incoming_msg for keyword in faq.keywords):
            response_text = faq.answer
            break

    # Aqui entraria a integração real com a API do WhatsApp (ex: Twilio ou Meta Cloud API)
    # Por enquanto, apenas simulamos a resposta
    print(f"Recebido de {message.from_number}: {message.message_body}")
    print(f"Resposta enviada: {response_text}")

    return {
        "status": "success",
        "received_message": message.message_body,
        "sent_response": response_text
    }

@app.get("/faqs", response_model=List[FAQ])
async def get_faqs():
    """
    Retorna a lista de FAQs configuradas.
    """
    return faq_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)