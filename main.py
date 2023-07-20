#https://beta.openai.com/examples
# You will need to register with OPENAI to get an API key you can use

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load your API key from an environment variable or secret management service

yourprompt = input("What would you like this AI to complete?")

response = openai.Completion.create(engine="text-davinci-003",
                                    prompt=yourprompt,
                                    temperature=0.1,
                                    max_tokens=100,
                                    top_p=1,
                                    frequency_penalty=9,
                                    presence_penalty=0)

print(response["choices"][0]["text"])

print("-" * 20)

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=
  "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ:How many litres are in a gallon?\nA: There are 3.785 liters in a gallon.\n\nQ: What is the meaning of life?\nA: The meaning of life is to live.\n\nQ: When will the world end?\nA: The world will end in the year 5,717,928.\n\n\nQ:What is a heuristic? \nA: A heuristic is a method of problem solving that is not guaranteed to produce a correct solution, but is a useful starting point.\n\nQ: "
  + yourprompt + "\n",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"])

#print(response)
print(response["choices"][0]["text"])
