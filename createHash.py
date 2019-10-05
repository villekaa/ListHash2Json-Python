import hashlib
import cutie
import json

#List of available hashing methods
available_methods = []
for var in hashlib.algorithms_guaranteed :
    available_methods.append(var)

def createHash(filePath, method):
    try:
        with open(filePath, encoding='utf-8') as f:
         result = []
         mylist = f.read().splitlines()
         for index, line in enumerate(mylist, start=0):
         
               encodedLine = line.encode('utf-8')
               hashedLine = getattr(hashlib, method)(encodedLine).hexdigest()
               result.append({"original" : line, "hash": hashedLine})
               print('Processig line: {} / line: {} / hash: {}'.format(index, line, hashedLine)) 
        return result
    except:
        print("Invalid File Path")

# File path input
filePath = input('Please enter file path: ')
# Select hash method
print('Select hash method.')

method = available_methods[
    cutie.select(available_methods, selected_index=0)]
print('You have selected method:', method)
#Pass the args and call the hash function
hashed = createHash(filePath, method)
   
try:
    with open('result.json', 'x') as json_file:
      json.dump(hashed, json_file)
except:
    print("Invalid path")