from random import randint #built in function randint from random library
calc = {
  "Area under a curve":"Integral",
  "Slope of a curve":"Derivative",
  "Approximate area using rectangles":"Riemann Sum"
}

chem = {
  "Model for covalent molecule":"Lewis structure",
  "Author of the plate tectonic theory":"Alfred Wegener",
  "How much an element loves electrons":"Electronegativity",
  "Disorder of particles":"Entropy",
  "Average kinetic energy of particles":"Temperature",
  "The force of the nucleus pulling on electrons":"Nuclear Charge"
}

whistory = {
  "Author of Art of War":"Sunzi",
  "Where the Tokugawa Shogunate was located":"Japan",
  "Ruler, last 50 years of the Qing Dynasty":"Cixi",
  "Leader of the Haitian Revolution":"Toussaint L'Overture",
  "First proponent of capitalism":"Adam Smith",
  "First country to industrialize":"Great Britain",
  "Europe's social structure during the middle ages":"Feudal"
}

print("Flashcards") #built-in print function
print("Answer correctly to earn points, type 'change' to change the subject") #instructions
points = 0 #accumulated points

#function refers input to a dictionary
def convert(topic):
  while True:
    if topic.lower() == "calculus": #built-in method .lower() for case insensitivity
      return calc
    elif topic.lower() == "history":
      return whistory
    elif topic.lower() == "chemistry":
      return chem
    else:
      print("Sorry, this is not an option.") #does not allow other subjects
      topic = input("Choose another subject: ")
      continue #goes onto next iteration

#chooses question, adds up points
def counter(subject):
  again = "Yes" #allows users to choose when to stop
  global points #points will not reset with each call of function
  while again.lower() == "yes": #allows user to decide when to stop
    term = randint(0,len(subject)-1) #chooses random index using randint function
    definitions = list(subject) #built in function to store all definitions in list
    print(definitions[term]) #refers index to proper flashcard
    answer = input("Answer: ") #prompts user to answer
    if answer.lower() == subject[definitions[term]].lower(): #matches answer to flashcard
      points += 1
      print("Correct!")
    else:
      print("Incorrect")
      print("Points: " + str(points)) #display points with built in string function
      again = input("Try again? ")
  while again.lower() == "change":
    subject = input("Pick a different topic: ")
    counter(convert(subject)) #first call of convert
    break

def add(subject): #add flashcards
  q = input("Definition: ")
  a = input("Term: ")
  subject[q] = a #maps the definition to the term in the dictionary

subject = convert(input("Which topic? Chemistry, calculus, or history? ")) #second call
more = input("Do you want to add more questions? ")
while more.lower() == "yes":
  add(subject)
  more = input("Add another? ")
counter(subject)
