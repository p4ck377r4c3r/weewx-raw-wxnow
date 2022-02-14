rawwxnow.txt is a weewx extension that emits a wxnow.txt file that is in raw packet form for programs that read raw files

Installation instructions:
  run in terminal

1) git clone https://github.com/p4ck377r4c3r/weewx-raw-wxnow
2) sudo wee_extension --install ~/weewx-raw-wxnow/
3) sudo /etc/init.d/weewx restart 
4) point your aprs program to /var/tmp/wxnow.pkt

Jonathan Delaney
