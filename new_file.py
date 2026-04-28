import pickle

with open("person.pkl", "rb") as file:
    new_person = pickle.load(file)


new_person.info()
