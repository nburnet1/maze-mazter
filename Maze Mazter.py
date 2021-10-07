# Noah Burnette
# Import pygame
import pygame
import time
import os
import random
# Intializing Pygame
pygame.init()
# Major variables will be stored (Here) 
display_width = 600
display_height = 600
black = (0,0,0)
# Intitializing the window
game_display = pygame.display.set_mode(size = (display_width,display_height))
game_fill = game_display.fill(black)
caption = pygame.display.set_caption("Maze Mazter")
pygame.display.update()
# Picture paths as variables or in character's list:
#   test = "Pictures/test.png"
# Functions 
#   Image translation
#       Arguments:
#           The file location of the image
def img_fit(img):
    load_img = pygame.image.load(img)
    game_display.blit(load_img,(0,0))
    pygame.transform.scale(load_img,(600,600))
    pygame.display.update()

# Intro
frme =0
while frme <= 1000:
    if frme < 125:
        img_fit("Pictures/intro_1.png")
    if frme >= 125 and frme < 250:
        img_fit("Pictures/intro_2.png")
    if frme >= 250 and frme < 375:
        img_fit("Pictures/black_space.png")
    if frme >= 375 and frme < 500:
        img_fit("Pictures/intro_3.png")
    if frme >= 500 and frme < 625:
        img_fit("Pictures/intro_4.png")
    if frme >= 625 and frme < 750:
        img_fit("Pictures/intro_5.png")
    if frme >= 750 and frme < 875:
        img_fit("Pictures/intro_6.png")
    if frme >= 875 and frme < 1000:
        img_fit("Pictures/black_space.png")
        
    frme += 10    

img_fit("Pictures/strange_being.png")        
        

# Character Creation
#   Character list:
#       Name
#       Age
#       Strength
#       Agility
#       Luck
#       Trade
#       Instinct
#       Total Health
#       Fatigue
#       Current Health
char_list = []
print("\nHint: Click on the shell when typing inputs and the window for everything else\n")
print("Now is the time to adjust both windows as well.")
char_name = input("What is your name?\n")
while True:
    char_age = int(input("How old are you?\n"))
    if char_age < 13:
        print("There is no way a child could survive that fall...\n")
    if char_age > 60:
        print("I find that hard to believe based on the fall you took...\n")
    if char_age >= 13 and char_age <= 60:
        print(str(char_age)+"..."+"Interesting...\n")
        break
    
char_str = 0
char_agl = 0
char_luck = 0
char_trade = 0
char_instinct = 0
char_list.append(char_name)
total_attrib_points = random.randrange(10,15)
attrib_points_used = 0
# Loop to ensure the attributes cannot be exploited
while True:
    print("You have",total_attrib_points,"attribute points to use\n\n")
    char_str = int(input("How strong are you?\n"))
    char_agl = int(input("How agile are you?\n"))
    char_luck = int(input("How lucky are you?\n"))
    char_trade = int(input("How charasmatic are you?\n"))
    char_instinct = int(input("How instinctual are you?\n"))
    attrib_points_used = char_str + char_agl + char_luck + char_trade + char_instinct
    if attrib_points_used == total_attrib_points:
        char_list.append(char_str)
        char_list.append(char_agl)
        char_list.append(char_luck)
        char_list.append(char_trade)
        char_list.append(char_instinct)
        break
    else:
        attrib_points_used = 0
# Dialogue from the first interaction dependent on age
if char_age < 18:
    print("""\nFrom your age and where you are now, I am guessing you are the unwanted child.
Perhaps you had no parents and you were thrown down the well by a jealous classmate.""")

if char_age >= 18 and char_age < 30:
    print("""\nFrom your age and where you are now, I am guessing your significant other was having an affair.
Perhaps you do not have a spouse and you were thrown down the well by your life long friend.""")

if char_age >= 30 and char_age < 45:
    print("""\nFrom your age and where you are now, I am guessing you are to successful in your trade.
Perhaps you do not have a trade and you were thrown down the well by your community because you are a leech.""")

if char_age >= 45 and char_age <= 60:
    print("""\nFrom your age and where you are now, I am guessing someone wants your property.
Perhaps you do not have property and you were thrown down the well by your children because you are a terrible parent.""")

print("""\nNonetheless, you cannot go back the way you came.
But there is a path that will lead somewhere eventually.
Best get to walking """+char_list[0]+".\n")


# NPC List: 
# 0  Name
# 1  Image Path
# 2  Strength
# 3  Agility
# 4  Luck
# 5  Trade
# 6  Instinct
# 7  Interaction
# 8  Combat
# 9  Health
# 10  Magic Immune

