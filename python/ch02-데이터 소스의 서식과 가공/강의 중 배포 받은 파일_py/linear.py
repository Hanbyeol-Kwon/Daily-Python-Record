import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

x = [-3,  31,  -11,  4,  0,  22, -2, -5, -25, -14]
y = [ -2,   32,   -10,   5,  1,   23,  -1,  -4, -24,  -13]
print(x)
print(y)

plt.plot(x, y)
plt.show()

df = pd.DataFrame({'X':x, 'Y':y})
print(df.shape) # (10, 2) : 10행 2열
print(df) # DataFrame 전체 출력
print(df.head()) # DataFrame 앞에서 5개 행 출력
print(df.tail()) # DataFrame 뒤에서 5개 행 출력

x_train = df.loc[:, ['X']]
y_train = df.loc[:, ['Y']]
print(x_train.shape, y_train.shape)

lr = LinearRegression()
lr.fit(x_train, y_train)

lr.coef_, lr.intercept_

print ("기울기: ", lr.coef_[0][0])
print ("y절편: ", lr.intercept_[0])










