define e = Character("Eileen")

label start:
    scene bg room
    show eileen happy
    Eileen "Suhhh dude"
    jump chapter1_start
    return

# # Python code run at initialization before the game loads
# # This is where we define classes and functions, or to initialize styles, config variables, or persistent data
# init python:
#     class fighter:
#         def init(self, name, level = 1, max_hp = 10, hp = 10, max_mp = 4, mp = 4, element = "None"):
#             self.name = name
#             self.level = level
#             self.max_hp = max_hp
#             self.hp = hp
#             self.max_mp = max_mp
#             self.mp = mp
#             self.element = element


# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")


# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg room

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show eileen happy

#     # These display lines of dialogue.

#     e "You've created a new Ren'Py game."

#     e "Once you add a story, pictures, and music, you can release it to the world!"

#     # This ends the game.

#     return
