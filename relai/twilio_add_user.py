from twilio.base.exceptions import TwilioRestException
import os
from twilio.rest import Client
# import dotenv
# dotenv.load_dotenv()
# from dotenv import dotenv_values

 # Your Account SID from twilio.com/console
account_sid = "ACbae95b1c54598d164d57372fd8c901dd"
# Your Auth Token from twilio.com/console
auth_token = "cb2820d5346912d24b185ddb7f9bd145"
client = Client(account_sid, auth_token)
# secrets = dotenv_values('.env')
# account_sid = secrets['TWILIO_ACCOUNT_SID']
# auth_token = secrets['TWILIO_AUTH_TOKEN']

# account_sid = 'ACbae95b1c54598d164d57372fd8c901dd'
# auth_token = 'cb2820d5346912d24b185ddb7f9bd145'
# account_sid = os.environ['ACbae95b1c54598d164d57372fd8c901dd']
# auth_token = os.environ['cb2820d5346912d24b185ddb7f9bd145']
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

# client = Client(account_sid, auth_token)

# validation_request = client.validation_requests \
#                            .create(
#                                friendly_name='My Home Phone Number',
#                                phone_number='+13149474018',
#                            )

# print(validation_request.validation_code)



# Twillio Documentation: [Twillio Python](https://www.twilio.com/docs/libraries/python)

# send_message_to_mobile
def send_message_to_mobile(contact_number, sms_content):
    # logger.info(f"send_message_to_mobile: {contact_number}")
    response = {"message": "SMS sent successfully",
                "status_code": 200}
    try:
        # Find your Account SID and Auth Token at twilio.com/console
       
        message = client.messages.create(
            to=contact_number,  # "+919955262206"
            from_="+13149474018",  # this is given by Twillio
            body=f"\nGreetings, Please find your SMS: \n{sms_content}"
        )

    except TwilioRestException as e:
        response["message"] = {"message": f"Something went wrong",
                               "error": str(e)}
        response["status_code"] = 500

    return response


# sms_content = """Hello Alex"""
# response = send_message_to_mobile("+919955262206", sms_content=sms_content)
# print(response)


