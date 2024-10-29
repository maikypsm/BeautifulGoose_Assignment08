class Music(object):
    """
    Model of different genres of music
    """
    def __init__(self, model): 
        """
        Constructor
        @param model String: The genre of music being listened too.   
        """
        self.__model = model
        
    def get_model(self): 
        """
        @return String: The model of the current object
        """
        return self.__model
    
    def set_model(self, model):
        """
        Assign a value to the model of the current object
        @param model String: The model to be assigned.
        """
        self.__model = model

    def musicType(song):  
        """
        @param song String: 
        """
        print("The genre of song that was played is " + song)
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        """
        return "model: " + self.__model

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"This song is ('{self.__model}')"
