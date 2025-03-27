# Kamu dapat taruh script game mu di file ini.
init python:

    import time

    class ToSay():
        def __init__(self, color, outline=False):
            self.color = color
            self.outline = outline
            self.outlinecolora = "#ffffff"
        def say(self, dialogue):
            if self.outline==False:
                return f"{{color={self.color}}}{dialogue}{{color={self.color}}}"
            else:
                return f"{{color={self.color}}}{{outlinecolor={self.outlinecolora}}}{dialogue}{{/outlinecolor}}{{/color=}}"

define learnsummoning = False
define persistent.nexusunrevealing = 0

define humancolor = "#00ff00"
define demoncolor = "#ff0000"
define cultcolor = "#ffff00"
define playercolor = "#ffffff"
define thingcolor = "#bb80ffff"

define narrator = nvl_narrator

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define rudfourthwallbreak = ToSay(humancolor, outline=True)
define rud = ToSay(humancolor)
define eme = ToSay(cultcolor)
define nex = ToSay(demoncolor)
define acr = ToSay(demoncolor)
define let = ToSay(cultcolor)
define her = ToSay(demoncolor)
define col = ToSay(humancolor)
define cul = ToSay(cultcolor)
define darcitizen = ToSay(humancolor)
define darcultcitizen = ToSay(cultcolor)
define aaacitizen = ToSay(humancolor)
define aaacultcitizen = ToSay(cultcolor)
define tel = ToSay(thingcolor, outline=True)

# Game dimulai disini.
label start:

    window hide

    python:
        
        playername = renpy.input("Nama untuk karakter utama? (Default = Rudy)")
        playername = playername.strip() or "Rudy"
        sister = renpy.input("Nama untuk adik perempuan? (Default = Emerald)")
        sister = sister.strip() or "Emerald"

    jump act00

    return
