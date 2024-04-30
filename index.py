from zk import *
import requests
import json

machine_port = 4370
z = ZK('192.168.31.51', port=machine_port, force_udp=False, ommit_ping=False)
conn = z.connect()
z.enable_device()
z.live_capture()

api_url = "https://webhook.site/65e348fd-94f8-4364-9801-0045d2f4c825"

for attendance in conn.live_capture():
    if attendance is None:
        pass
    else:
        attendance_data = {
            'data': str(attendance) 
        }

        json_data = json.dumps(attendance_data)

        response = requests.post(api_url, json=json_data)
        
        if response.status_code == 200:
            print("Attendance entry sent successfully.")
        else:
            print("Failed to send attendance entry. Status code:", response.status_code)
        print(attendance)
