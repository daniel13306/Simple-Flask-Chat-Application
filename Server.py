from flask import Flask, render_template

app = Flask(__name__)

# Created by DeadEagle.
# www.DeadEagle.nl
# www.Coding-Community.com
# 2023

# This function gets called to create a new room.
@app.route('/chatrm/CREATEROOM' , methods = ['POST', 'GET'])
def ChatCRTROOM():
    content = request.json
    roomname = content['roomname']
    db = sqlite3.connect("chatroom.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT count FROM count WHERE yes='yes'")
    Output = cursor.fetchone()
    roomnumber = int(Output[0]) + 1
    cursor.execute(f"UPDATE count SET count= '{roomnumber}' WHERE yes='yes'")
    db.commit()
    cursor.execute(f"INSERT INTO rooms VALUES ('{roomnumber}','{roomname}','Room Start.\n','yes')")
    db.commit()
    return f"Room {roomname} Succesfully created [Room number: {roomnumber}]"

# This function gets called to get all available rooms with their data.
@app.route('/chatrm/GETROOMS')
def chatrmCNCT():
    db = sqlite3.connect("chatroom.db")
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM rooms WHERE yes='yes'")
    Output = cursor.fetchall()
    return Output


# This function gets called when a user sends a message to any chat room.
@app.route('/chatrm/SENDMSG' , methods = ['POST', 'GET'])
def ChatSENDMSG():
    db = sqlite3.connect("chatroom.db")
    cursor = db.cursor()
    content = request.json
    roomID = content['roomid']
    message = content['message']
    cursor.execute(f"SELECT roommessages FROM rooms WHERE roomid='{roomID}'")
    Output = cursor.fetchone()
    MSGpart = str(Output[0])
    fullmessage = MSGpart + message
    cursor.execute(f"UPDATE rooms SET roommessages= '{fullmessage}' WHERE roomid='{roomID}'")
    db.commit()
    return "Message sent."
    




if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=False,port=80)
