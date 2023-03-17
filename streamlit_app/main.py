from utils import * 
from constants import *

def main():
    getAndSaveDatasetFromURL(url='https://www.gutenberg.org/files/103/103-0.txt', filename=WORD_CORPUS_FILENAME)
    
    data = preprocessDataFromFile(WORD_CORPUS_FILENAME)
    locs, err_count = getLatAndLong(data)
    
    dataframe = pd.DataFrame(locs, columns=["Place", "Lat", "Long"])
    errorDataframe = pd.DataFrame(err_count["places"], columns=["Error_Places"])
    dataframe = sortedDataFrame(dataframe)

    saveDataFrame(df=dataframe, filename= LOCATION_DATASET)
    saveDataFrame(df=errorDataframe, filename=ERROR_DATA)

if __name__ == "__main__":
    main()