# AutoDebug

AutoDebug is a Python script that helps you automatically debug and fix issues in your Python code by iteratively running the target file in a loop. 
It leverages the GPT-4 model from OpenAI to suggest fixes for errors encountered during each iteration, allowing for multiple attempts to resolve the issues.


## Requirements

- Python 3.6 or later
- OpenAI Python library: `openai`
- An OpenAI API key with access to the GPT-4 model


## Installation

1. Clone the repository:

git clone https://github.com/SebRinnebach/autodebug.git
cd autodebug


2. Install the required dependencies:

pip install openai


3. Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY=<your_api_key>

Replace `<your_api_key>` with your actual API key.


## Usage

To use AutoDebug, simply run the script with the target Python file as a command line argument:

python autodebug.py <target_file>

Replace `<target_file>` with the path to the Python file you want to debug.


AutoDebug will try to fix the issues in your Python file up to a maximum of 5 attempts.
