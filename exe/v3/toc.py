import nltk
from math import floor
from itertools import repeat

qtPlaceHolderList = ['<q0>', '<q1>']

def cocanbise(inputStr: str):
    # splits into words
    words = inputStr.split(' ')
    
    # removes punctuation
    
    # counts letters in each word
    wcList = []
    
    for word in words:
        if not word.startswith('<') and not word.endswith('>'):
            wcList.append(len(word))
        
    # converts last letters into strings
    for i in wcList:
        t = repeat("å", floor(i))
        u = chr((i % 26) + 96)
        oList = [t, u]
        i = str(oList)
        
    # moves last letters
    llList = []
    for word in words:
        if not word.startswith('<') and not word.endswith('>'):
            wList = list(word)
            llList.append(wList[-1])
            del wList[-1]
            word = str(wList)
        
    # combines suffix into single string
    suffixList = []
    
    for i in range(len(llList)):
        suffixList.append(wcList[i])
        suffixList.append(llList[i])
        
    suffix = str(suffixList)

def main(inputStr: str, qtIndex: int):
    # separates quotes
    strList = inputStr.split('"')
    qtList = []
    for i in range(len(strList)):
        if i % 2 == 1:
            qtList.append(strList[i])
            strList[i] = qtPlaceHolder[qtIndex]
            
    qtLess = str(strList)
            
    # separates sentences
    nltk.download('punkt')
    sentences = nltk.tokenize.sent_tokenize(qtLess)
    
    # magic
    for sentence in sentences:
        cocanbise(sentence)