# 🧠 Desktop Hacker | 桌面加密与恢复系统

> ⚠️ 本程序具有较强的系统操作权限，请 **谨慎使用**，作者不对误操作造成的数据丢失负责。
>  
> ⚠️ This program can **alter or remove files on your desktop**. Use it **at your own risk**.

---

## 🚀 项目简介 | Project Introduction

`Desktop Hacker` 是一个纯 Python 编写、**无需额外依赖库**的桌面加密与解密程序。它可以在 Windows 和 macOS/Linux 系统中运行，通过对文件名进行哈希处理，达到**不可读加密**效果，并且可以通过唯一的恢复文件完整复原。

`Desktop Hacker` is a **no-dependency Python utility** that encrypts and recovers desktop files by renaming them using SHA256 hashes. It's cross-platform and supports both **debug mode** and **real system-level operation**.

---

## 🔐 功能特性 | Features

- ✅ **加密模式**：将桌面上的所有文件（包括子目录）重命名为哈希值，并删除原始路径结构。
- 🔄 **解密模式**：基于加密时生成的 `.recovery` 文件，完全复原文件路径和文件名。
- 🛡️ **调试保险机制**（SAFE）：在 `ON` 模式下仅操作 `Fake Desktop` 文件夹，确保安全测试。
- 🧠 **恢复容错机制**：如果恢复失败，会在桌面上生成 `Recovery Hint.txt`，提示用户手动处理。

---

## 🖥️ 使用说明 | Usage

### 🧪 调试模式 Debug Mode

在调试期间，程序只会加密/解密桌面上的 `Fake Desktop` 文件夹内容：

```python
SAFE = "ON"  # 保险模式（只操作 Fake Desktop）
RECOVERY = False  # False = 加密模式，True = 解密模式
````

将 `RECOVERY` 设置为 `True` 进入解密模式。

### ⚠️ 真正加密桌面 Real Desktop Encryption

```python
SAFE = "OFF"
RECOVERY = False
```

这将**真实加密整个桌面内容**，请谨慎操作！

---

## 📂 文件结构 | File Structure

| 类型   | 说明                | 标识方式                |
| ---- | ----------------- | ------------------- |
| 文件   | 被移动至桌面主目录，命名为其哈希值 | `F<加密名>*<原路径>?`     |
| 文件夹  | 记录其路径结构以便恢复       | `D<原路径>?`           |
| 恢复文件 | 存储所有路径映射信息        | 哈希命名文件 |

---

## ⚙️ 技术细节 | Technical Notes

* 使用 `hashlib.sha256` 保证文件命名的不可逆加密性
* 使用 `shutil` 完成文件的移动与删除
* 不依赖第三方库，确保兼容性与可移植性
* 所有加密操作均基于路径和文件名，**文件内容不被修改**

---

## 🧠 作者说明 | Author Note

这个项目仅用于编程学习与加密逻辑实验，请不要用于恶意用途。
如误操作导致文件丢失，作者概不负责。

This program is for educational purposes **only**. Please do **not** use it for any malicious intent. The author is **not responsible** for any data loss caused by misuse.

---

## 📎 项目地址 | Project Link

👉 GitHub: [https://github.com/LeoWang0814/Desktop-Hacker](https://github.com/LeoWang0814/Desktop-Hacker)

欢迎 Star、Fork 或提出 Issues！

---

## 📝 License

This project is released under the **MIT License**.

```
