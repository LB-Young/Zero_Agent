import numpy as np
from typing import List, Tuple, Dict
import pandas as pd
import matplotlib.pyplot as plt

def detect_outliers(data: List[float], multiplier: float = 1.5) -> Dict:
    """
    使用IQR方法检测数组中的异常值
    
    参数:
        data: 输入的数值数组
        multiplier: IQR的乘数,用于确定异常值的阈值,默认为1.5
        
    返回:
        包含异常值分析结果的字典
    """
    # 转换为numpy数组便于计算
    arr = np.array(data)
    
    # 计算四分位数
    q1 = np.percentile(arr, 25)
    q3 = np.percentile(arr, 75)
    iqr = q3 - q1
    
    # 计算上下边界
    lower_bound = q1 - multiplier * iqr
    upper_bound = q3 + multiplier * iqr
    
    # 找出异常值
    outliers = arr[(arr < lower_bound) | (arr > upper_bound)]
    outliers_indices = np.where((arr < lower_bound) | (arr > upper_bound))[0]
    
    # 计算基本统计量
    stats = {
        "总样本数": len(data),
        "异常值数量": len(outliers),
        "异常值百分比": round(len(outliers) / len(data) * 100, 2),
        "异常值": outliers.tolist(),
        "异常值索引": outliers_indices.tolist(),
        "四分位数Q1": q1,
        "中位数": np.median(arr),
        "四分位数Q3": q3,
        "IQR": iqr,
        "下边界": lower_bound,
        "上边界": upper_bound,
        "最小值": np.min(arr),
        "最大值": np.max(arr)
    }
    
    def plot_boxplot(data: List[float]) -> None:
        """绘制箱线图来可视化异常值"""
        plt.figure(figsize=(10, 6))
        plt.boxplot(data)
        plt.title("数据分布箱线图")
        plt.ylabel("数值")
        plt.grid(True)
        plt.show()
    
    # 绘制箱线图
    plot_boxplot(data)
    
    return stats

# 使用示例
if __name__ == "__main__":
    sample_data = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 100, 0.1, 200]
    results = detect_outliers(sample_data)
    
    # 打印分析结果
    for key, value in results.items():
        print(f"{key}: {value}")