# enemies
enemy_rat = ["Rat","Pictures/enemy_rat.png",2,3,1,0,0,True,True,False]
enemy_knight = ["Knight","Pictures/enemy_knight.png",4,2,2,2,1,True,True,False]
# trainers, merchants, etc...
trainer_agl = ["Trainer(Agility)","Pictures/trainer_agl.png",0,0,0,6,5,True,False]
# Terrain
path_1 = ["Path_1","Pictures/path_1.png",0,0,0,0,0,0,False]
path_2 = ["Path_2","Pictures/path_2.png",0,0,0,0,0,0,False]
path_3 = ["Path_3","Pictures/path_3.png",0,0,0,0,0,0,False]
path_4 = ["Path_4","Pictures/path_4.png",0,0,0,0,0,0,False]
path_5 = ["Path_5","Pictures/path_5.png",0,0,0,0,0,0,False]
path_6 = ["Path_6","Pictures/path_6.png",0,0,0,0,0,0,False]
# Magic file path = [name,image path,self]
magic_absorb = "Pictures/magic_absorb.png"
magic_burn = "Pictures/magic_burn.png"
magic_crit = "Pictures/magic_crit.png"
magic_defense = "Pictures/magic_defense.png"
magic_escape = "Pictures/magic_escape.png"
magic_heal = "Pictures/magic_heal.png"
magic_paralyze = "Pictures/magic_paralyze.png"

# Randomizers that will be created(Here):
#   Encounters, Locations, Chance to hit(Based off attributes above^)
rand_encounter_list  = [enemy_rat,enemy_knight,trainer_agl,path_1,path_2,path_3,path_4,path_5,path_6]



# The Running loop... Very Important
print("press \'h\' anytime to get help")
Running = True
First_Interaction = True
Interaction = False
Combat = False
Instinct_Checker = False
Magic = False
Resting = False
Dialogue = False
arb_enc = []
gold = 0
spells_aquired = []
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.display.quit()
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                print("resting")
# Help Condition
            if event.key == pygame.K_h:
                print("Press the arrow keys to move while not in an interaction or combat\n\'r\' to rest\n\'s\' to view your stats")
# Movement Condition
            if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#               Minus fatigue here
                arb_enc = rand_encounter_list[random.randrange(0,len(rand_encounter_list))]
                img_fit(arb_enc[1])
                Interaction = arb_enc[7]
                Instinct_Checker = arb_enc[7]
# Back Arrow Condition
            if event.key == pygame.K_DOWN:
                print("I can't go back, I really need to get out of here...")




#Interaction loop is engaged any time there is a NPC present
    while Interaction:
# Compares Instinct in order to scout the NPC 
        while Instinct_Checker:
            if char_list[5] > arb_enc[6]:
                print("I have encountered a",arb_enc[0])
            else:
                print("I have encountered an unknown being")
            Instinct_Checker = False
        for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_d:
                      print("dialogue here")
#Instinct 
                  if event.key == pygame.K_i:
                      if char_list[5] * .5 > arb_enc[6]:
                          print("Scouting")
#Exit Interaction condition
                  if event.key == pygame.K_w:
                      if arb_enc[8] == False:
                          Interaction = False
                          print("I have exited this interaction")
                      elif char_list[2] > arb_enc[3]:
                          print("I can't believe I ran away...")
                          Interaction = False
                      else:
                          Interaction = False
                          print("I am not adapted enough to leave this interaction...\nI must prepare to fight...")
                          Combat = True 
                          
# Help Condition    
                  if event.key == pygame.K_h:
                      print("Press \'a\' to attack\n\'d\' for dialogue\n\'w\' to exit this interaction if possible\n\'i\' to use your instincts")
# Engage/Attack Condition
                  if event.key == pygame.K_a:
                      Combat = arb_enc[8]
                      Interaction = False
                      print("In combat")
                      if Combat == False:
                          print("I cannot attack this being\nThey have lost interest in me...")
                    


                
# Combat loop, used only after the interaction mode
    while Combat:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
# Stat condition (Health,Fatigue, etc...)
                if event.key == pygame.K_s:
                    print("posting stats")
# Attack Condition 
                if event.key == pygame.K_a:
                    print("attacking")
# Help Condition 
                if event.key == pygame.K_h:
                    print("Press \'a\' to do physical damage\n\'s\' to view your stats\n\'m\' for magic if you possess the skill")
# Magic Condition
                if event.key == pygame.K_m:
                    Magic = True
                    while Magic:
                        print("casting magic")
                        Magic = False
                        
                    
                if event.key == pygame.K_q:
                    print("quitting")
                    Combat = False
                      
        
      
    
    

