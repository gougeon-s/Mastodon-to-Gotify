#!/usr/bin/python3
from settings import *

# Create Mastodon App
masto = Mastodon(
    access_token = app_name + "_cred.secret",
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
        url = ''
        # Get the notification type and issuer
        notification_type = notif['type']
        who = notif['account']['display_name']
        # Write message depending on the notificaiton type
        if notification_type == 'mention':
            url = notif['status']['url']
            msg = who +" mentioned you"
        if notification_type == 'reblog':
            url = notif['status']['url']
            msg = who + " retoot your status"
        if notification_type == 'favourite':
            url = notif['status']['url']
            msg = who + " favoured your toot"
        if notification_type == 'follow':
            msg = who + " started following you"
        if notification_type == 'poll':
            msg = "Poll is finished"
        # Push the notification to the gotify server
        if (url != ''):
            data={
                'title': "Mastodon",
                'message': msg,
                'priority': 10,
                'extras': {
                     'client::notification': {
                          'click': {'url': url}
                      }
                 }
            }
        else:
            data={
                'title': "Mastodon no extra",
                'message': msg,
                'priority': 10}
        r = requests.post(
                gotify_url + "/message",
                headers=gotify_header,
                json=data)
