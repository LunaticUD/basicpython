from scipy.stats import chi2,t,f

print("(1)")
print("df=15",round(t.cdf(-1.5,15),6))
print("df=20",round(1-t.cdf(2,20),6))
print("df=30",round(t.ppf(0.05,30),6))
print("(2)")
print("df=8",round(chi2.cdf(12,8),6))
print("df=20",round(1-chi2.cdf(18,20),6))
print("df=15",round(chi2.ppf(0.025,15),6))
print("(3)")
print("df=15,10",round(f.cdf(3.5,15,10),6))
print("df=12,8",round(1-f.cdf(3,12,8),6))
print("df=20,16",round(f.ppf(0.025,20,16),6))