# CSF ALLOW DOMAINS
If you're using [CSF firewall](http://configserver.com/cp/csf.html) and your app relies heavily on an external service like Twitter or Facebook, chances are that your firewall will block those any time soon and you will have to white list them in /etc/csf/csf.allow. 

This happened to us while doing a stress test that left us with no database access. If it would have happened on production, caused by user traffic, it would be a serious issue.

But firewalls enjoy working with IPs not domain names... Here comes this module. With it you can list domain names that will get resolved and added to the CSF settings file. It does not delete any domains from the file so some spring clean may be needed from time to time. Some domains may return different sets of A records throughout time, even if they are all valid servers at any given moment, eg. github.


# Install
This module was only (barely) tested in Ubuntu 14.04

## Debian Package

- download [csf-allow-domains.deb](csf-allow-domains.deb)
- dpkg -i ./csf-allow-domains.deb

## Manual Install
All the relevant code can be found in [./usr/local/csf/bin/csf-allow-domains](/usr/local/csf/bin/csf-allow-domains)
Just copy those files to your system, update the config.py and use whatever strategy you want to keep the python script going.