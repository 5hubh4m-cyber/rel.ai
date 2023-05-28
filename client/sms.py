from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Twillio Documentation: [Twillio Python](https://www.twilio.com/docs/libraries/python)

# send_otp_message


def send_otp_mobile(contact_number, sms_content):
    # logger.info(f"send_otp_mobile: {contact_number}")
    response = {"message": "SMS sent successfully",
                "status_code": 200}
    try:
        # Find your Account SID and Auth Token at twilio.com/console
        # Your Account SID from twilio.com/console
        account_sid = "ACbae95b1c54598d164d57372fd8c901dd"
        # Your Auth Token from twilio.com/console
        auth_token = "cb2820d5346912d24b185ddb7f9bd145"
        client = Client(account_sid, auth_token)
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


sms_content = """Hello Alex Fandu"""
response = send_otp_mobile("+919955262206", sms_content=sms_content)
print(response)
