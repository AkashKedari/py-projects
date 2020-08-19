# Flappy Bird!

Yes, this is the game that we all were addicted to back in 2013. This is a clone of the beloved flappy bird but written in python.


### Some edits

The first thing is that some of the comments might not match up to the code. For example, on the very bottom, it says "not faster than 120 FPS" when clearly Clock tick is set to 75 FPS. I have modified some things to make it work on a smaller scale liek the original game.

The score keeping mechanism is still a bit buggy because it doesn't count exactly til the bird passes the pipes. It counts sometimes
slightly before or slightly after. I am working on another solution to that problem. 

One minor issue with graphics is that I coded a way to flip the pipes if they are on the top or bottom, but there is one specific
height where this does not happen. It occurs rarely but I will figure out and update the list when I do figure out that height.

