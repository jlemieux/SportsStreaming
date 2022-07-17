## Reverse Proxy

See `external.conf`.

## Serving static files

Web root is set to `/var/www/html`. The stock 'pi-hole' lighttpd conf has
`/admin` for the web interface. SportsStreaming, for example, has `/sports`.
Use this folder as static resources for whatever site you want to make.

```
pi@raspberrypi:~/SportsStreaming $ ls -l /var/www/html/sports/
total 660
-rw-r--r-- 1 root root   2248 Jul 16 23:56 3rdpartylicenses.txt
-rw-r--r-- 1 root root   5430 Jul 16 23:56 favicon.ico
-rw-r--r-- 1 root root    680 Jul 16 23:58 index.html
-rw-r--r-- 1 root root 306570 Jul 16 23:56 main.9912384afd880b59138c.js
-rw-r--r-- 1 root root  42016 Jul 16 23:56 polyfills.b48c5d62f496af968247.js
-rw-r--r-- 1 root root   1053 Jul 16 23:56 runtime.a66f828dca56eeb90e02.js
-rw-r--r-- 1 root root 150643 Jul 16 23:56 scripts.618f6a850951c6fe70f6.js
-rw-r--r-- 1 root root 147814 Jul 16 23:56 styles.7a7dba6abc86fc2733ac.css
```
