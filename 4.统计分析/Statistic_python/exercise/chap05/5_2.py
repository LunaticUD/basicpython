import pandas as pd
from scipy.stats import binom

print("P(X=2)=",binom.pmf(2,4,0.1))
print("P(X<=2)=",round(binom.pmf(2,4,0.1)+binom.pmf(1,4,0.1)+binom.pmf(0,4,0.1),6))
