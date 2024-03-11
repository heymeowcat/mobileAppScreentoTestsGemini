import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

try:
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model_vision = genai.GenerativeModel('gemini-pro-vision')
    model_text = genai.GenerativeModel('gemini-pro')
    model_qa = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"Error configuring Gemini API: {e}")
    st.stop()

def generate_test_cases(image: Image.Image) -> str:
    """
    Generate test cases for the given image.

    Args:
        image (Image.Image): Input image.

    Returns:
        str: Test cases for the image.
    """
    try:
        prompt_parts_vision = [
            "Analyze the image and identify interactable elements. List the elements and their types.\n\nUser's image:\n\n",
            image,
            "\n\nFor each element, write test cases to verify its functionality."
        ]

        response_vision = model_vision.generate_content(prompt_parts_vision)
        response_vision_text = response_vision.candidates[0].content.parts[0].text

        prompt_parts_text = [
            "From the perspective of a QA engineer, format the following information as a numbered list of interactable elements with their types and test cases. Each test case should be in another unordered list:\n\n" + response_vision_text
        ]

        response_text = model_text.generate_content(prompt_parts_text)

        prompt_parts_qa = [
            "You are a highly experienced QA engineer. Review and refine the following test case list to ensure it is well-structured, consistent, and follows best practices for writing test cases. Provide any necessary improvements or corrections:\n\n" + response_text.text
        ]

        response_qa = model_qa.generate_content(prompt_parts_qa)

        return response_qa.text
    except Exception as e:
        st.error(f"Error processing the image: {e}")
        return ""

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
                test_cases = []
                for image in images:
                    with st.spinner(f"Generating test cases for {image.name}..."):
                        test_case = generate_test_cases(Image.open(image))
                        test_cases.append(test_case)
                st.success("Test cases generated!")
            else:
                st.warning("Please upload some images before generating test cases.")

    st.title("Mobile App Test Case Generator")
    if test_cases:
        for i, test_case in enumerate(test_cases):
            st.subheader(f"Image {i+1}")
            st.image(images[i])
            st.write(test_case)

if __name__ == "__main__":
    main()