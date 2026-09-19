from google import genai
from backend_hindi.core.settings import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

for model in client.models.list():
    print(model.name)