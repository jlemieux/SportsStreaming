## Redirecting traffic to a different port
At the top of `/etc/ufw/before.rules`

```
*nat
:PREROUTING ACCEPT [0:0]

# multiport example
-A PREROUTING -p tcp --match multiport --dports 80,443 -j REDIRECT --to-port 8080

# based on destination ip example
-A PREROUTING -p tcp -d dest.ip.goes.here --dport 80 -j REDIRECT --to-port 8080

COMMIT
```

## Allow traffic to pass through to the next gateway
See [here](https://manpages.ubuntu.com/manpages/trusty/man8/ufw.8.html) for more details.

```
ufw route allow from src.ip.ad.dr to any port 443 proto tcp
ufw route allow from src.ip.ad.dr to any port 80 proto tcp
```
