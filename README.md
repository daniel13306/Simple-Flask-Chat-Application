# Simple-Flask-Chat-Application
Simple chat application with a Server, Database & Client, Powered by Python, Flask & Sqlite3!

![alt text](https://s20.directupload.net/images/220109/hpwfzunf.png) Written by DeadEagle

WHAT CAN YOU DO
-------------
 
 * Create Chatrooms via the Client

   - Select option 2 in the client to create a new room.
   
   - On room Creation, You can choose a name for the room.
   
   - Choose a name on client startup to display in front of your message.

 * Join Chatrooms via the Client
 
   - Choose a name on client startup to display in front of your message.
   
   - Select 1 in the menu to Load Chatrooms, Then enter the chatroom ID you want to open in order to open a room.
     
   - Messages are sent to the server and saved in the database under the chatroom ID's data row.

 * How does the Flask server work?

   - The Flask server is contacted by the client via HTTP Requests, REMEMBER: If your website/Flask application does NOT use SSL/HTTPS, your messages are NOT encrypted! (If you have SSL, and force HTTP to HTTPS, for example with cloudflare, The messages are encrypted.)
   
   - The Flask server has 3 different Functions, One to Create a new room, this function takes JSON input (Room Name sent by Client)
   
   - Function two allows the Client to call this function in order to receive room data, (ROOM_IDS, NAMES, MESSAGES, And so on.)
   
   - Function three allows the Client to send a message, this function takes JSON input from the client in order to receive the wanted roomnumber, & user message.
   
   - Each function will respond back to the Client. 
   
 * How does the Sqlite3 Database work?

   - The "rooms" table is where all rooms are saved, containing: ROOMID, ROOMNAME, ROOMMESSAGES, and "yes", this last variable is here so the server can send the data, why? in this case, the server will get data from all rows containing a "yes" in the "yes" section.

   - The "count" table keeps track of the room ID Count.
 
   - Use this software to browse through the .db file: https://sqlitebrowser.org/
   
   
   
 * Simple Chatroom Client with Server & Database.
      
   - Made for Windows
    
   - This Software is [FREE] to use in ANY Case.

   

     Join our Community via the link;
     https://discord.gg/FTmrYbEN8w


 * Experience any Problems? Join our Discord.
   
   
   
   https://Coding-Community.com
   https://DeadEagle.nl
   https://Spitfire-Games.com
