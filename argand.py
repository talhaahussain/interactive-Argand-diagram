#---T♠ - 09/05/2020: 'COMPLEX NUMBERS IDEA'

#---initialisation
import pygame, sys, random, time, math
from pygame.locals import *
pygame.init()
#---instructions
print("\n")
print("Hello user!")
time.sleep(1)
print("This program is designed to display Complex Numbers on an Argand Diagram.")
time.sleep(2)
print("This program was developed by Talhaa Hussain, beginning on 09/05/2020. Not for redistribution or resale.")
time.sleep(2.5)
print("A new window will open. When it does, there will be two points on an Argand Diagram, labelled 'z' and 'w'.")
time.sleep(2)
print("These points can be controlled using the ARROW KEYS (for point z) and WASD (for point w).")
time.sleep(2)
print("On the right hand side, information about the current values of z and w can be found. All calculations are tested and accurate, all angles are in RADIANS.")
time.sleep(2)
print("Press the SPACEBAR to manually enter the values of z and w. Return to this window to do so.")
time.sleep(2)
print("Both z and w are colour-coded. All colours are randomly generated out of the colours of the rainbow. This may mean that z and w could be the same colour.")
print("In the event that this happens, you have my greatest sympathies.")
time.sleep(2.5)
print("That is all the information you need.")
print("You can view this information at any time while the program is running by clicking on this window and scrolling to the top of the Python shell.\n")
time.sleep(3)
print("The new window will now launch...")
for i in range(3):
    print(".\n")
    time.sleep(0.5)
print("Launched.")
#---set_display/framerate
pygame.display.set_caption("Argand Diagram")
screen = pygame.display.set_mode((1250, 800))
clock = pygame.time.Clock()
#---text_setup
font1 = pygame.font.SysFont("cambriacambriamath", 20)
font1.set_italic(1)
font2 = pygame.font.SysFont("cambriacambriamath", 20)
#---colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (46, 43, 95)
violet =(139, 0, 255)

#---complex_number_class
class Complex_Number:
    #---initialising_all
    def __init__(self, name, ctrls, id_number):
        self.ctrls = ctrls
        self.name = name
        self.id = id_number
        self.dx = 1
        self.dy = 1
        self.x = 400
        self.y = 400
        self.colour = random.choice((red, orange, yellow, green, blue, indigo, violet))
        self.x_value = self.x

    #---movement_function
    def move(self):
        if pressed_keys[self.ctrls[0]] and self.x >= 85:
            self.x -= self.dx
        if pressed_keys[self.ctrls[1]] and self.x <= 715:
            self.x += self.dx
        if pressed_keys[self.ctrls[2]] and self.y >= 85:
            self.y -= self.dy 
        if pressed_keys[self.ctrls[3]] and self.y <= 715:
            self.y += self.dy
        #self.x +=self.dx
        #self.y +=self.dy

    #---drawing_function
    def draw(self):
        pygame.draw.circle(screen, (self.colour), (self.x,self.y), 5) #draws point

    def lines(self):
        pygame.draw.line(screen, (self.colour), (400, 400), (self.x, self.y), 3)#line from origin
        pygame.draw.line(screen, (black), (self.x, 400), (self.x, self.y), 1)#x-line
        pygame.draw.line(screen, (black), (400, self.y), (self.x, self.y), 1)#y-line

    def accelerate(self):
        self.dx = 5
        self.dy = 5

    def reset_speed(self):
        self.dx = 1
        self.dy = 1

    def manual_entry(self): # A new function created to manually allow entry of complex numbers
        print("\n")
        print("Manual entry called.")
        print("Accepts only INTEGERS and values between -9 and 9, inclusive.")
        print("Any FLOAT values entered will be read as INTEGERS.")
        print("WARNING: DO NOT ATTEMPT TO INTERACT WITH THE PYGAME WINDOW WHILE MANUAL ENTRY INPUTS ARE ACTIVE. THIS WILL RESULT IN THE PROGRAM FAILING.\n")
        time.sleep(1)
        global manual_re
        manual_re = float(input("Enter a value for Re(" + self.name + ")."))
        while -9 > manual_re or manual_re > 9:
            print("Value out of range. Please try again.")
            manual_re = float(input("Enter a value for Re(" + self.name + ")."))

        global manual_im    
        manual_im = -float(input("Enter a value for Im(" + self.name + ")."))
        while -9 > manual_im or manual_im > 9:
            print("Value out of range. Please try again.")
            manual_im = -float(input("Enter a value for Im(" + self.name + ").")) #NEGATIVE DUE TO AXIAL INVERSION
        print("Updated. Check the other window.")
            

    def set_manual(self):
        self.x = int((35*manual_re) + 400)
        self.y = int((35*manual_im) + 400) #Converts to coordinates for pygame using position-to-term formula (shown in notes)
            
        
    
    #---edge_detection_function [REDUNDANT]
    #def edge(self):
    #    if 85 >= self.x or 715 <= self.x:
    #        self.dx = 0
    #        #self.dx *= -1
    #    if 85 >= self.y or 715 <= self.y:
    #        self.dy = 0
    #        #self.dy *= -1

    #---text
    def text(self):
        x = (self.x-400)/35
        y = -(self.y-400)/35
        screen.blit(font1.render(str(self.name) + "= " + str(round(x, 2)) + " + " + str(round(y, 2)) + "i", True, (self.colour)), (self.x, self.y))

        #---working_out_the_modulus
        self.modulus = math.sqrt(x**2 + y**2)
        #print(self.modulus)
        screen.blit(font1.render(str("Re(" + self.name + ") = ") + str(round(x, 2)), True, (self.colour)),(850,100+self.id*300))
        screen.blit(font1.render(str("Im(" + self.name + ") = ") + str(round(y, 2)), True, (self.colour)),(850,150+self.id*300))
        screen.blit(font1.render(str("|"+ self.name + "| = ") + str(round(self.modulus, 2)), True, (self.colour)),(850,200+self.id*300))

        #---working_out_the_argument
        if x == 0:
            if y > 0:
                self.argument = round((math.pi/2),2)
            elif y < 0:
                    self.argument = round(-(math.pi/2),2)
            else:
                self.argument = 0
        elif y == 0:
            if x > 0:
                self.argument = 0
            elif x < 0 :
                self.argument = round((math.pi),2)
        else:
            if x > 0:
                self.argument = math.atan(y/x)
            elif x < 0 and y > 0:
                self.argument = math.pi + math.atan(y/x)
            elif x < 0 and y < 0:
                self.argument = -(math.pi - math.atan(y/x))

        screen.blit(font1.render(str("arg(" + self.name + ") = ") + str(round(self.argument, 2)), True, (self.colour)),(850,250+self.id*300))
        #---modulus-argument form
        screen.blit(font1.render(str(self.name + " = [") + str(round(self.modulus, 2)) + ", " + str(round(self.argument, 2)) + "]", True, (self.colour)),(850,300+self.id*300))
        screen.blit(font1.render(str(self.name + " = ") + str(round(self.modulus, 2)) + "(cos(" + str(round(self.argument, 2)) + ") + isin(" + str(round(self.argument, 2)) + "))", True, (self.colour)),(850,350+self.id*300))

        
