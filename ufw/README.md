## Allow traffic to pass through to the next gateway
See [here](https://manpages.ubuntu.com/manpages/trusty/man8/ufw.8.html) for more details.

```
ufw route allow from src.ip.ad.dr to any port 443 proto tcp
ufw route allow from src.ip.ad.dr to any port 80 proto tcp
```

Ensure these lines are uncommented in `/etc/ufw/sysctl.conf`

```
net/ipv4/ip_forward=1
net/ipv6/conf/default/forwarding=1
net/ipv6/conf/all/forwarding=1
```

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

Note that you MUST allow incoming traffic on the ports you are `REDIRECT`ing to.
For me, it's port `8080`

```
pi@raspberrypi:~ $ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22                         ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
53/tcp                     ALLOW IN    Anywhere
53/udp                     ALLOW IN    Anywhere
8080/tcp                   ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
22 (v6)                    ALLOW IN    Anywhere (v6)
80/tcp (v6)                ALLOW IN    Anywhere (v6)
53/tcp (v6)                ALLOW IN    Anywhere (v6)
53/udp (v6)                ALLOW IN    Anywhere (v6)
8080/tcp (v6)              ALLOW IN    Anywhere (v6)
443/tcp (v6)               ALLOW IN    Anywhere (v6)

443/tcp                    ALLOW FWD   src.ip.ad.dr
80/tcp                     ALLOW FWD   src.ip.ad.dr
```
