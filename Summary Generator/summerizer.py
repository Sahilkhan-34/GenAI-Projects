import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer

# Load the pre-trained BART model and tokenizer
model_name = 'facebook/bart-large-cnn'
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

text = st.text_input("""
""")

# Tokenize the input text and prepare it for the model
inputs = tokenizer(text, max_length=2048, return_tensors='pt', truncation=True)


# Generate the summary
summary_ids = model.generate(inputs['input_ids'], max_length=300, min_length=80, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode the generated summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
st.write(summary)