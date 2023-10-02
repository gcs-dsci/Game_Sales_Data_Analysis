#Import all the required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from loader import GameSalesLoader
from datamanager import DataManager


def main():
    # cool stuff happening here
    # Initializing classes

    # Load Dataset
    print("Loading toy dataset (and turning class into nominal one)")
    df = GameSalesLoader().load_data()
    main = GameSalesLoader().main_data()
    dataman = DataManager(df, main)
    # Testing data manager
    print(dataman.feature_list())
    print("Sample of 5 random games:")
    print(dataman.show_sample(5))
    print("Title of 5 random games:")
    print(dataman.show_titles(5))
    print("A common title for different platforms:")
    print(dataman.show_same_title('Grand Theft Auto V'))
    print("Statistics of sales per region:")
    print(dataman.describe_some_data(['NA_Sales', 'EU_Sales', 'JP_Sales','Other_Sales']))
    print("Top videogame platforms:")
    print(dataman.show_counter('Platform'))
    print("Top game per genres:")
    print(dataman.show_counter('Genre'))
    print("Top games per ratings:")
    print(dataman.show_counter('Rating'))
    print("Top game developers:")
    print(dataman.show_counter('Developer'))
    print("Top games per different platforms:")
    print(dataman.same_titles_counter())
    dataman.plot_counts('Platform', "Count of Video Games by Platform")
    #print(df.head())

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    #try:
        # start JVM with Weka package support
        #jvm.start(packages=True, max_heap_size="2048m")
    main()
    #except Exception as e:
        #print(traceback.format_exc())
    #finally:
        #jvm.stop()
