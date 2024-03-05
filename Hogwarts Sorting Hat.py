# Step 1: Initialise the Sorting Hat
print("~~~~~~~~~~~~~~~~~~~~~~~")
print("~                     ~")
print("~   The Sorting Hat   ~")
print("~                     ~")
print("~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print("Welcome to Hogwarts school of witchcraft and wizardry!")
print("Answer the following questions to be assigned your new house.")
print("")
gryffindor = 0    
hufflepuff = 0
ravenclaw = 0
slytherin = 0

#gryffindor

gry = input("Are you a brave person?").lower()
if gry=="yes":
  gryffindor = gryffindor + 1
  
gry2 = input("Do you stand up for what you believe in, even when it's difficult?").lower()
if gry2=="yes":
  gryffindor = gryffindor + 1

gry3 = input("Do you have a strong sense of justice and fairness?").lower()
if gry3=="yes":
  gryffindor = gryffindor + 1

gry4 = input("Do you enjoy taking risks and challenges?").lower()
if gry3=="yes":
  gryffindor = gryffindor + 1
  
#hufflepuff 

huf = input("Are you a patient person?").lower()
if huf=="yes":
  hufflepuff = hufflepuff + 1

huf2 = input("Are you kind and compassionate towards others?").lower()
if huf2=="yes":
  hufflepuff = hufflepuff + 1

huf3 = input("Do you value hard work, dedication, and perseverance?").lower()
if huf3=="yes":
  hufflepuff = hufflepuff + 1  
  
huf4 = input("Are you a good listener and friend?").lower()
if huf4=="yes":
  hufflepuff = hufflepuff + 1  

#slytherin
 
sly = input("Are you a cunning person?").lower()
if sly=="yes":
  slytherin = slytherin + 1
 
sly2 = input("Do you value leadership and taking charge?").lower()
if sly2=="yes":
  slytherin = slytherin + 1 
 
sly3 = input("Do you believe in being self-sufficient and independent?").lower()
if sly3=="yes":
  slytherin = slytherin + 1 

sly4 = input("Are you not afraid to use your intelligence and skills to achieve your goals?").lower()
if sly4=="yes":
  slytherin = slytherin + 1 
#ravenclaw
  
rav = input("Have you got a creative/inventive mind?").lower()
if rav=="yes":
  ravenclaw = ravenclaw + 1
 
rav2 = input("Are you curious and always eager to learn new things?").lower()
if rav2=="yes":
  ravenclaw = ravenclaw + 1 

rav3 = input("Do you appreciate creativity and originality?").lower()
if rav3=="yes":
  ravenclaw = ravenclaw + 1

rav4 = input("Do you have a quick wit and a sharp mind?").lower()
if rav4=="yes":
  ravenclaw = ravenclaw + 1
  
print("Slytherin :"+str(slytherin) + "points")
print("Gryffindor :"+str(gryffindor) + "points")
print("Hufflepuff :"+str(hufflepuff) + "points")
print("Ravenclaw : "+str(ravenclaw) + "points")



#######
  
if gryffindor>=ravenclaw and gryffindor>=hufflepuff and gryffindor>=slytherin:
   print("You belong to Gryffindor!")
elif ravenclaw>=gryffindor and ravenclaw>=hufflepuff and ravenclaw>=slytherin:
   print("You belong to Ravenclaw!")
elif hufflepuff>=ravenclaw and hufflepuff>=gryffindor and hufflepuff>=slytherin:
   print("You belong to Hufflepuff!")
elif slytherin>=ravenclaw and slytherin>=hufflepuff and slytherin>=gryffindor:
   print("You belong to Slytherin!")