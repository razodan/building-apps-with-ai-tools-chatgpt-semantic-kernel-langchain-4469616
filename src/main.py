import os
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AzureOpenAI(api_key=os.getenv('AZURE_OPENAI_API_KEY'),
                     azure_deployment=os.getenv('AZURE_OPENAI_MODEL_DEPLOYMENT'),
                     azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
                     api_version=os.getenv('AZURE_OPENAI_VERSION'))
while True:
  user_input = input('Enter a phrase to determine whether it is happy or sad.\n')
  if user_input == 'exit' or user_input == 'quit':
    break
  response = client.chat.completions.create(
    model='gpt-4',
    messages=[
      {'role':'system','content':'You are a sentiment classification bot. Print out whether the message is happy or sad.'},
      {'role':'user','content':user_input}
    ],
    temperature=0.7,
    max_tokens=150,
  )

  response_message = response.choices[0].message
  print(f'\trole: {response_message.role}\n\tcontent: {response_message.content}\n')