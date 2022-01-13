import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


# plt.rcParams['font.sans-serif'] = 'simhei'
# plt.rcParams['axes.unicode_minus'] = False

# data = pd.read_csv("11.csv")
# data = np.array(data)
# print(data)

# data是一个多维数组，所以可以用data[:,1]这种分片操作取某一列的值
# plt.pie(data[:, 1], labels=data[:, 0], autopct="%.1ff%%")
# plt.legend(data[:, 0], loc="upper left")
# plt.show()

# plt.plot(data[:, 0], data[:, 2], '-*')
# plt.xlabel("均价")
# plt.show()


# sns.set_theme(); np.random.seed(0)
# # x = np.random.randn(100)
# ax = sns.displot(data)
# plt.show()


# data = pd.read_csv("11.csv")
# data = np.array(data)
# print(data)
# data = pd.DataFrame(data[:1])
# res = sn.distplot(data)
# data = np.random.randn(100)
# res = sn.distplot(data)

data_set = pd.read_csv("11.csv")
# print(data_set)
# data_set = np.array(data_set)
data = pd.DataFrame(data_set["money"])
print(data)
res = sn.distplot(data)
plt.show()
