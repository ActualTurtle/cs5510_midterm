import matplotlib.pyplot as plt
import pandas as pd

frame = pd.read_csv("data2.csv")
plt.plot(frame['angry0'], label="Angry")
plt.plot(frame['disgust0'], label="Disgust")
plt.plot(frame['fear0'], label="Fear")
plt.plot(frame['happy0'], label="Happy")
plt.plot(frame['neutral0'], label="Neutral")
plt.plot(frame['sad0'], label="Sad")
plt.plot(frame['surprise0'], label="Surprise")


plt.legend()
plt.xlabel('Frame')
plt.ylabel('Emotion')
plt.title('Title of the Plot')


plt.show()