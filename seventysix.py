# Python program to demonstrate pickling

import pickle

#serialization
# data_to_pickle={
#     'name': 'John Doe',
#     'age': 30,
#     'email': 'john.doe@example.com'
# }

# with open('data.pickle','wb') as file:
#     pickle.dump(data_to_pickle,file)

# deserialization

with open('data.pickle','rb') as file:
    unpickled_data=pickle.load(file)
print(unpickled_data)