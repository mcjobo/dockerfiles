#!/usr/bin/python3.5

import subprocess
import os
from pathlib import Path
from sys import exit


if(Path('/etc/samba/.setup').exists()):
  subprocess.run('samba', shell=True, check=True);
  exit();

dns_forwarder = "192.168.100.1"
realm = "local.bolay.org"
domain = "bolay"
adminpass = "jb80049JB"

print("Install script for a samba 4 Active Directory Primary Domain Controller");

# dns auf den externen forwarder setzen
with open('/etc/resolv.conf.orig', 'w+') as output, open('/etc/resolv.conf', 'r') as input:
    output.write(input.read())
#os.rename('/etc/resolv.conf', '/etc/resolv.conf.orig');
text_file = open("/etc/resolv.conf", "w");
text_file.write("nameserver %s" % dns_forwarder);
text_file.close()


os.environ['DEBIAN_FRONTEND']='noninteractive';
subprocess.run('apt-get update && apt-get install -y krb5-user samba', shell=True, check=True);

subprocess.run('rm /etc/samba/smb.conf', shell=True, check=True);
subprocess.run(['samba-tool', 'domain', 'provision', '--use-rfc2307', '--use-ntvfs', '--realm', realm, '--domain', domain, '--adminpass', adminpass, '--option=ldap server require strong auth = no']);
#dns server neu setzten auf den localhost oder multiple dns server setzten
#os.rename('/etc/resolv.conf.orig', '/etc/resolv.conf');
with open('/etc/resolv.conf', 'w+') as output, open('/etc/resolv.conf.orig', 'r') as input:
    output.write(input.read())

subprocess.run('cp /var/lib/samba/private/krb5.conf /etc/krb5.conf', shell=True, check=True);

subprocess.run('apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*', shell=True, check=True);

Path('/etc/samba/.setup').touch()
subprocess.run('samba', shell=True, check=True);
#subprocess.run('samba-tool dns update localhost local.bolay.org pdc A 172.17.0.3 192.168.100.50', shell=True, check=True);
