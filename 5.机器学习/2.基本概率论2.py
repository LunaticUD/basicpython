# 经典Broken Rod示例
# !蒙特卡洛经典应用
# *三角形存在：a+b>c,a+c>b,b+c>a,y>x/x>y
import numpy as np

x,y = np.random.rand(2,1000000)
a,b,c = x,y-x,1-y
s = (a+b+c)/2
print(np.mean((s>a)&(s>b)&(s>c)&(y>x)))
# approx 1/8=0.125
# 又因对称性 1/8+1/8=0.25
# 经典勾股定理
# !随机变量到条件概率的映射
# !条件期望是随机变量的投影算子
# *<X-h_opt(y),X-h_opt(y)> = <X,X> - <h_opt(y),h_opt(y)>
# *E(X-E(X|Y))^2 = E(X)^2 - E(E(X|Y))^2
from sympy.abc import y,x
from sympy import integrate,simplify
fxy = x + y 
fy = integrate(fxy,(x,0,1))
fx = integrate(fxy,(y,0,1))
EXY = (3*y+2)/(6*y+3)
LHS = integrate((x-EXY)**2*fxy,(x,0,1),(y,0,1))
print(LHS)
RHS = integrate((x)**2*fx,(x,0,1))-integrate((EXY)**2*fy,(y,0,1))
print(RHS)
print(simplify(LHS-RHS)==0)
# 最小化目标函数
# !基于A做B的最优估计，这个最优估计就是条件期望E(B|A)
import sympy as S
from sympy.stats import density, E, Die
x = Die('D1',6)
y = Die('D2',6)
print(x,y)
a = S.symbols('a')
z = x + y
J = E((x-a*(x+y))**2)
print(S.simplify(J))
sol,= S.solve(S.diff(J,a),a)
print(sol)
# a 就是1/2
# E(X|Z)=z/2
# 验证
# !若Z=7,为什么不用离7最近的6？
import numpy as np
from sympy import stats
sample_z7 = lambda:stats.sample(x,S.Eq(z,7))
mn = np.mean([(6-sample_z7())**2 for i in range(100)])
mn1 = np.mean([(7/2.-sample_z7())**2 for i in range(100)])
print(f'MSE={mn:.2f} using 6 vs MSE={mn1:.2f} using 7/2')
# MSE=9.02 using 6 vs MSE=2.73 using 7/2 由此可知条件期望是最优的估计器
# 如果🎲的有一个不公平呢
x = stats.FiniteRV('D3',{
    1:1/15,2:1/15,3:1/15,
    4:1/15,5:1/15,6:2/3
})
print(f'条件期望：{E(x,S.Eq(z,7))=}')
sample_z7 = lambda:stats.sample(x,S.Eq(z,7))
MSE_6 = np.mean([(6-sample_z7())**2 for i in range(1000)])
MSE_5 = np.mean([(5-sample_z7())**2 for i in range(1000)])
print(f'{MSE_6=:.2f} vs {MSE_5=:.2f}')
# !条件期望的最优性是普适的，并不依赖于分布是否公平


