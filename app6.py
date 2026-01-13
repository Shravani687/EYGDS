import google.generativeai as genai

genai.configure(api_key="AIzaSyD6X-VRnmJdHsY0sTzamlZu3yoWi1Kd80U")

for m in genai.list_models():
    print(m.name)
