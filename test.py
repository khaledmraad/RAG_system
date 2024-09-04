import openai

# Azure OpenAI API configuration
endpoint = "https://othai.openai.azure.com/"
deployment = "text-embedding-ada-002"

openai.api_type = "azure"
openai.api_base = endpoint
openai.api_version = "2024-05-01-preview"
openai.api_key = "0dc97b63aaaa46ad855acbc6c0d7660c"

def ask_gpt(prompt, max_tokens=50):
    try:
        response = openai.Completion.create(
            engine=deployment,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage
prompt = "Translate the following English sentence into French: 'Hello, how are you?'"
response = ask_gpt(prompt)
print("Response:", response)