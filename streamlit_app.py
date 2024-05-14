import streamlit as st
import google.generativeai as genai
from google.colab import userdata

# Configure API key
api_key = userdata.get('SECRET_KEY')
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

system_instruction = "Como especialista em decoração de interiores altamente qualificado, sua missão é analisar as imagens enviadas e comparar qual transmite mais felicidade através das cores utilizadas na decoração. O objetivo é ajudar os usuários a entender como as cores podem influenciar suas emoções e a criar espaços mais felizes e acolhedores em suas próprias casas. Crie uma tabela listando as características de cada ambiente."

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings,
)

st.title('Análise de Ambientes: Náutico vs. Contemporâneo')

st.write('Vamos explorar como as cores e o design de cada sala podem influenciar a sensação de felicidade.')

imagem1 = st.text_input('Digite o caminho da imagem 1:')
imagem2 = st.text_input('Digite o caminho da imagem 2:')

if st.button('Analisar'):
    prompt = [genai.upload_file(imagem1), genai.upload_file(imagem2), system_instruction]
    response = model.start_chat(prompt)
    st.write(response.text)
