import pandas as pd
import numpy as np
import neattext.functions as nfx

# Estimators
from sklearn.linear_model import LogisticRegression

# Transformers
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

df = pd.read_csv("emotion-dataset.csv")
df['Emotion'].value_counts()

# User handles
df['Clean_Text'] = df['Text'].apply(nfx.remove_userhandles)

# Stopwords
df['Clean_Text'] = df['Clean_Text'].apply(nfx.remove_stopwords)

Xfeatures = df['Clean_Text']
ylabels = df['Emotion']

x_train,x_test,y_train,y_test = train_test_split(Xfeatures,ylabels,test_size=0.3,random_state=42)

pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])
pipe_lr.fit(x_train,y_train)
pipe_lr.score(x_test,y_test)

pipe_lr = Pipeline(steps=[('cv',CountVectorizer()),('lr',LogisticRegression())])
pipe_lr.fit(x_train,y_train)

Pipeline(steps=[('cv', CountVectorizer()), ('lr', LogisticRegression())])
pipe_lr.score(x_test,y_test)

sample1 = "This is a neutral statement"
print(pipe_lr.predict([sample1]))

# Begin analyzing

results = {}

df = pd.read_csv("test-dataset.csv")

correct = 0
incorrect = 0

for index, row in df.iterrows():
    actual = row[1]
    prediction = pipe_lr.predict([row[1]])
    if actual == prediction[0]:
        correct += 1
    else:
        incorrect += 1

print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")