import base64
import os
import cohere
import dotenv

dotenv.load_dotenv()

import twilio_add_user 

# Example string from the Twilio POST
message_body = str(base64.b64decode("VG9Db3VudHJ5PUNBJlRvU3RhdGU9UVEmU21zTWVzc2FnZVNpZD1TTU05YjVkOTA5OGUwZDg4NDZlN2EyMzllNGExY2Q4Zjc4NSZOdW1NZWRpYT0wJlRvQ2l0eT1USEVUVE9ERStNSU5FUyZGcm9tQ2l0eT1DQSZUb1ppcD0mTnVtU2VnbWVudHM9MSZNZXNzYWdlU2lkPVMNTTliNWQ5MDk4ZTBkODg0NmU3YTIzOWU0YTFjZDhmNzg1JkFjY291bnRTaWQ9QUNiYWU5NWIxYzU0NTk4ZDE2NGQ1NzM3MmZkOGM5MDFkZCZGcm9tPSMxMzE0OTQ3NDAxOCZBcGlWZXJzaW9uPTEwMTAtMDQtMDE="),'utf-8')
print(f"message_body: {message_body}")
key_value_pairs = message_body.split("&")
for pair in key_value_pairs:
    if "Body" in pair:
        print("pair: ",pair)
        body = pair.split("=")[1]
        print("hi\n")
        print(body.replace('+',' '))

# Call Cohere

# print(f"cohere api key: {os.getenv('COHERE_API_KEY')}")
co = cohere.Client(os.getenv('COHERE_API_KEY'))
response = co.generate(
  model='command-medium-nightly',
  prompt='how are you? explain quantum computing as if i\'m 5 years old. in 100 words',
  max_tokens=300,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='NONE')

prediction_text = response.generations[0].text
print('Prediction: {}'.format(response.generations[0].text))

contact_number = '+919955262206'
twilio_add_user.send_message_to_mobile(contact_number, prediction_text)
