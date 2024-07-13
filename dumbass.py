import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
import pickle, os

genai.configure(api_key="AIzaSyDxm__PW_ryvyAM347cmnNwTsr3F_JaJu8")

system_prompt = """
You are python helper bot
You will help the user with ANYTHING python related

You dont fold list or collapse them using list comprehension
You dont use f-strings
You dont use 'with' syntax
"""

his = False
if os.path.isfile("history.pkl"):
    with open("history.pkl", 'rb') as f:
        hx = pickle.load(f)
        his = True

if not his:
    hx = []

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    safety_settings={
        genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT: genai.types.HarmBlockThreshold.BLOCK_NONE,
        genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH: genai.types.HarmBlockThreshold.BLOCK_NONE,
    },
    system_instruction=system_prompt,
)

chat_session = model.start_chat(history=hx)

console = Console()

while True:
    try:
        user_input = console.input("[bold italic cyan]You:[/] ")
        response = chat_session.send_message(user_input)
        console.print(Markdown(response.text))
    except KeyboardInterrupt:
        break

with open("history.pkl", "wb") as f:
    pickle.dump(chat_session.history, f)
