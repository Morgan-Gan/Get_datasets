import numpy as np
import torch
from torchvision.datasets import MNIST # 导入 pytorch 内置的 mnist 数据
from torch.utils.data import DataLoader
from torch import nn

import time
import matplotlib.pyplot as plt
# %matplotlib inline


def data_tf(x):
    x = np.array(x, dtype='float32') / 255 # 将数据变到 0 ~ 1 之间
    x = (x - 0.5) / 0.5 # 标准化，这个技巧之后会讲到
    x = x.reshape((-1,)) # 拉平
    x = torch.from_numpy(x)
    return x

train_set = MNIST('images/mnist', train=True, download=True, transform=data_tf) # 载入数据集，申明定义的数据变换
test_set = MNIST('images/mnist', train=False, download=True, transform=data_tf)

# 定义 loss 函数
criterion = nn.CrossEntropyLoss()

def sgd_update(parameters, lr):
    for param in parameters:
        param.data = param.data - lr * param.grad.data

# batch size设为1
train_data = DataLoader(train_set, batch_size=64, shuffle=True)
# 使用 Sequential 定义 3 层神经网络
net = nn.Sequential(
    nn.Linear(784, 200),
    nn.ReLU(),
    nn.Linear(200, 10),
)

# 开始训练
losses1 = []
idx = 0

start = time.time() # 记时开始
for e in range(10):
    train_loss = 0
    for im, label in train_data:
        
        # 前向传播
        out = net(im)
        loss = criterion(out, label)
        
        # 反向传播
        net.zero_grad()         # 上一次计算梯度清零
        loss.backward()

        # 更新梯度
        lr = 1e-1 if e < 5 else 1e-2
        sgd_update(net.parameters(), lr) # 使用 0.01 的学习率
        # 记录误差
        train_loss += loss.item()
        if idx % 30 == 0:
            losses1.append(loss.item())
        idx += 1
    print('epoch: {}, Train Loss: {:.6f}'
          .format(e, train_loss / len(train_data)))
end = time.time() # 计时结束
print('使用时间: {:.5f} s'.format(end - start))


# x_axis = np.linspace(0, 5, len(losses1), endpoint=True)
# plt.semilogy(x_axis, losses1, label='batch_size=1')
# plt.legend(loc='best')
