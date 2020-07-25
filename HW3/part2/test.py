import pandas as pd
centroids = {}
d = {'col1': [1, 2], 'col2': [3, 4]}
data  = pd.DataFrame(data=d)
data =data.sample(frac=1).reset_index(drop=True)
for i in range(10):
    centroids[i] = data[i]

def jaccard(a, b):
    """
        Jaccard_Dist = 1 - |(A M B)|/|(A U B)|
    """
    common = list(set(a) & set(b))
    union = list(set(a) | set(b))
    return 1 - (len(common)/len(union))

text = "asdg,garwgjk"
"""distances = [jaccard(text,centroids[cent]) for cent in centroids]"""


print("centroids is ",centroids)
for cent in centroids:
    print("cent is",cent)

