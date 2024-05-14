!pip install -q -U google-generativeai
     

# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
from google.colab import userdata
api_key = userdata.get('SECRET_KEY')
genai.configure(api_key=api_key)
     

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}
     

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

     

system_instruction = "Como especialista em decoração de interiores altamente qualificado, sua missão é analisar as imagens enviadas e compara qual transmite mais felicidade através das cores utilizadas na decoração. O objetivo é ajudar os usuários a entender como as cores podem influenciar suas emoções e a criar espaços mais felizes e acolhedores em suas próprias casas. Crie uma tabela listando as caracteristicas de cada ambiente.\n\n\n"
     

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)
     

chat = model.start_chat(history=[
  {
    "role": "model",
    "parts": ["## Comparando Ambientes Náutico e Contemporâneo:\n\nEmbora ambas as salas apresentem um estilo elegante, elas exploram diferentes sensações através de suas escolhas de cores e elementos de design:\n\n**Sala Náutica:**\n\n* **Sensação:** Tranquila, serena, sofisticada, com um toque de informalidade.\n* **Cores:** Azul marinho e branco dominam, evocando a calma e a vastidão do mar. Toques de azul claro e amarelo nas almofadas trazem um pouco de vivacidade sem quebrar a serenidade.\n* **Destaques:** Sofá branco,  tapetes listrados, elementos decorativos com temática marinha como quadros e estampas, materiais naturais como madeira e corda nos pufes.\n\n**Sala Contemporânea:**\n\n* **Sensação:** Sofisticada, masculina,  moderna, com um toque de dramaticidade.\n* **Cores:**  Paleta neutra com predominância de preto, cinza e marrom, transmitindo elegância e serenidade.\n* **Destaques:** Mobiliário de linhas retas e simples,  decoração minimalista com poucos objetos, tapete de pelo alto para um toque de aconchego.\n\n**Comparação:**\n\n| Característica     | Sala Náutica     | Sala Contemporânea |\n|------------------ | ---------------- | ------------------ |\n| Paleta de Cores     | Azul marinho, branco, toques de amarelo | Preto, cinza, marrom |\n| Mobiliário         | Elegante, linhas retas, toque rústico | Linhas retas, simples |\n| Elementos Decorativos | Temática marinha, listras, materiais naturais | Minimalista, pessoal |\n| Atmosfera         | Tranquila, serena, sofisticada | Sofisticada, masculina, dramática |\n| Iluminação        | Natural e suave  | Artificial e direcionada |\n\n**Conclusão:**\n\nA sala náutica é ideal para quem busca um ambiente tranquilo e relaxante com um toque de sofisticação. A sala contemporânea é perfeita para quem deseja um espaço moderno e elegante com um toque masculino. A escolha entre as duas dependerá do seu estilo de vida e da atmosfera que deseja criar em seu espaço."]
  },
])


     

while True:
    imagem1 = input("Digite o caminho da imagem 1: ")
    if imagem1 == "fim":
        break
    imagem2 = input("Digite o caminho da imagem 2: ")
    if imagem2 == "fim":
        break
    prompt = [genai.upload_file(imagem1), genai.upload_file(imagem2), system_instruction]
    response = chat.send_message(prompt)
    print(response.text)
