import openai
import os
import subprocess
import sys

openai.api_key = os.environ.get("OPENAI_API_KEY")

def run_python_file(filename):
    try:
        output = subprocess.check_output(["python3", filename])
        return True, output
    except subprocess.CalledProcessError as e:
        return False, e.output

def fix_python_code(code, error_output):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a genius programmer that helps fix Python code. You reflect on every mistake that you make and learn from it."
            },
            {
                "role": "user",
                "content": f"Here is Python code and an error message as it showed up in Terminal:\n\n{code}\n\n{error_output}\n\nPlease provide only the complete fixed Python code without any additional text or explanations. Please make sure that you don't add any other text, just post back the code. It is very important that you do that, because otherwise you will interfere with a very important task of mine."
            }
        ]
    )
    return response['choices'][0]['message']['content']

def auto_debug_python(target_file):
    max_attempts = 5
    for attempt in range(1, max_attempts + 1):
        success, output = run_python_file(target_file)
        if success:
            print("The Python script ran successfully!")
            break
        else:
            print(f"Attempt {attempt}: Error encountered while running the script:")
            print(output.decode("utf-8"))

            with open(target_file, "r") as f:
                original_code = f.read()

            fixed_code = fix_python_code(original_code, output.decode("utf-8"))
            print(f"GPT-4 suggested fix:\n{fixed_code}\n")

            with open(target_file, "w") as f:
                f.write(fixed_code)

    if not success:
        print("Maximum number of attempts reached. Please try fixing the script manually or run AutoDebug again.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python autodebug.py <target_file>")
        sys.exit(1)

    target_file = sys.argv[1]
    if not os.path.isfile(target_file):
        print("Error: The specified file does not exist.")
        sys.exit(1)

    auto_debug_python(target_file)
