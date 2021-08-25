import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#baizeweiyu第二次修改

#plt.rcParams['font.sans-serif']=['SimHei'] # 解决中文乱码

labels = [200, 400, 600, 800]
e_0 = [25913, 44329, 53080, 64459]
e_50 = [37966, 38800, 45205, 68723]
e_100 = [32421, 28060, 33817, 37362]

x = np.arange(len(labels))  # 标签位置
width = 0.25  # 柱状图的宽度，可以根据自己的需求和审美来改

fig, ax = plt.subplots()

rects1 = ax.bar(x - width-0.02, e_0, width, label='0', color="#4472C4", hatch="XXXX", edgecolor="w")#蓝色
rects2 = ax.bar(x, e_50, width, label='50(wr)', color="#ED7D31", hatch='|||||', edgecolor="w")#橙色
rects3 = ax.bar(x + width+0.02, e_100, width, label='100(2*wr)', color="#A5A5A5", hatch='////', edgecolor="w")#灰色

plt.ylim(0, 80000)
#plt.xticks([200, 400, 600, 800])
#plt.xlim(100, 900)

# 为y轴、标题和x轴等添加一些文本。
ax.set_ylabel('Energy consumption (*$10^3$nJ)', fontsize=16)
ax.set_xlabel('Distance from Source to Sink (m)', fontsize=16)
#ax.set_title('这里是标题')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc="best", frameon=False)

"""
def autolabel(rects):
    在*rects*中的每个柱状条上方附加一个文本标签，显示其高度
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3点垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom')
"""
#autolabel(rects1)
#autolabel(rects2)
#autolabel(rects3)

fig.tight_layout()

plt.show()
