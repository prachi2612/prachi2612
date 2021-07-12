import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
ser = serial.Serial("COM2", 9600)
print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)
a=[]
str1=str(ser.readline())
a=str1.split(",")
humi=a[0]
humi=humi[5:]
temp=a[1]
temp=temp[3:]
rain=a[2]
rain=rain[3:]
cm=a[3]
cm=cm[:-2]
flow=a[4]
flow=flow[:-5]

print(flow)
while res:
     cc=str(1234)
     print(cc)
     val=cc
     firebase1 = firebase.FirebaseApplication('https://flood-prediction-system-48428-default-rtdb.firebaseio.com/', None)##paste your firebase url
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data = { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':humi,
               'time': datetime.now().strftime("%H:%M")
          }
             result = firebase1.patch('https://flood-prediction-system-48428-default-rtdb.firebaseio.com/'+ '/humidity_data/'+ str(i), data)##paste your firebase url
             print(result)
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data = { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':temp,
               'time': datetime.now().strftime("%H:%M")
          }
             result = firebase1.patch('https://flood-prediction-system-48428-default-rtdb.firebaseio.com/'+ '/temperature_data/'+ str(i), data)##paste your firebase url
             print(result)
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data = { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':rain,
               'time': datetime.now().strftime("%H:%M")
          }
             result = firebase1.patch('https://flood-prediction-system-48428-default-rtdb.firebaseio.com/'+ '/rain_data/'+ str(i), data)##paste your firebase url
             print(result)
     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data = { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':cm,
               'time': datetime.now().strftime("%H:%M")
          }
             result = firebase1.patch('https://flood-prediction-system-48428-default-rtdb.firebaseio.com/'+ '/distance_data/'+ str(i), data)##paste your firebase url
             print(result)


     for i in range(0,4):
             string1="123"
             #string1=str(ser.readline())
             #string1=string1[9:][:-6]
             data = { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':flow,
               'time': datetime.now().strftime("%H:%M")
          }
             result = firebase1.patch('https://flood-prediction-system-48428-default-rtdb.firebaseio.com/'+ '/flow_data/'+ str(i), data)##paste your firebase url
             print(result)

     res = 0
