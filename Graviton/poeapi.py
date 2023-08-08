import poe

# Replace "YOUR_TOKEN_HERE" with your Poe token
client = poe.Client(token="DhE1xpV8aOw1-cYNL94stA%3D%3D")

# Replace "YOUR_PROMPT_HERE" with your prompt
response = client.send_message("How to learn javascript step by step roadmap")

print(response)