# read write file

def writeToFile(fileName, text):
    with open(fileName, 'w') as file:
        file.write(text)

def appendToFile(fileName, text):
    with open(fileName, 'a') as file:
        file.write(text)

def readFromFile(fileName):
    with open(fileName, 'r') as file:
        content = file.read()
        
        return content
        
writeToFile('greet.txt', 'Hello!\n') 
appendToFile('greet.txt', 'Goodbye!\n') 
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n' 