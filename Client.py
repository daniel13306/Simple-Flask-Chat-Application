import requests
import json

# Make sure you change this link to fit your own URL.
SELF_URL = "https://yourwebsite.com"


# This function prints \n 30* to remove other messages from the screen.
def UltraEnter():
    for i in range(30):
        print("\n")

UltraEnter()
username = input("Enter your Username:\n")
UltraEnter()

# This function is called to create a room
def CreateRoom():
    UltraEnter()
    INP = input("How do you want to call your room:\n")
    url = f'{SELF_URL}/chatrm/CREATEROOM'
    data = {'roomname': f'{INP}'}
    r = requests.post(url, json = data)
    print(f"Server: {r.text}")
    UltraEnter()
    GetRooms()

# This function is called to create a brand new room
def GetRooms():
    UltraEnter()
    r = requests.get(f"{SELF_URL}/chatrm/GETROOMS")
    Room_IDS, Room_NAMES, Room_MESSAGES, RoomData = [], [], [], r.json()
    for i in RoomData:
        Room_IDS.append(i[0])
        Room_NAMES.append(i[1])
        Room_MESSAGES.append(i[2])

    print("𝐒𝐞𝐥𝐞𝐜𝐭 𝐚 𝐫𝐨𝐨𝐦 𝐛𝐞𝐥𝐨𝐰.")
    for i in range(len(RoomData)):
        print(f"Room: {Room_IDS[i]} Name: {Room_NAMES[i]}\n")
    INP = input("Enter a room number:\n")
    INP = int(INP) - 1
    UltraEnter()
    print(f"Room {INP+1}:")
    print(Room_MESSAGES[int(INP)])
    SEND_MESSAGE = input("Send a message:\n")
    SEND_MESSAGE = f"\n{username}: {SEND_MESSAGE}\n"

    url = f'{SELF_URL}/chatrm/SENDMSG'
    data = {'roomid': f'{INP+1}', 'message': f'{SEND_MESSAGE}'}
    r = requests.post(url, json = data)
    print(f"Server: {r.text}")
    UltraEnter()
    GetRooms()





print("1. Load Chatrooms")
print("2. Create Chatroom")
INP = input("What do you want to do?\n")
if INP == "1":

    GetRooms()
if INP == "2":
    CreateRoom()
