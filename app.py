import os
from PIL import Image
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

try:
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model_vision = genai.GenerativeModel('gemini-pro-vision')
    model_text = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.stop()

def generate_test_cases(images):
    test_cases = []
    for image in images:
        try:
            image_file = Image.open(image)
            prompt_parts_vision = [
                "Analyze the image and identify interactable elements. List the elements and their types and coordinates.\n\nUser's image:\n\n",
                image_file,
                "\n\nFor each element, write test cases to verify its functionality."
            ]
            response_vision = model_vision.generate_content(prompt_parts_vision)

            prompt_parts_text = [
                "Format the following information as a numbered list of interactable elements with their types, coordinates, and test cases, and each test case should be in another unordered list" + response_vision.text
            ]
            response_text = model_text.generate_content(prompt_parts_text)
            test_cases.append((image_file, response_text.text))
        except Exception as e:
            st.error(f"Error processing image {image.name}: {e}")
    return test_cases

def main():
    st.set_page_config(
        page_title="Mobile App Test Case Generator"
    )
    test_cases = None
    images = None

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
                        test_cases = generate_test_cases(images)
                    st.success("Test cases generated!")
                except Exception as e:
                    st.error(f"Error generating test cases: {e}")
            else:
                st.warning("Please upload some images before generating test cases.")

    st.title("Mobile App Test Case Generator")

    if test_cases:
        for i, (image, test_case) in enumerate(test_cases):
            st.subheader(f"Image {i+1}")
            st.image(image)
            st.write(test_case)

if __name__ == "__main__":
    main()  