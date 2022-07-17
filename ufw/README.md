*nat
:PREROUTING ACCEPT [0:0]
#-A PREROUTING -p tcp --match multiport --dports 80,443 -j REDIRECT --to-port 8080

-A PREROUTING -p tcp -d dest.ip.goes.here --dport 80 -j REDIRECT --to-port 8080

COMMIT
