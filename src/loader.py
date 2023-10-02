import pandas as pd
import numpy as np

class Loader:
    """ Abstract class.
    """
    def __init__(self, name):
        self.__name = name
        self.__filename = filename

    def get_name(self):
        return self.__name

    def load_data(self):
        pass

    def main_data(self):
        pass

    def feature_extraction(self):
        pass

class AnimeLoader(Loader):
    """ We have an anime dataset here.
    """
    def __init__(self):
        self.__name = 'Anime Dataset'
        self.__filename = '../anime/Anime.csv'

    def get_name(self):
        return self.__name

    def load_data(self):
        """ Load and returns a dataset.
        """

        # Load data as a Pandas Dataframe
        return pd.read_csv(self.__filename)

 
    def main_data(self):
        """ Load and returns a dataset.
        """

        # Load data as a Pandas Dataframe
        return ['Name']

    def feature_extraction(self):
        """ Load and returns a dataset.
        """

        # Load data as a Pandas Dataframe
        return ['Tags']

class GameSalesLoader(Loader):
    """ We have an anime dataset here.
    """
    def __init__(self):
        self.__name = 'Video Games Sales Dataset'
        self.__filename = '../game/Video_Games_Sales_as_at_22_Dec_2016.csv'

    def get_name(self):
        return self.__name

    def load_data(self):
        """ Load and returns a dataset.
        """

        # Load data as a Pandas Dataframe
        return pd.read_csv(self.__filename)
        
    def main_data(self):
        """ Load and returns a dataset.
        """

        # Load data as a Pandas Dataframe
        return ['Name']

    def feature_extraction(self):
        """ Load and returns a dataset.
        """

        # Load data as a Pandas Dataframe
        return ['Name', 'Platform', 'Genre', 'Publisher']
