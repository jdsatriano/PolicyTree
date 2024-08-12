# Medical Policy Decision Tree Generator

This project processes medical policy PDFs to generate machine-parseable decision trees, evaluates the quality of these trees, and serves the information through a REST API. The decision trees help in determining the medical necessity of specific procedures.

## Features
- Extracts and processes medical policies from PDFs.
- Generates JSON decision trees for each policy.
- Ranks the quality of the generated decision trees.
- Caches results for efficient subsequent requests.
- Serves the data through a FastAPI REST API.

## Prerequisites
- Python 3.x
- pip3

## Installation

1. **Clone the repository:**
    ```
    git clone https://github.com/jdsatriano/PolicyTree.git
    cd PolicyTree
    ```
2. **Install Dependencies:**
    ```
    pip3 install -r requirements.txt
    ```
3. **Set up environment variables:**
    Create a .env file in the root directory with the following content:
    ```
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_ORG_ID=your_openai_org_id
    OPENAI_PROJECT_ID=your_project_id
    ```

## Running the Project

1. **Start the server:**
    ```
    python3 -m uvicorn main:app --reload
    ```
2. **Access the API:**
    Once the server is running, you can access the API endpoint at:
    ```
    http://127.0.0.1:8000/generate-decision-trees/
    ```

## Project Structure

- **main.py:** The entry point of the application. Configures the FastAPI app and routes.
- **api/generate_tree.py:** Contains the endpoint for generating decision trees and caching results.
- **services/decision_tree.py:** Handles the logic for processing PDFs and generating decision trees.
- **services/openai_client.py:** Manages communication with the OpenAI API.
- **services/text_extraction.py:** Extracts text from PDF files.
- **prompts/decision_tree_prompt.txt:** The configurable prompt template used to generate decision trees.