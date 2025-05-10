# 小袁口算 - 手写数字识别口算练习系统

## 项目概述

小袁口算是一个基于PyQt5开发的交互式口算练习应用，集成了手写数字识别功能。该应用提供加减法算术题，用户通过手写方式输入答案，系统利用神经网络模型自动识别并判断答案的正确性。

## 功能特点

- 自动生成10以内的两位数加减法题目
- 双画板界面，分别用于输入十位和个位数字
- 基于深度学习的手写数字识别
- 计时功能，记录用户完成10道题目的总时间
- 实时反馈答题正确与否
- 最终显示得分和用时

## 文件结构

- huatu.py: 实现画板功能，包含画图控件和双画板控件
- kousuan.py: 主程序，实现口算练习的界面和逻辑
- shibie.py: 数字识别模块，加载训练好的模型并识别手写数字
- shuzishibie.py: 定义数字识别的网络结构
- model_Mnist.pth: 预训练的手写数字识别模型
- mnist: MNIST数据集，用于训练手写数字识别模型

## 如何使用

1. 启动应用：
   ```bash
   python kousuan.py
   ```

2. 点击"开始"按钮进入口算练习界面

3. 系统会随机生成算术题，用户在左右两个画板上分别手写答案的十位和个位数字

4. 点击"提交"按钮提交答案，系统会自动识别并判断正确性

5. 完成10道题目后，系统会显示总分和用时

## 技术细节

- 使用PyQt5构建用户界面
- 基于PyTorch实现手写数字识别模型
- 使用MNIST数据集训练模型
- 利用图像处理技术对手写输入进行预处理和识别

## 开发环境

- Python 3.x
- PyQt5
- PyTorch
- torchvision
- PIL (Pillow)


## 安装依赖

```bash
pip install -r requirements.txt
```

## 贡献指南

欢迎对项目进行改进和优化，可以通过以下方式贡献：
1. Fork 该仓库
2. 创建新的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件
