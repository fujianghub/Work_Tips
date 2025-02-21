# 目录处理.py

- 一个用于清理文本文件行尾冗余 "-数字、数字" 并转为`MD`的 Python 脚本，专为处理结构化文档设计

- ✨ 功能特性

  - **智能清理**  自动删除每行末尾的 `-数字` 格式冗余内容（如 `-167、22`）
  - **编码兼容**  支持 `utf-8`/`utf-8-sig`/`gbk`/`utf-16` 等多种编码格式
  - **转MD**  将处理过的目录转为MD格式

- 🚀 快速使用

  - 环境要求：Python 3.6+

  - 使用步骤：
    1. 将脚本和待处理文件放在同一目录
    2. 在Pycharm中使用脚本模式
    3. 运行命令：`python convert_dir.py zabbix.txt output.md`
---
# 文本格式整理.py
- 将输入的乱序的文本转为格式化的表格：

```
+---------------------------------------+--------------+
| Variable_name                         | Value        |
+---------------------------------------+--------------+
| Variable_name                         | Value        |
| rpl_semi_sync_master_enabled          | ON           |
| rpl_semi_sync_master_timeout          | 3000         |
| rpl_semi_sync_master_trace_level      | 32           |
| rpl_semi_sync_master_wait_no_slave    | ON           |
| rpl_semi_sync_master_wait_point       | AFTER_COMMIT |
| rpl_semi_sync_slave_delay_master      | OFF          |
| rpl_semi_sync_slave_enabled           | OFF          |
| rpl_semi_sync_slave_kill_conn_timeout | 5            |
| rpl_semi_sync_slave_trace_level       | 32           |
+---------------------------------------+--------------+
9 rows in set (0.002 sec)
```
# 文本格式处理(剪贴板方式).py
以下是使用剪贴板操作表格格式化脚本的详细指南：

### 📋 操作流程（Windows/macOS通用）

1. **安装依赖库**
```bash
pip install pyperclip
```

### 🖥️ 分步操作演示

1. **复制源文本**
   - 用鼠标选中要格式化的表格文本（含边框和内容）
   - 按 `Ctrl+C` (Windows) / `Command+C` (macOS) 复制

2. **运行脚本**
   ```bash
   python table_formatter.py
   ```

3. **粘贴结果**
   - 打开目标文档（Word/记事本/Markdown文件等）
   - 按 `Ctrl+V` (Windows) / `Command+V` (macOS) 粘贴



### 🛠️ 技术原理

1. **剪贴板交互流程**
   ```mermaid
   graph LR
   A[用户复制表格文本] --> B[脚本读取剪贴板]
   B --> C[处理表格格式]
   C --> D[结果写入剪贴板]
   D --> E[用户粘贴使用]
   ```

2. **异常处理机制**
   - 自动检测剪贴板内容是否为空
   - 捕获无效表格格式错误
   - 网络剪贴板同步问题处理



### ⚠️ 常见问题解决方案

**问题1：提示`ModuleNotFoundError: No module named 'pyperclip'`**
```bash
# 安装时使用清华镜像加速
pip install pyperclip -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**问题2：处理中文乱码**
```python
# 在脚本开头添加编码声明
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

**问题3：剪贴板内容不更新**
```python
# 添加强制刷新（Windows专用）
import time
time.sleep(0.5)  # 等待500ms确保复制完成
```


### 🎯 高级技巧

1. **创建桌面快捷方式**
   ```bash
   # Windows
   pythonw.exe table_formatter.py  # 后台运行

   # macOS
   osascript -e 'do shell script "python3 table_formatter.py"'
   ```

2. **绑定全局快捷键**
   - 使用AutoHotkey（Windows）或Keyboard Maestro（macOS）
   - 设置快捷键组合（如 `Ctrl+Alt+T`）自动执行脚本

3. **跨设备同步剪贴板**
   ```python
   # 结合Pushbullet API实现
   import requests
   def sync_clipboard():
       pb_key = "your_api_key"
       data = {"type": "note", "body": pyperclip.paste()}
       requests.post('https://api.pushbullet.com/v2/pushes', 
                    auth=(pb_key, ''), json=data)
   ```


### 📌 使用示例演示

**操作前剪贴板内容：**
```
| Variable | Value |
|----------|-------|
| timeout | 3000 |
```

**操作后剪贴板内容：**
```
+------------+-------+
| Variable   | Value |
+------------+-------+
| timeout    | 3000  |
+------------+-------+
```
