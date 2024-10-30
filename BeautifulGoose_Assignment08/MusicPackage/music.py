# music.py

# Name: Sarah Mahan, Joshua Klingelhafer, Lucas Ransick
# email:  mahansa@mail.uc.edu, klingejh@mail.uc.edu, ransiclg@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Creating two class objects and testing their methods.

# Brief Description of what this module does: The module for the music class
# Citations:
# Anything else that's relevant:

class Music(object):
    """
    Model of different genres of music, artist, and song name
    """
    def __init__(self, artist, name): 
        """
        Constructor
        @param artist String: The artist of song being listened to.  
        @param name String: The name of the song being listened to.  
        """
        self.__artist = artist
        self.__name = name
    
    def get_Music(self):
        """
        @return string: the artist and name of the song
        """
        return f"{self.__name} {self.__artist}"

    def get_artist(self): 
        """
        @return String: The artist of the current object
        """
        return self.__artist

    def get_name(self): 
        """
        @return String: The name of the current object
        """
        return self.__name
    

    def set_artist(self, artist):
        """
        Assign a value to the artist of the current object
        @param model String: The artist to be assigned.
        """
        self.__artist = artist

    def set_name(self, name):
        """
        Assign a value to the name of the current object
        @param model String: The name to be assigned.
        """
        self.__name = name

    def jamOut(self):  
        """
        @param self String: 
        """
        print("\n♫♫ This song,", self.__name,", is so groovy! ♪♫", self.__artist, "made a great song! ♪♫")

    def __str__(self):
        """
        @return String: a string of the attributes of the current object
        """
        return f"{self.__name} by {self.__artist}"

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Music('{self.__artist}','{self.__name}')"    
