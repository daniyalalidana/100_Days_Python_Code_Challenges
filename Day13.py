import gradio as gr
from langchain_deepseek import ChatDeepSeek
import os
from dotenv import load_dotenv

if load_dotenv():
    print("api called")

llm = ChatDeepSeek(
    model="deepseek-flash",
    api_key= os.getenv("DEEPSEEK_API_KEY"),
    base_url= "https://api.deepseek.com",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

def generare_response(prompt):
    msg = llm.invoke(prompt)
    return msg.content


llm_ui = gr.Interface(
    fn= generare_response,
    inputs= [ gr.Text(label =  "As your query", lines=2, placeholder="ENter your query")],
    title="DeepSeek Flash Model",
    description="This is simple minimum chatbot ask simple question , model is deepseek",
    outputs= gr.Textbox(label= "Output", lines= 3, placeholder="Response from model")
)
# print(generare_response("HI"))
llm_ui.launch(share=True)