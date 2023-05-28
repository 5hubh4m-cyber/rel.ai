import os
from twilio.rest import Client
import dotenv
dotenv.load_dotenv()


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

validation_request = client.validation_requests \
                           .create(
                                friendly_name='My Home Phone Number',
                                phone_number='+xxxxxxx',
                            )

print(validation_request.validation_code)


