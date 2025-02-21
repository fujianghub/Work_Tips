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