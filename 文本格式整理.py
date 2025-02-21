import re
from io import StringIO


def format_text_table(input_text):
    # 预处理输入文本
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]

    # 提取有效数据行
    data = []
    for line in lines:
        if re.match(r'^\|.*\|.*\|$', line):  # 匹配 | 列1 | 列2 | 格式
            # 移除首尾的|并分割列
            parts = [p.strip() for p in line[1:-1].split('|')]
            if len(parts) == 2:
                data.append(parts)

    if not data:
        return "No valid table data found"

    # 计算列宽
    col1_width = max(len(row[0]) for row in data)
    col2_width = max(len(row[1]) for row in data)

    # 构建表格边框
    separator = f"+{'-' * (col1_width + 2)}+{'-' * (col2_width + 2)}+"

    # 构建格式化字符串
    format_str = "| {:<%d} | {:<%d} |" % (col1_width, col2_width)

    # 生成输出文本
    output = StringIO()
    output.write(separator + "\n")
    output.write(format_str.format("Variable_name", "Value") + "\n")
    output.write(separator + "\n")
    for row in data:
        output.write(format_str.format(row[0], row[1]) + "\n")
    output.write(separator)

    # 保留原始统计信息
    stats = next((line for line in lines if 'rows in set' in line), None)
    if stats:
        output.write("\n" + stats)

    return output.getvalue()


# 使用示例
if __name__ == "__main__":
    # 从剪贴板获取输入
    try:
        import pyperclip

        input_text = pyperclip.paste()
    except ImportError:
        input_text = """
        +---------------------------------------+--------------+
| Variable_name | Value |
+---------------------------------------+--------------+
| rpl_semi_sync_master_enabled | ON |
| rpl_semi_sync_master_timeout | 3000 |
| rpl_semi_sync_master_trace_level | 32 |
| rpl_semi_sync_master_wait_no_slave | ON |
| rpl_semi_sync_master_wait_point | AFTER_COMMIT |
| rpl_semi_sync_slave_delay_master | OFF |
| rpl_semi_sync_slave_enabled | OFF |
| rpl_semi_sync_slave_kill_conn_timeout | 5 |
| rpl_semi_sync_slave_trace_level | 32 |
+---------------------------------------+--------------+
9 rows in set (0.002 sec)
        """

    print(format_text_table(input_text))