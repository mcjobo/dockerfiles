#!/usr/bin/python3.5

import subprocess
import os
from pathlib import Path
from sys import exit


if(Path('/etc/samba/.setup').exists()):
  subprocess.run('samba', shell=True, check=True);
  exit();

#dns_forwarder = "192.168.100.1"
#realm = "local.bolay.org"
#domain = "bolay"
#adminpass = "jb80049JB"

print("Install script for a dhcp server which updates it's coresponding samba 4 Active Directory Primary Domain Controller");



os.environ['DEBIAN_FRONTEND']='noninteractive';
subprocess.run('apt-get update && apt-get install -y isc-dhcp-server', shell=True, check=True);

#subprocess.run('rm /etc/samba/smb.conf', shell=True, check=True);
#subprocess.run(['samba-tool', 'domain', 'provision', '--use-rfc2307', '--use-ntvfs', '--realm', realm, '--domain', domain, '--adminpass', adminpass]);
#subprocess.run('samba-tool domain provision --use-rfc2307  --use-ntvfs --realm local.bolay.org --domain bolay --adminpass jb80049JB', shell=True, check=True);
#dns server neu setzten auf den localhost oder multiple dns server setzten
#os.rename('/etc/resolv.conf.orig', '/etc/resolv.conf');
#with open('/etc/resolv.conf', 'w+') as output, open('/etc/resolv.conf.orig', 'r') as input:
#    output.write(input.read())

#subprocess.run('cp /var/lib/samba/private/krb5.conf /etc/krb5.conf', shell=True, check=True);

subprocess.run('apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*', shell=True, check=True);

Path('/etc/dhcp/.setup').touch()
#subprocess.run('samba', shell=True, check=True);

