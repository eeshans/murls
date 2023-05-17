#imports
import pandas as pd



def readFile():
    pd.options.display.max_rows = 50
    data = pd.read_csv('../malicious_phish.csv')
    print(data)

#main function
def main():
    data = readFile()
    print(data)

if __name__ == "__main__":

    main()