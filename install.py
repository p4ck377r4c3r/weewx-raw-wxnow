# installer for cwxn
# Copyright 2014-2020 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return RAWWXNOWInstaller()

class RAWWXNOWInstaller(ExtensionInstaller):
    def __init__(self):
        super(RAWWXNOWInstaller, self).__init__(
            version="1.0",
            name='rawwxnow',
            description='Emit a raw wxnow.pkt for LOOP data.',
            author="Jonathan Delaney",
            author_email="p4ck37ur4c3r@gmail.com",
            process_services='user.rawwxnow.RAWWXNOW',
            config={
                'RAWWXNOW' : {
                    'filename': '/var/tmp/wxnow.pkt'}},
            files=[('bin/user', ['bin/user/rawwxnow.py'])]
            )
