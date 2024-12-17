
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Content generation function using ChatCompletion
def generate_content(prompt: str):
       try:
        print("Generating content... This may take a moment.")
        response = client.chat.completions.create(
            model="gpt-4o",  # Use GPT-4o or GPT-3.5-turbo as needed
               messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
               ],
            response_format={"type": "text"},
            max_tokens=500,
               temperature=0.7
        )
        content = response.choices[0].message.content.strip()
        print("Content generated successfully!")
        return content
       except Exception as e:
            print(f"Error generating content: {e}")
            return None

# Save generated content to an HTML file
def save_content_to_file(content: str):
    filename = f"generated_content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(filename, "w") as file:
        file.write("<!DOCTYPE html>\n<html>\n<head>\n<title>AI Generated Content</title>\n</head>\n<body>\n")
        file.write(f"<h1>AI Generated Content</h1>\n<p>{content}</p>\n")
        file.write("</body>\n</html>")
    print(f"Content saved to {filename}")
    return filename

# Main execution workflow
def main():
    prompt = "Write a blog post about the benefits of autonomous AI publishing systems."
    content = generate_content(prompt)
    if content:
        save_content_to_file(content)
    else:
        print("No content generated. Please check the API configuration.")

if __name__ == "__main__":
    main()