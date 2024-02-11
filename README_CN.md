## 语言
[English](./README.md) | [中文](./README_CN.md)

## 项目简介
本项目为Python实现的多方安全计算实践，模拟了两位百万富翁（A与B）在不泄露自身确切财富值的前提下比较谁更富有的问题。我们利用SMPC（Secure Multi-party Computation）技术确保数据隐私性。

## 文件结构
- utils.py：包含RSA加密相关的基础工具函数，如生成密钥对、加密和解密功能。
- utils_test.py：用于测试utils文件中RSA等工具函数的正常运行情况，确保加密和解密过程的正确无误。
- index.py：模拟百万富翁问题的核心代码，展示了如何通过设计的安全通信协议来解决这一问题，使双方能在加密状态下进行有效比较。

## 运行指南
先运行utils_test.py以验证加密工具的正确性。
接着运行index.py查看模拟的实际流程及最终结果。