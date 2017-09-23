#!/usr/bin/python3

import subprocess
import os
from pathlib import Path
from sys import exit


if(Path('/etc/samba/.setup').exists()):
  subprocess.run('samba', shell=True, check=True);
  exit();


print("Install script for a dhcp server which updates it's coresponding samba 4 Active Directory Primary Domain Controller");



os.environ['DEBIAN_FRONTEND']='noninteractive';
subprocess.run('apt-get update && apt-get install -y isc-dhcp-server samba krb5-user', shell=True, check=True);

os.chmod('/etc/dhcp/dhcpd-update-samba-dns.sh', 0o700);
os.chmod('/etc/dhcp/samba-dnsupdate.sh', 0o700);


subprocess.run('apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*', shell=True, check=True);
Path('/etc/dhcp/.setup').touch();
Path('/var/lib/dhcp/dhcpd.leases').touch();
subprocess.run('/usr/sbin/dhcpd -q  -cf /etc/dhcp/conf/dhcpd.conf eth0', shell=True, check=True)

