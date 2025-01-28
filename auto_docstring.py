import os
import time
import google.generativeai as genai

# Configure the generative AI API
genai.configure(api_key="your_api_key_here")

model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")

def generate_docstring(code: str) -> str:
    """
    Generates detailed and professional Google-style docstrings for the provided Python code.

    This function leverages a generative AI model to analyze the given Python code and
    generate comprehensive docstrings. It aims to improve existing docstrings or add new ones
    where they are missing, adhering to the Google docstring style.

    Args:
        code: The Python code to process as a string.

    Returns:
        The updated Python code with generated docstrings as a string.
    """
    prompt = (
        "You are an expert Python developer. Add high-quality, detailed, and professional Google-style docstrings to the following Python code. "
        "Ensure that all existing docstrings are edited and improved. If no docstring exists, add one. Do not include `python` in the output. The code:"
        + code
    )

    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            max_output_tokens=10000, temperature=0.7
        ),
    )
    return response.text.strip()

def process_file(file_path: str) -> None:
    """
    Processes a single Python file to generate and overwrite existing docstrings.

    This function reads a Python file, uses `generate_docstring` to update the docstrings,
    and then overwrites the original file with the updated code. Includes a rate-limiting
    mechanism to avoid API throttling.

    Args:
        file_path: The path to the Python file as a string.
    """
    with open(file_path, "r") as file:
        code = file.read()

    # Generate improved docstrings for the code
    updated_code = generate_docstring(code)

    # Save the updated code back to the file
    with open(file_path, "w") as file:
        file.write(updated_code)

    print(f"Processed: {file_path}")

def process_project(directory: str) -> None:
    """
    Processes all Python files in the given directory to generate and overwrite docstrings.

    This function recursively traverses the given directory, identifies all Python files, and
    calls `process_file` to update the docstrings for each one. Errors during file processing
    are caught and reported. Includes a rate-limiting mechanism to avoid API throttling.

    Args:
        directory: The path to the project directory as a string.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    process_file(file_path)
                    time.sleep(1)  # Rate limiting to avoid API throttling
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

def main() -> None:
    """
    Main entry point for the script.

    Prompts the user for a project directory, validates it, and then processes all Python
    files within it using `process_project`. Prints a success message upon completion or
    an error message if the directory is invalid.
    """
    project_directory = input("Enter the path to your Python project: ").strip()
    if os.path.isdir(project_directory):
        process_project(project_directory)
        print("Documentation generation complete!")
    else:
        print("Invalid directory. Please try again.")

if __name__ == "__main__":
    main()
