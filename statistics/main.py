import statistics as st
import fractions as fr
import decimal as de

# 平均数
print(st.mean([1,2,3,4,5,6,7,8,9]))
x=[(3,7),(1,21),(5,3),(1,3)]
y=[fr.Fraction(* item) for item in x]
print(st.mean(y))
x=('0.5','0.75','0.625','0.375')
y=map(de.Decimal,x)
print(st.mean(y))

# 中位数
print(st.median([1,3,5,7]))
print(st.median_low([1,3,5,7]))
print(st.median_high([1,3,5,7]))
print(st.median_grouped([1,3,5,7]))

# 众数
print(st.mode([1,3,3,7,5]))

# 总体标准差，方差
print(st.pstdev([1,3,5,7,9]))
print(st.pvariance([1,3,5,7,9]))

# 样本标准差，方差
print(st.stdev([1,2,5,4]))
print(st.variance([1,3,5,7,9]))