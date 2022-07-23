import pyshark

capture = pyshark.LiveCapture(interface="イーサネット")
for raw_socket in capture.sniff_continuously():
    #print(raw_socket)
    try:
        print(raw_socket.ip.src)
    except:
        print('Nothing')
