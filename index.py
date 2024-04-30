
from zk import *
machine_port = 4370
z = ZK('192.168.31.51', port=machine_port, force_udp=False, ommit_ping=False)
conn = z.connect()
z.enable_device()
z.live_capture()
attendances = conn.get_attendance()
conn.clear_attendance()
for attendance in conn.live_capture():
    if attendance is None:
        pass
    else:
        print (attendance)

