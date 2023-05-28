# RelAI
Be able to access an AI no matter if you have internet or not!

## Abstract
Creating RelAI that works offline is a noble and inspiring goal, especially for those in third-world countries who may not have access to reliable internet. In many parts of the world, access to the internet is limited or non-existent, making it difficult for people to communicate and access information. However, even in these areas, people often have access to mobile phones, making SMS a crucial means of communication.

With RelAI you have the potential to bridge the digital divide and bring the benefits of AI technology to people who may not have had access to it otherwise. With this app, people in third-world countries could communicate with friends and family, access information, and even receive personalized recommendations, all without the need for a stable internet connection.

## Working

By sending a message to the number, you are able to have an AI generate a response back purely through SMS and not through the internet at all. 

You are able to send images, and text, and even ask as many questions as you want and it would text you back with the AI-generated response with no wifi. 

## Implementation

When a user sends a text message to the app's phone number, Twilio routes the message to an AWS Lambda function. This function acts as a gateway, directing the message to the appropriate API or service based on the prompt contained in the message. For example, if the user sends a message asking for an image, it will route the prompt to openAi

Once the message has been directed to the appropriate API or service, the body of the message is passed to Co:here, an advanced natural language processing platform. Using machine learning algorithms, Co:here processes the message and generates a response, which is then sent back to the user via Twilio.

This innovative approach to SMS messaging leverages the latest in AI technology to provide users with fast, accurate, and personalized responses, all without the need for a stable internet connection. Whether a user is in a remote rural area or in a city with limited access to the internet, your app provides a valuable and convenient means of communication and information access.



ToCountry=CA&ToState=QQ&SmsMessageSid=SMM9b5d9098e0d8846e7a239e4a1cd8f785&NumMedia=0&ToCity=THEFTORD&MessageStatus=ON&FromCity=CA&ToZip=&FromState=ON&From=+13149474018&ToZip=&NumSegments=1&MessageSid=SMM9b5d9098e0d8846e7a239e4a1cd8f785&AccountSid=ACbae95b1c54598d164d57372fd8c901dd&From=+13149474018&ApiVersion=2010-04-01
1
