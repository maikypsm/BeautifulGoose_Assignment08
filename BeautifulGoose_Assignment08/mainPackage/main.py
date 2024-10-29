# main.py

# Name: Sarah Mahan, Joshua Klingelhafer, Lucas Ransick
# email:  mahansa@mail.uc.edu, klingejh@mail.uc.edu, ransiclg@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Creating two class objects and testing their methods.

# Brief Description of what this module does: This is the main module's main function. This executes and tests objects from the classes
# Music and Headphones.
# Citations:
# Anything else that's relevant:

from HeadphonesPackage.headphones import *
from MusicPackage.music import *

if __name__ == "__main__":
    print("This tests the functionality of the Headphones and Music classes.") 


    print("Headphones class test logic...")
    speakers = Headphones("Bose Quiet Comfort 45") # Instantiation of a Headphones object

    print("Type attribute of Headphones object:", speakers.get_model())
    print("Changing the type of the object...")
    speakers.set_model("Sony 1000XM5")
    print("Type attribute of Headphones object:", speakers.get_model())

    print("\n\nTesting the repr method...")

    print("From __repr__():", speakers.__repr__())
    speakersCopy = eval(speakers.__repr__())
    print("Copied car:", speakersCopy.__str__())

    print("Type attribute of original Headphones object:", speakers.get_model())
    print("Type attribute of copied Headphones object:", speakersCopy.get_model())

    # Music Object

    print("Music class test logic...")
    vanhalenSong = Music("Rock", "Van Halen", "Jump") # Instatiation of a Music object

    print("Type attribute of Headphones object:", speakers.get_model())
    print("Changing the type of the object...")
    speakers.set_model("Sony 1000XM5")
    print("Type attribute of Headphones object:", speakers.get_model())

    print("\n\nTesting the repr method...")

    print("From __repr__():", speakers.__repr__())
    speakersCopy = eval(speakers.__repr__())
    print("Copied car:", speakersCopy.__str__())

    print("Type attribute of original Headphones object:", speakers.get_model())
    print("Type attribute of copied Headphones object:", speakersCopy.get_model())

    # Let's get silly
    # Computer resources are finite

    #myVehicle = []
    #while(True):
        # Add a new Vehicle object to the list
        #newVehicle = Vehicle("Some Vehicle")
        # myVehicle.append(newVehicle)
