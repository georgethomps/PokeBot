# PokeBot

**Project Description**

PokeBot is a Discord bot that allows one to send comments to users that are mentioned in Discord
text messages.

&nbsp;

**Bot Behavior**

When you are sending messages in Discord (through text chat), PokeBot will send out comments
if certain users/names are mentioned in a Discord message. For example, if you tell the bot to
send comments if "Noah" is mentioned in a message (this is not case sensitive):

EXAMPLE
User: "Hey Noah, the bot is going to send you a joke"
Bot: "[insert terrible joke here]"

PokeBot can also send jokes if multiple users are mentioned:

EXAMPLE
User: "Hey Noah and George, the bot has some words for both of you"
Bot: "Noah, I hope you're having a great day!"
Bot: "George, you're a really weird guy."

What's great about PokeBot is that you can have certain comments designated for specific users.
For example, you can have a text file that has potential comments designated for George and another
text file that contains comments designated for Noah. When either of these users are mentioned,
PokeBot will randomly select a comment for George from his designated comment file and randomly
select a comment for Noah from his designated comment file.

&nbsp;

**The Poke List**

To target certain users for the bot to send comments to users, you can use the Poke List to load
or unload users from the list. Users that are on the Poke List will be targeted by PokeBot. To add
users, they must have a user profile created before they can be added.

&nbsp;

**The Data Manager**

The data manager allows you to create user profiles so PokeBot will be able to retrieve comments
to send to certain users. For example, one profile will contain the name that will trigger the 
PokeBot as well as the text file that PokeBot should select a comment to send from.

&nbsp;

**Documentation Guide**

For a better understanding of how this program works, you can view the documentation in the doc
folder.


FILES:

commands.txt: Contains all the commands available for you to use.
modules.txt:  Contains information on the programs modules and how to create user profiles.
setup.txt:    Contains instructions on how to setup PokeBot on your Discord server.

&nbsp;

**Other Files**

This section pertains to all files and folders in the pokebot folder.

FILES:

PokeBot.py: the script that will run the bot on your server as well as its commands.


DATAMANAGER FOLDER:

users/user_data.txt: contains all user profile data. Do not modify this!!!
comments/example.txt: contains all text files that contain the comments to send to users

&nbsp;

**Additional Comments and Concerns**

At the moment, you will need to use a virtualenv to run the program. If this project gains more
support, I will then create a setup.py to make the installation process more feasible.

Furthermore, you must keep PokeBot.py running in a terminal for PokeBot to continue running.
Do not close the terminal or the Bot will stop!

Finally, the files in the DataManager should not be tampered with (except the comment files you
create). User settings should be managed through PokeBot's Discord commands.

