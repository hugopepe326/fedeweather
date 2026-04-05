from openai import OpenAI

# Configuración para conectar con el servidor local de LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="local-model", # LM Studio ignorará este nombre y usará el cargado
  messages=[
    {"role": "system", "content": "Eres un asistente experto corriendo en un Mac M4."},
    {"role": "user", "content": "Explícame qué ventajas tiene el chip M4 para IA."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)
