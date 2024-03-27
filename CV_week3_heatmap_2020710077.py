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

plt.figure(figsize = (10,7))
sns.heatmap(df_cm, annot=True)
plt.show()