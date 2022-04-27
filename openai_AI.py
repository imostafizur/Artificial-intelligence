import os
import openai

print('This an AI configure by Mostafizur Rahman and powered by OpenAI.')
#take input query continuously


Query = input('Ask me a question: ')


openai.api_key = ("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")
response = openai.Completion.create(
  engine="text-davinci-002",
    prompt=Query,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

content = response.choices[0].text
print(content)
Query = content






