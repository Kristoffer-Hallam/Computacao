# titulo

# input do chat (campo de mensagem)
# cada mensagem que o usuário enviar:
    # mostrar a mensagem que o usuário enviou na tela
    # pegar a pergunta e enviar para a IA responder
    # exibir a resposta da IA na tela
    
# Principais Frameworks para sites e sistemas:
# Flask
# Django
# FastAPI
# >>> Streamlit <<< -> apenas com o Python, cria o frontend e backend
# a IA que vamos usar: OpenAI


import streamlit as st
from var import modelo_ia

st.title("Chat com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem", key="user_input")

# role = quem é o usuário
# content = conteúdo da mensagem

for mensagem in st.session_state["lista_mensanges"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # Podemos usar o ícone com a inicial do Nome do usuário, usuário, assistente (IA)
    st.chat_message("user").write(texto_usuario)
    mensagem_user = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensanges"].append(mensagem_user)
    
    
    # IA responde
    resposta_ia = modelo_ia.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state["lista_mensanges"]
    )
    # print(resposta_ia.choices[0].message.content)
    texto_resposta_ia =  resposta_ia.choices[0].message.content #"Você perguntou" + texto_usuario
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensages"].append(texto_resposta_ia)
