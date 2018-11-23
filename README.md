# Smugglers Run
### (Piratin' Simula'or 1819)

## Inspiration

We wanted to interpret the theme of "Changing Human computer interaction" in a fun and unique way but using a mixture of voice and physical input to enhance the theme and interactivity of a game. 

- We don't know why pirates either _

## What it does

 _ Ahoy Land Lubbers, for our hackerton project, we wanted to craft the finest pirating experience. Rather than those filthy pretend keyboard controls, Pirate Simula'or uses a real wheel you can grasp wit' yer hands ~shiver me timbers~. We also included a loyal crew for ye to yell yer commands at, so you can feel just like a real cap'in. _

The game uses an OpenCV object tracker to measure the position of our ship wheel which the user holds. This then feeds into the game where the boat responds with realistic physics. We also have speech recognition for more immersion which responds to commands such as "Full Sail!" to increase the speed 

## How we built it

We individually worked on each component of the game; the speech input, the wheel input and the game interface. Once completed with our section we collaborated to improve others code.

Also we found a cool 8-bit Pirates of the Caribbean remix to enhance the atmosphere

## Challenges we ran into

We initially tried to use a Wiimote to find the position of the wheel, this proved difficult as the Wiimote is not very compatible with non Linux systems. We instead changed to use OpenCV to track objects and calculate the angle of it.

We also ran out of time to integrate the speech processing element into the game. 

## Accomplishments that we're proud of

We are proud of managing to get a fairly complex image recognition system working having little to no experience in using image processing technologies. We were also happy with our usage of Git work on code simultaneously.  

## What we learned

Use Linux! 

## What's next for Pirate Simulator 2018

Finish implementing the voice control, then build a simple game involving enemy AI and a story complete with pirate loot, Durham City Council and a boss fight against the legendary Blackbeard!
