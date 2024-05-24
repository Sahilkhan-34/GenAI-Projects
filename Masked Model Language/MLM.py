import streamlit as st
from transformers import BertTokenizer, BertForMaskedLM
from transformers import AlbertTokenizer, AlbertForMaskedLM
import torch


# Define a function to predict masked words
def predict_masked_words(sentence):
    # Tokenize the input sentence
    tokenized_input = tokenizer.encode_plus(sentence, return_tensors="pt", add_special_tokens=True)

    # Get the position of the masked token
    masked_index = torch.where(tokenized_input["input_ids"] == tokenizer.mask_token_id)[1]

    # Predict the masked token
    with torch.no_grad():
        outputs = model(**tokenized_input)

    # Get the logits for the masked token
    predictions = outputs.logits[0, masked_index, :]

    # Get the top predictions
    top_indices = torch.topk(predictions, 5, dim=1).indices[0].tolist()

    # Convert token IDs to actual words
    predicted_tokens = [tokenizer.decode([index]).strip() for index in top_indices]

    return predicted_tokens

# Load pre-trained BERT model and tokenizer

bert_base_uncased = "bert-base-uncased"
bert_large_uncased = "bert-large-uncased"
bert_base_multilingual_uncased = "bert-base-multilingual-uncased"
albert_large = "albert-large-v2"


model_name = st.sidebar.radio(
            "Select the Model 👉",
            key="visibility",
            options=[bert_base_uncased, bert_large_uncased, bert_base_multilingual_uncased, albert_large],)

if model_name == albert_large:
  tokenizer = AlbertTokenizer.from_pretrained(model_name)
  model = AlbertForMaskedLM.from_pretrained(model_name)
else:
  tokenizer = BertTokenizer.from_pretrained(model_name)
  model = BertForMaskedLM.from_pretrained(model_name)

# Streamlit app
st.title("BERT Masked Word Predictor")

st.write("Enter a sentence with a masked word, denoted by [MASK], and See BERT's top 5 words predictions.")

# Text input for the sentence
input_sentence = st.text_input("Input Sentence", "I want to go [MASK].")

if st.button("Predict"):
    if "[MASK]" not in input_sentence:
        st.error("The input sentence must contain the [MASK] token.")
    else:
        # Predict masked words
        predicted_words = predict_masked_words(input_sentence)
        st.write("Predicted words:")
        for i, word in enumerate(predicted_words):
            st.write(f"{i+1}. {word}")
