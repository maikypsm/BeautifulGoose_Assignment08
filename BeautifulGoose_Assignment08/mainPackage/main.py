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
    """
    This tests the functionality of the Headphones and Music classes."
    """

    print("Headphones class test logic:")
    speakers = Headphones("Bose Quiet Comfort 45") # Instantiation of a Headphones object
    testSong = Music("Marcos Valle", "Estrelar") # Instantiation of a Music object for testing
    songInfo = testSong.__str__()

    print ("\n-----TESTING: Non Dunder methods-----") # TEST with NON DUNDER

    print("Type attribute of Headphones object:", speakers.get_model())
    speakers.set_model("Sony 1000XM5")
    print("CHANGE: New type attribute of Headphones object:", speakers.get_model())
    print("TEST: Class method playedMusic with Music object")
    speakers.playedMusic(songInfo)
    
    print ("\n-----TESTING: Dunder methods-----") # TEST with DUNDER methods

    print("TEST: __repr__ method:")
    print("From __repr__():", speakers.__repr__())
    speakersCopy = eval(speakers.__repr__())
    print("Copied Headphones:", speakersCopy.__str__())

    print("Original Headphones object:", speakers.get_model())
    print("Copied Headphones object:", speakersCopy.get_model())
    print("\nTEST: __str__ method:")
    print("__str__() of current Headphones object: ", speakers.__str__())

    print ("\n*********************************")

    # Music Object Functionality Testing

    print("Music class test logic:")
    exampleSong = Music("Van Halen", "Jump") # Instatiation of a Music object

    print ("\n-----TESTING: Non Dunder methods-----") # TEST with NON DUNDER

    print("Attributes of Music object:", exampleSong.get_Music())
    print("Name of song in Music object:", exampleSong.get_name())
    print("Name of artist in Music object:", exampleSong.get_artist())
    print("CHANGE: Artist of Music object: Lady Gaga")
    exampleSong.set_artist("Lady Gaga")
    print("New attributes of Music object", exampleSong.get_artist(), exampleSong.get_name())
    print("CHANGE: Song Name of Music object: Bad Romance")
    exampleSong.set_name("Bad Romance")
    print("New attributes of Music object", exampleSong.get_artist(), exampleSong.get_name())
    print("New type attribute of Music object:", exampleSong.get_Music())
    print("TEST: Music class method")
    exampleSong.jamOut()
    
    print ("\n-----TESTING: Dunder methods-----") # TEST with DUNDER methods

    print("TEST: __repr__ method:")
    print("From __repr__():", exampleSong.__repr__())
    exampleSongCopy = eval(exampleSong.__repr__())
    print("Copied Music:", exampleSongCopy.__str__())

    print("Original Music object:", exampleSong.get_Music())
    print("Copied Music object:", exampleSongCopy.get_Music())
    print("\nTEST: __str__ method:")
    print("__str__() of current Music object: ", exampleSong.__str__())

    # Let's get silly - Test against a list

    """
    myArtists = ["Journey", "Migos", "Amerie"]
    mySongNames = ["Don't Stop Believin'", "Stir Fry", "1 Thing"]
    myPlaylist = []
    for x in range():
        newSong = Music(myArtists[x], mySongNames[x])
        myPlaylist.append(newSong)
    """
