import serial

port = "COM4"
conn = serial.Serial(port, 115200)

message = input("Hello you!")
print(message)

if message:
    message = message.encode().strip()
    conn.write(message)

