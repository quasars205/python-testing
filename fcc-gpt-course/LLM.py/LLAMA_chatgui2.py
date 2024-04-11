import os
import gradio as gr
from text_generation import Client

LLAMA_70B = os.environ.get("LLAMA_70B","http;//localhost:3000"),
CLIENT = Client(base_url = LLAMA_70B)

PARAMETERS ={
    "temperature" : 0.1,
    "top_p" : 0.95,
    "repetition_penalty": 1.2,
    "top_k" : 50,
    "max_new_tokens": 1024,
    "truncate" : 1000,
    "seed": 42,
    "stop_sequence":["</s>"],
}

PROMPT ="""<s>[INST]<<SYS>>
you are a helpful bot, answer user questions. respect the users
dont provide incorrect and bad answers. if you dont know just say that you dont know
<</SYS>>
"""

def format_message(message, history):
    if len(history) > 5:
        history = history[-5:]

    if len(history) == 0:
        query = PROMPT + f"{message} [/INST]"
    elif history == 1:
        query = PROMPT + f"{history[0][0]}</INST> {history[0][1]}<s>"
    for user_msg, model_answer in history[1:]:
        query += f"<s>[INST] {user_msg} [/INST] {model_answer}</s>"

    query += f"<s>[INST] {message}[/INST]"

    return query

def predict(message, history):
    query = format_message (message, history)
    test=""
    for response in CLIENT.genrate_stream(query,**PARAMETERS):
        if not response.token.special:
            text += response.token.text
            yield text

gr.ChatInterface(predict).queue().launch(share=True)
