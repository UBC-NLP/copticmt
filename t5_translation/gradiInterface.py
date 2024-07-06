import os
import logging
import sacrebleu
import pandas as pd
from simpletransformers.t5 import T5Model, T5Args
import gradio as gr

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

model_args = T5Args()
model_args.max_length = 512
model_args.length_penalty = 1
model_args.num_beams = 10
model_args.evaluation_batch_size = 32

model_output_dir = "/local/musaeed/BESTT5TranslationModel"
model = T5Model("t5", model_output_dir, args=model_args, use_cuda=False)

def translate_text(direction, input_text):
    if not input_text.strip():
        return ""  # Return empty string if input_text is empty
    if direction == "English to PCM":
        prefix = "translate en to pcm"
    elif direction == "PCM to English":
        prefix = "translate pcm to en"
    else:
        raise ValueError("Invalid translation direction.")
    preds = model.predict([f"{prefix}: {input_text}"])
    return preds[0]

direction_dropdown = gr.Dropdown(choices=["English to PCM", "PCM to English"], label="Translation Direction:")
input_text = gr.Textbox(lines=2, placeholder="Enter the sentence", label="Enter the Sentence:")

output_text = gr.Textbox(readonly=True)

iface = gr.Interface(
    fn=translate_text,
    inputs=[direction_dropdown, input_text],
    outputs=output_text,
    title="T5 Text Translation",
    live=True,
)

iface.launch(share=True)
