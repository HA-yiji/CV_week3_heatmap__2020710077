import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

array = [[976,0,0,0,6,18,0],
         [0,997,0,0,3,0,0],
         [1,0,982,0,0,6,11],
         [1,2,2,995,0,0,0],
         [14,0,0,0,975,11,0],
         [17,0,0,0,5,978,0],
         [0,0,3,0,0,0,997]]
labels = ["angry", "disgusted", "fearful", "happy", "neutral", "sad", "surprised"]

df_cm = pd.DataFrame(array, index=labels, columns=labels)

#plt.figure(figsize = (10,10))
fig, ax = plt.subplots(figsize=(15,10))
sns.heatmap(df_cm, linewidths=1, annot=True, ax=ax, fmt='d',cmap='Blues')
# sns.set(font_scale=1.4)

plt.show()