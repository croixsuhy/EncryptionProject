import pickle

# dictionary we will be using to pickle
dictExample = b"Hello"

# pickles dictionary and puts pickled data in text file
with open("pickledData.txt", "wb") as file:
    pickle.dump(dictExample, file)

# unpickle data and print
with open("pickledData.txt", "rb") as file:
    print(pickle.load(file))
