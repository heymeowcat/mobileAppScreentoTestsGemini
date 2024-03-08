import os
from PIL import Image
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

try:
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-pro-vision')
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.stop() 

def generate_test_cases(images):
    test_cases = []
    for image in images:
        try:
            image_file = Image.open(image)
            prompt_parts = [
                "Analyze the image and identify interactable elements. List the elements and their types and coordinates.\n\nUser's image:\n\n",
                image_file,
                "\n\nInteractable elements:\n",
            ]
            response = model.generate_content(prompt_parts)
            test_cases.append(response.candidates)
        except Exception as e:
            st.error(f"Error processing image {image.name}: {e}")
    return test_cases

def main():
    st.set_page_config(
        page_title="Mobile App Test Case Generator"
    )

    test_cases = None 
    
    with st.sidebar:
        st.title("Menu")
        images = st.file_uploader(
            "Upload your mobile app screenshots",
            accept_multiple_files=True,
            type=["png", "jpg", "jpeg"]
        )

    
        if st.button("Generate Test Cases"):
            if images:
                    try:
                        with st.spinner("Generating test cases..."):
                            test_cases = generate_test_cases(images)  # Call the function to assign a value
                            st.success("Test cases generated!")
                    except Exception as e:
                        st.error(f"Error generating test cases: {e}")
            else:
                st.warning("Please upload some images before generating test cases.")

    st.title("Mobile App Test Case Generator")

    if test_cases: 
        for i, test_case in enumerate(test_cases):
            st.subheader(f"Image {i+1} Test Cases")
            st.write(test_case)

if __name__ == "__main__":
    main()