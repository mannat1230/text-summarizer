from transformers import pipeline
import gradio as gr

# Define the model
model = pipeline("summarization")

# Define the predict function
def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Using gr.Blocks() to create the interface
with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    output = gr.Textbox()
    submit_btn = gr.Button("Summarize")
    submit_btn.click(fn=predict, inputs=textbox, outputs=output)

demo.launch()
