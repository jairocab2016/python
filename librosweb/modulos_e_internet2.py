from ftplib import FTP

# Conectarse con los metodos connect y login
ftp = FTP()
ftp.connect('sr-sigmaserv-ad01', 22, -999)
ftp.login('miuser', 'miclave')

# Conectarse en la instancia a FTP
ftp = FTP('66.228.52.93', 'miuser', 'miclave')

# -*- coding: utf-8 -*-
from ftplib import FTP

ftp = FTP()
ftp.connect('66.228.52.93', 21, -999)
ftp.login('user', 'pass')
print ftp.getwelcome()
ftp.mkd('nuevo-dir')
ftp.cwd('nuevo-dir')
print ftp.pwd()
ftp.storlines('STOR example.txt', open('ftp_examples.py', 'r'))
ftp.rename('example.txt', 'example.py')
ftp.dir()
archivo = ftp.retrlines('RETR example.py')
print archivo
ftp.close()