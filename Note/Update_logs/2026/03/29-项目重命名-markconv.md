# 项目重命名 - 更新日志

**日期**: 2026-03-29  
**版本**: v0.1.0

---

## 变更内容

### 项目重命名
- 项目名称从 `mdconvert` 更改为 `markconv`
- 包名从 `mdconvert` 更改为 `markconv`
- PyPI 包名从 `mdconvert` 更改为 `markconv`

### 文件变更

#### 目录重命名
- `mdconvert/` → `markconv/`

#### 代码文件更新
- `setup.py` - 更新包名、项目 URL 和项目链接
- `examples/html_example/html_example.py` - 更新导入语句
- `README.md` - 更新所有项目引用和文档说明

#### 远程仓库更新
- GitHub: https://github.com/Zheng-Enci/markconv
- Gitee: https://gitee.com/zheng-enci050704/markconv
- GitCode: https://gitcode.com/ZhengEnCi/markconv

---

## 影响范围

### 安装方式
```bash
# 旧方式（已废弃）
pip install mdconvert
from mdconvert import MDConverter

# 新方式（推荐）
pip install markconv
from markconv import MDConverter
```

### 仓库地址
- GitHub: https://github.com/Zheng-Enci/markconv
- Gitee: https://gitee.com/zheng-enci050704/markconv
- GitCode: https://gitcode.com/ZhengEnCi/markconv

---

## Git 提交
- Commit ID: 8de8e76
- 提交信息: "重命名项目为 markconv"
- 变更文件: 9 个文件