#---Axis_class
class Axis:
    #---initialising_all_variables
    def __init__(self):
        pass

    #---draws_axis
    def draw(self):
        #---axis
        pygame.draw.line(screen, black, (400, 50), (400, 750), 5)
        pygame.draw.line(screen, black, (50, 400), (750, 400), 5)
        #---arrowheads
        pygame.draw.line(screen, black, (400, 50), (395, 60), 5)
        pygame.draw.line(screen, black, (400, 50), (405, 60), 5)

        pygame.draw.line(screen, black, (750, 400), (745, 395), 5)
        pygame.draw.line(screen, black, (750, 400), (745, 405), 5)

        pygame.draw.line(screen, black, (50, 400), (55, 405), 5)
        pygame.draw.line(screen, black, (50, 400), (55, 395), 5)

        pygame.draw.line(screen, black, (400, 750), (405, 740), 5)
        pygame.draw.line(screen, black, (400, 750), (395, 740), 5)
        #Re/Im_text    
        screen.blit(font1.render(str("Re"), True, (black)) ,(750, 400))
        screen.blit(font1.render(str("Im"), True, (black)) ,(400, 25))
        #Numbers_text(x)
        screen.blit(font2.render(str("-9"), True, (black)) ,(85-9, 400))
        screen.blit(font2.render(str("-8"), True, (black)) ,(120-9, 400))
        screen.blit(font2.render(str("-7"), True, (black)) ,(155-9, 400))
        screen.blit(font2.render(str("-6"), True, (black)) ,(190-9, 400))
        screen.blit(font2.render(str("-5"), True, (black)) ,(225-9, 400))
        screen.blit(font2.render(str("-4"), True, (black)) ,(260-9, 400))
        screen.blit(font2.render(str("-3"), True, (black)) ,(295-9, 400))
        screen.blit(font2.render(str("-2"), True, (black)) ,(330-9, 400))
        screen.blit(font2.render(str("-1"), True, (black)) ,(365-9, 400))
        screen.blit(font2.render(str("1"), True, (black)) ,(435-6, 400))
        screen.blit(font2.render(str("2"), True, (black)) ,(470-6, 400))
        screen.blit(font2.render(str("3"), True, (black)) ,(505-6, 400))
        screen.blit(font2.render(str("4"), True, (black)) ,(540-6, 400))
        screen.blit(font2.render(str("5"), True, (black)) ,(575-6, 400))
        screen.blit(font2.render(str("6"), True, (black)) ,(610-6, 400))
        screen.blit(font2.render(str("7"), True, (black)) ,(645-6, 400))
        screen.blit(font2.render(str("8"), True, (black)) ,(680-6, 400))
        screen.blit(font2.render(str("9"), True, (black)) ,(715-6, 400))
        #Numbers_text(y)
        screen.blit(font2.render(str("-9"), True, (black)) ,(375, 715-12))
        screen.blit(font2.render(str("-8"), True, (black)) ,(375, 680-12))
        screen.blit(font2.render(str("-7"), True, (black)) ,(375, 645-12))
        screen.blit(font2.render(str("-6"), True, (black)) ,(375, 610-12))
        screen.blit(font2.render(str("-5"), True, (black)) ,(375, 575-12))
        screen.blit(font2.render(str("-4"), True, (black)) ,(375, 540-12))
        screen.blit(font2.render(str("-3"), True, (black)) ,(375, 505-12))
        screen.blit(font2.render(str("-2"), True, (black)) ,(375, 470-12))
        screen.blit(font2.render(str("-1"), True, (black)) ,(375, 435-12))
        screen.blit(font2.render(str("1"), True, (black)) ,(385, 365-12))
        screen.blit(font2.render(str("2"), True, (black)) ,(385, 330-12))
        screen.blit(font2.render(str("3"), True, (black)) ,(385, 295-12))
        screen.blit(font2.render(str("4"), True, (black)) ,(385, 260-12))
        screen.blit(font2.render(str("5"), True, (black)) ,(385, 225-12))
        screen.blit(font2.render(str("6"), True, (black)) ,(385, 190-12))
        screen.blit(font2.render(str("7"), True, (black)) ,(385, 155-12))
        screen.blit(font2.render(str("8"), True, (black)) ,(385, 120-12))
        screen.blit(font2.render(str("9"), True, (black)) ,(385, 85-12))
        


