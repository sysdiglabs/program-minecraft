# Learn to Program with Minecraft - Docker Edition

So you've bought ["Learn to Program with Minecraft"](https://nostarch.com/programwithminecraft) and need to set up your computer to run through the exercises. While the book gives detailed instructions to set everything up, this repo gives you what you need to run the Minecraft server and a Python development container to execute the exercises. Before proceeding, you'll need to install:

1. Java - Required to run Minecraft. http://www.oracle.com/technetwork/java/javase/downloads/index.html
2. Minecraft - To play the Game. https://minecraft.net/en-us/download/
3. MultiMC - Optional but recommened. https://multimc.org/
4. Docker - You'll use this to run the Minecraft Server and Python development container. https://www.docker.com/get-docker
5. Visual Studio Code - Not required, but provides an excellent text editor for programming. This provides the same (and more) functionality to IDLE which is referenced in the book. https://code.visualstudio.com/download

## Getting started

Once you've installed the above clone this repo using git, or download this repo using the button above. If you download a ZIP, you'll want to extract it to a folder of your choice. Open a terminal (or command line) and change into the folder. Run `docker-compose up` to start the Minecraft Server as well as a container with Python installed. That's it! You're now able to start coding the exercises in the book. 

## Source Code Location

Throughout the book you'll create small snippets of code to execute. Any code you create will need to be placed in the `src` directory. You can make sure you're saving things in the correct location by starting Visual Studio Code (Code for short), clicking the File menu, then clicking "Open Workspace". Select the src folder as the workspace and click open.

## Executing Your Python Scripts

The book will tell you to write your code in IDLE and then hit F5 to run it. In this environment you'll do things differently. Write your code in Code, save it to the `src` directory, then from a command line (or terminal) run `docker exec -it mc-pi-dev bash`. This will give you a terminal inside the Python development container. From here you can run `python <myscript>` where `<myscript>` is the name of the file containing your code. You can leave this terminal up while you're going through the exercises.

## Minecraft Data

All data for the Minecraft server is stored in the `data` directory. To reset the server, stop the server (`docker-compose down`), then remove all the files and folders in the `data` folder. The Minecraft Server will recreate these files when it starts. Note that this will also delete any Worlds you've created!

## Accessing the Minecraft Console

You might want to have access to the Minecraft Server's console to execute commands. You can run `docker exec -it mc-pi-srv rcon-cli` from a terminal to open the console. You can then issue server commands as you normally would on a Minecraft Server.

## Increasing the Memory Available to Minecraft

Depending on your system and depending on what you're building, you might need to increase the memory of the Minecraft Server. Edit the `docker-compose.yml` file, changing the server's environment variable "MEMORY". Currently it is set to 1G.
