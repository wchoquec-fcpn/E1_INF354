import pandas as pd
import numpy as np

estres = pd.read_csv("SaYoPillow.csv", sep=",")

print(estres.head())

# sr1,rr,t,lm, bo,rem,sr2,hr,clase
print("sr1--> Q1",np.quantile(estres["sr1"], .25),"Percentil50=",np.percentile(estres["sr1"], 50))
print("rr-->  Q1",np.quantile(estres["rr"], .25),"Percentil50=",np.percentile(estres["rr"], 50))
print("t-->   Q1",np.quantile(estres["t"], .25),"Percentil50=",np.percentile(estres["t"], 50))

print("lm-->   Q1",np.quantile(estres["lm"], .25),"Percentil50=",np.percentile(estres["lm"], 50))
print("bo-->   Q1",np.quantile(estres["bo"], .25),"Percentil50=",np.percentile(estres["bo"], 50))
print("rem-->  Q1",np.quantile(estres["rem"], .25),"Percentil50=",np.percentile(estres["rem"], 50))

print("sr2-->  Q1",np.quantile(estres["sr2"], .25),"Percentil50=",np.percentile(estres["sr2"], 50))
print("hr-->   Q1",np.quantile(estres["hr"], .25),"Percentil50=",np.percentile(estres["hr"], 50))
print("clase-- Q1",np.quantile(estres["clase"], .25),"Percentil50=",np.percentile(estres["clase"], 50))

# =============================================================================
#      sr1      rr       t      lm      bo    rem    sr2     hr  clase
# 0  93.80  25.680  91.840  16.600  89.840  99.60  1.840  74.20      3
# 1  91.64  25.104  91.552  15.880  89.552  98.88  1.552  72.76      3
# 2  60.00  20.000  96.000  10.000  95.000  85.00  7.000  60.00      1
# 3  85.76  23.536  90.768  13.920  88.768  96.92  0.768  68.84      3
# 4  48.12  17.248  97.872   6.496  96.248  72.48  8.248  53.12      0
# sr1--> Q1 52.5 Percentil50= 70.0
# rr-->  Q1 18.5 Percentil50= 21.0
# t-->   Q1 90.5 Percentil50= 93.0
# lm-->   Q1 8.5 Percentil50= 11.0
# bo-->   Q1 88.5 Percentil50= 91.0
# rem-->  Q1 81.25 Percentil50= 90.0
# sr2-->  Q1 0.5 Percentil50= 3.5
# hr-->   Q1 56.25 Percentil50= 62.5
# clase-- Q1 1.0 Percentil50= 2.0
# =============================================================================
