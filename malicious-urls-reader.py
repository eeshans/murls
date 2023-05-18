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

    #check for https
    if ("https" in url):
        urlscore += 2

    #check for http
    if ("http" in url):
        urlscore += 2

    #checks for .com, .org, 

    #checks for .html
    if ("html" in url):
        urlscore -= 2
    print(urlscore)

# main function
def main():
    data = fileread()
    
    for i, row in data:
        if ((i % 2 == 0) and (i < 52)) :
            scoreurl(row)
            print(row)
            i += 1
        else:
            print(row)
            i += 1
       
    # printing entries 1-20
    # print(data.head(21))
    
    # sorting dataframe
    # data.sort_values("type", axis=0, ascending=False, inplace=True)
    
if __name__ == "__main__":
    main()