import streamlit as st
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def predict_caption(image: Image.Image):
    if image.mode != "RGB":
        image = image.convert(mode="RGB")
    
    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    
    gen_kwargs = {"max_length": 16, "num_beams": 4}
    output_ids = model.generate(pixel_values, **gen_kwargs)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()
    return caption

st.title("Image Captioning with VisionEncoderDecoderModel")
st.write("Upload one or more images, and the model will generate captions for all of them.")

uploaded_files = st.file_uploader("Choose one or more images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.write("### Uploaded Images and Captions:")
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Generating caption..."):
            caption = predict_caption(image)
        st.success("Caption generated!")
        st.write(f"**Caption for {uploaded_file.name}:** {caption}")
