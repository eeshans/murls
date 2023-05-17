# imports
import pandas as pd


# reading file
def fileread():
    pd.options.display.max_rows = 50
    data = pd.read_csv('../malicious_phish.csv')
    return data

# scoring urls function
def scoreurl(url):
    urlscore = 5
    if ("https" in url):
        urlscore += 1


    print(urlscore)


# main function
def main():

    data = fileread()
    for row in data:
        scoreurl(row[1])
    
    # printing entries 1-20
    # print(data.head(21))
    
    # sorting dataframe
    # data.sort_values("type", axis=0, ascending=False, inplace=True)
    

if __name__ == "__main__":

    main()