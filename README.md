# CSF ALLOW DOMAINS

Allows whitelisting all ips in a domain name by resolving the A records for those domain names and placing them in /etc/csf/csf.allow

It does not delete any domains from the file so some spring clean may be needed from time to time. Some domains may return different sets of A records throughout time, even if they are all valid servers at any given moment, eg. github.