class Numbers:
    #---initialising_all_variables
    def __init__(self):
        pass
    


#---instance
axis = Axis()
z = Complex_Number( "z", [K_LEFT, K_RIGHT, K_UP, K_DOWN], 0 ) #Previously these two were created in the list, now they are standalone instances, with their own attributes...
w = Complex_Number( "w", [K_a, K_d, K_w, K_s], 1 )#(creates both complex numbers, and passes the 'ctrls' in.)
complex_numbers = [z, w]#...which are then moved into this list.

#z = Complex_Number()
#w = Complex_Number()

#gameloop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
#---REDUNDANT
    #if event.type == KEYDOWN and event.key == K_SPACE:
    #    Complex_Number.accelerate()
    #else:
    #    Complex_Number.reset_speed()
#---
    #---keys_pressed_setup
    pressed_keys = pygame.key.get_pressed()
    #---screen_colour
    screen.fill(white)
    #---axis
    axis.draw()
    #---functions_on_instance
    for complex_number in complex_numbers:
        complex_number.move()
        complex_number.draw()
        complex_number.lines()
        #---manual_entry
        if event.type == KEYDOWN and event.key == K_SPACE:
            complex_number.manual_entry()
            complex_number.set_manual()
            
    #z.edge()
        complex_number.text()
    

    #---display_refresh    
    pygame.display.update()


pygame.quit()

#---notes
#Parameters of the Argand diagram are (50, 50)[TL], (50, 750)[TR], (750, 50)[BL], (750, 750)[BR], (400, 400)[C].
#cont... (400, 50)[TOP], (50, 400)[LEFT], (400, 750)[BOTTOM], (750, 400)[RIGHT], (400, 400)[CENTER]
#Since the screen is 800 by 800, I have left a 50px offset for the Argand Diagram for all directions.
    
    
#nth term for the coordinate of on the argand diagram vs pygame: a = 35b + 400
#the above is where b is the value on the argand diagram, and a is the pygame coordinate value.
#In the form b = a...
#(-10 = 50)
#-9 = 85
#-8 = 120
#-7 = 155
#-6 = 190
#-5 = 225
#-4 = 260
#-3 = 295
#-2 = 330
#-1 = 365 
#0 = 400
#1 = 435
#2 = 470
#3 = 505
#4 = 540
#5 = 575
#6 = 610
#7 = 645
#8 = 680
#9 = 715
#(10 = 750)
#Essentially, the position-to-term formula is u(n) = 35n + 400
#And the recurrence relation is u(n+1) = u(n) + 35, where u(1) = 435, u(0) = 400, and u(-80/7) = 0
