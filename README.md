# Mastodon to Gotify
This Programm fetches notifications from Mastodon and pushes them to a Gotify server.

## Dependencies
[Mastodon.py](https://github.com/halcy/Mastodon.py)
```pip install Mastodon.py```

## Usage
First, rename the file settings.py.sample to settings.py and set all the configurations inside it.
Second, create an app on your instance (read notification is enough) and store the access token in ```{app_name}_cred.secret```.
Thirdly, run main.py

It is advised to have it running as a service :
```
sudo cp mastogotify.service /etc/systemd/system/
sudo systemctl start mastogotify
sudo systemctl enable mastogotify
```
