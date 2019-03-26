import pickle, os

import pickle

a=set()
a.add("a")
a.add("b")
a.add("c")

# Store data (serialize)
with open('filename.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Load data (deserialize)
with open('filename.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

print(unserialized_data)