#!/usr/bin/python3
from settings import *

# Create Mastodon App
masto = Mastodon(
    access_token = f"{app_name}_cred.secret",
    api_base_url = instance_url
)

last_id = masto.notifications()[0]['id']
# Start infinite loop
while True:
    # Wait sleep_time seconds
    time.sleep(sleep_time)
    # Fetch the notifications
    notifications = masto.notifications(since_id = last_id)
    if not notifications:
      continue
    last_id = notifications[0]['id']
    # Iterate over the notifications

    for notif in notifications:
        # Get the notification type and issuer
        notification_type = notif['type']
        who = notif['account']['display_name']
        # Write message depending on the notificaiton type
        if notification_type == 'mention':
            url = notif['status']['url']
            msg = f"{who} mentioned you :\n{url}"
        if notification_type == 'reblog':
            url = notif['status']['url']
            msg = f"{who} retoot your status :\n{url}"
        if notification_type == 'favourite':
            url = notif['status']['url']
            msg = f"{who} favoured your toot :\n{url}"
        if notification_type == 'follow':
            msg = f"{who} started following you"
        # Push the notification to the gotify server
        r = requests.post(
                f"{gotify_url}/message",
                headers=gotify_header,
                data={
                    'title': "Mastodon",
                    'message': msg,
                    'priority': 10})
