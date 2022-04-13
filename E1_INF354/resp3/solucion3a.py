# 3. Del dataset anterior realice en PYTHON, tres algoritmos de preprocesamiento.
# 3.a) algoritmos de preprocesamiento missing_values
import numpy as np
from sklearn.impute import SimpleImputer
prepro = SimpleImputer(missing_values=np.nan, strategy="mean")
X1 = np.array([
  [np.nan,25.68,91.84,16.6,89.84,99.6,1.84,74.2,3]
,[91.64,25.104,91.552,15.88,89.552,98.88,1.552,np.nan,3]
,[60,20,96,10,95,85,7,60,1]
,[85.76,23.536,90.768,13.92,88.768,96.92,0.768,68.84,3]
,[48.12,17.248,97.872,6.496,96.248,72.48,8.248,53.12,0]
,[56.88,19.376,95.376,9.376,94.064,83.44,6.376,58.44,1]
,[47,16.8,97.2,5.6,95.8,68,7.8,52,0]
,[50,18,99,8,97,80,9,55,0]
,[45.28,16.112,96.168,4.224,95.112,61.12,7.112,50.28,np.nan]
])
X2 = prepro.fit_transform(X1)
print(X2)
# np.nan
# =============================================================================
# [[60.585 25.68  91.84  16.6   89.84  99.6    1.84  74.2    3.   ]
#  [91.64  25.104 91.552 15.88  89.552 98.88   1.552 58.985  3.   ]
#  [60.    20.    96.    10.    95.    85.     7.    60.     1.   ]
#  [85.76  23.536 90.768 13.92  88.768 96.92   0.768 68.84   3.   ]
#  [48.12  17.248 97.872  6.496 96.248 72.48   8.248 53.12   0.   ]
#  [56.88  19.376 95.376  9.376 94.064 83.44   6.376 58.44   1.   ]
#  [47.    16.8   97.2    5.6   95.8   68.     7.8   52.     0.   ]
#  [50.    18.    99.     8.    97.    80.     9.    55.     0.   ]
#  [45.28  16.112 96.168  4.224 95.112 61.12   7.112 50.28   1.375]]
# =============================================================================