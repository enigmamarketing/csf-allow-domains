# CSF ALLOW DOMAINS

Allows whitelisting all ips in a domain name by resolving the A records for those domain names and placing them in /etc/csf/csf.allow

It does not delete any domains from the file so some spring clean may be needed from time to time. Some domains may return different sets of A records throughout time, even if they are all valid servers at any given moment, eg. github.


# Install
This module was only tested in Ubuntu 14.04

## Debian Package

- download [csf-allow-domains.deb](csf-allow-domains.deb)
- dpkg -i ./csf-allow-domains.deb

## Manual Install
All the relevant code can be found in [./usr/local/csf/bin/csf-allow-domains](/usr/local/csf/bin/csf-allow-domains)
Just copy those files to your system, update the config.py and use whatever strategy you want to keep the python script going.

