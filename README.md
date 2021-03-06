# Swarmer
> A command-line tool for creating ephemeral server swarms


Swarmer launches and maintains a random swarm of decoy servers. These "will-o'-the-wisp" servers jump around continuously over a given portnumber space at regular intervals; they are intended to confuse and mislead network scanners (such as nmap).

<img src="READimage.png" alt="example" width="600" height="400" />
## Usage example

Running the starter.py on the command line instantiates a server swarm:

> ./starter.py

The -o ("occupied") and -n ("number") switches can be used to indicate ports that are already in use and to launch multiple server swarms with distinct parameters. Using either of these switches will prompt the tool to solicit user input:

> ./starter.py -o -n 3

<img src="Usage.png" alt="usage" width="600" height="400" />




## Meta

Patrick Kelly – patrickyunen@gmail.com

