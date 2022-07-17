## Configuration for mitmdump/mitmproxy

Put `config.yml` within `~/.mitmproxy`

```
pi@raspberrypi:~/SportsStreaming $ ls /home/pi/.mitmproxy/config.yml
/home/pi/.mitmproxy/config.yml
```

## Custom addons/hooks

Put addons within any folder, but specify their location within `config.yml`.
For example, I have them in `/home/pi/.mitmproxy/custom-addons/*`.

```
pi@raspberrypi:~/SportsStreaming $ ls /home/pi/.mitmproxy/custom-addons/
__pycache__  remove_comma.py
```
