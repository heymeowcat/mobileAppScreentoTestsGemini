
## MobileAppScreentoTestsGemini: Generate Test Cases from Mobile App Screenshots

This Streamlit application leverages Gemini, a large language model from Google AI, to automatically generate test cases for your mobile app based on screenshots.

### How it Works

1.  Upload one or more mobile app screenshots (PNG, JPG, JPEG formats).
2.  Click the "Generate Test Cases" button.
3.  The app analyzes each image using a vision model to identify interactive elements.
4.  It then uses a text model to format the elements and generate initial test cases.
5.  Finally, a QA-focused model refines the test cases for better structure and clarity.
6.  The generated test cases are displayed for each uploaded image.

### Running the App

**Prerequisites:**

-   Python 3.7 or later

**Installation:**

1.  **Clone the Repository:**
    
    
    
    ```
    git clone https://github.com/heymeowcat/mobileAppScreentoTestsGemini.git
    cd mobileAppScreentoTestsGemini
    ```
    
    
2.  **Install Dependencies:**
    
    
    
    ```
    pip install -r requirements.txt 
    ```
    
    
3.  **Set Up Gemini API Key:**
    
    -   Create a project and obtain an API key from Google AI Platform: 
        
    -   Create a `.env` file in the project root directory and add the following line, replacing `YOUR_GEMINI_API_KEY` with your actual key:
        
        ```
        GEMINI_API_KEY=YOUR_GEMINI_API_KEY  
        ```
        
4.  **Run the App:**
  
    
    ```
    streamlit run main.py   
    ```
    
    
    This will launch the app in your web browser, usually at `http://localhost:8501`.
    

### Usage

1.  Upload your mobile app screenshots in the sidebar menu.
2.  Click the "Generate Test Cases" button.
3.  The generated test cases will be displayed beneath each corresponding image.

**Note:** Processing multiple images might take some time depending on the image size and complexity.

### Contributing

We welcome contributions to this project! Feel free to fork the repository and submit pull requests with improvements or bug fixes.
