import datetime
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
print(os.getenv("SLACK_BOT_TOKEN"))
print(client)
logger = logging.getLogger(__name__)
# ID of the channel you want to send the message to
channel_id = "C04JHCMFP5X"

# tomorrow = datetime.date.today() + datetime.timedelta(days=1)
# scheduled_time = datetime.time(hour=9, minute=30)
# schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')
# print(tomorrow, scheduled_time)

try:
        # Call the chat.postMessage method using the WebClient
            result = client.chat_postMessage(
                            channel=channel_id, 
                                    text="Hello world",
                                            # post_at=schedule_timestamp
                                                )
                logger.info(result)

except SlackApiError as e:
        logger.error(f"Error posting message: {e}")
