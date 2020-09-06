# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rjrbnB2nJFI18v1mo6KER_-_tPaUqiFd
"""

# Commented out IPython magic to ensure Python compatibility.
#18BCE0954
#nurse star ratings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline
data=pd.read_csv("https://data.medicare.gov/resource/ax9d-vq6k.csv")
plt.figure(figsize=(8,8)) 
data.hist()
print("Histogram Plot")
plt.show()



#18BCE0954
#nurse star ratings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = pd.DataFrame(data)
fig = plt.figure(figsize = (15,10))
ax = fig.gca()
dataset.hist(ax=ax)
plt.show()

#18BCE0954
#Physician data compare
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
n_data=pd.read_csv("https://data.medicare.gov/resource/2bhu-tmkt.csv")
df = pd.DataFrame(n_data) 
fig = plt.figure(figsize =(40, 10)) 

# Horizontal Bar Plot 
plt.bar(x=n_data['specialty'].head(50),height=df['service_count'].head(50))
  
# Show Plot 
plt.show()

#18BCE0954
#Physician data compare
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
n_data=pd.read_csv("https://data.medicare.gov/resource/2bhu-tmkt.csv")
fig = plt.figure(figsize =(30, 6)) 
plt.scatter(n_data['specialty'].head(30),n_data['service_count'].head(30))
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x_data=pd.read_csv("https://data.medicare.gov/resource/rs6n-9qwg.csv")
fig = plt.figure(figsize =(30, 6)) 
plt.scatter(x_data['state'].head(100), x_data['score'].head(100))
plt.show()

#18BCE0954
#Medicare Spending Per Beneficiary – State
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
n_data=pd.read_csv("https://data.medicare.gov/resource/2bhu-tmkt.csv")
df=pd.DataFrame(n_data.head(30))
df.boxplot(by ='specialty', column =['service_count'], grid = False,figsize =(30, 9))

#18BCE0954
#Medicare Spending Per Beneficiary – State
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

x_data=pd.read_csv("https://data.medicare.gov/resource/rs6n-9qwg.csv")
fig = plt.figure(figsize =(30, 6))
# plotting the points  
plt.plot(x_data['state'].head(10), x_data['score'].head(10)) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Medicare Spending Per Beneficiary – State') 
plt.show()

#18BCE0954
#Physician data compare
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
x_data=pd.read_csv("https://data.medicare.gov/resource/rrqw-56er.csv")
fig = plt.figure(figsize =(20, 10))
sns.heatmap(n_data.corr())

new_data = n_data.pivot_table(index='state', columns='city', values='score')