const accountSid = 'ACbae95b1c54598d164d57372fd8c901dd'; // Your Account SID from twilio.com/console
const authToken = 'cb2820d5346912d24b185ddb7f9bd145'; // Your Auth Token from twilio.com/console
const client = require('twilio')(accountSid, authToken);

function sendOTPMobile(contactNumber, smsContent) {
  return new Promise((resolve, reject) => {
    client.messages
      .create({
        body: `Greetings, Please find your SMS:\n${smsContent}`,
        from: '+13149474018', // this is given by Twilio
        to: contactNumber,
      })
      .then((message) => {
        resolve({
          message: 'SMS sent successfully',
          statusCode: 200,
        });
      })
      .catch((error) => {
        reject({
          message: 'Something went wrong',
          error: error.message,
          statusCode: 500,
        });
      });
  });
}

const smsContent = 'Hello Alex Fandu';
sendOTPMobile('+919955262206', smsContent)
  .then((response) => console.log(response))
  .catch((error) => console.error(error));
