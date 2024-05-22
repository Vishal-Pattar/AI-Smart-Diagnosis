import streamlit as st
from PIL import Image
from prediction import DiseaseModelFactory
from suggestions import SuggestionFactory

# Initialize and cache model factory
@st.cache_resource
def load_models():
    return DiseaseModelFactory()

# Main Streamlit app
def main():
    st.title("AI Smart Diagnosis - A Smart Step in Self Diagnosis")
    
    st.subheader("Select the Disease you want to diagnose")
    disease = st.selectbox("Select", ["Kidney Disease", "Brain Tumor", "Lungs Disease", "Tuberculosis"])

    st.subheader("Upload your data")
    uploaded_file = st.file_uploader("Choose file", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        if st.button('Start checkup'):
            process_report(disease, uploaded_file)

def process_report(disease, uploaded_file):
    st.subheader("Report")
    
    image = Image.open(uploaded_file)
    st.subheader("Uploaded Image")
    st.image(image, caption='Uploaded Image', width=400)
    
    img_path = "temp_image.png"
    image.save(img_path)

    # Use the cached model factory
    model_factory = load_models()
    disease_model = model_factory.get_model(disease)
    result, dis_name = disease_model.predict(img_path)

    suggestion_factory = SuggestionFactory()
    suggestion = suggestion_factory.get_suggestion(disease, dis_name)
    
    st.write(f"Disease Name: {dis_name}")
    st.write(suggestion)
    st.warning("Caution: This is a computer-generated report, please don’t rely on it completely for any medications.")

if __name__ == "__main__":
    main()