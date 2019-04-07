# chatbot
chatbot backend


## slack bot creation
### reference articles
- https://pattern-match.com/blog/2018/10/30/serverless-slackbot-using-aws-chalice/
- https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e

### steps
1. create an app in your workspace on slack
2. get OAuth Tokens and Bot Access Token for the app
3. create a lambda function and api gateway with serverless framework. get api endpoint url for next step
4. create a bot user
5. subscribe 'event subscriptions' for the bot app. this is where bot get the chat message input.
use the aws api gateway endpoint url as request url. slack requires url verification, so include the codes
to handle the first challenge message to verify the request url.
6. customize your bot with a cool avatar and start play
