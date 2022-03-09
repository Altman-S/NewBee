

import pickle
import re, collections
def words(text): return re.findall('[a-z]+', text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


NWORDS = train(words(open('text.txt').read()))

NWORDS=dict(NWORDS)
with open('NWORDS.pkl', 'wb') as handle:
    pickle.dump(NWORDS, handle, protocol=pickle.HIGHEST_PROTOCOL)
