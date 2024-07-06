import streamlit as st
from PIL import Image

# Streamlit interface
st.title("Sentiment Analysis of Instagram Comments")
st.write("Benchmarking two models for training- DistilBERT, and DistilRoBERTa for the classification task of determining whether an instagram comment is positive or negative.")

# Load images
image1 = Image.open('accuracy_graph.png')
image2 = Image.open('f1_graph.png')
image3 = Image.open('loss_graph.png')

# Display images
st.image(image1, caption='Accuracy', use_column_width=True)
st.image(image2, caption='F1 score', use_column_width=True)
st.image(image3, caption='Loss', use_column_width=True)
