import re
from io import StringIO
import pyperclip


def format_table():
    try:
        # 从剪贴板获取原始文本
        raw_text = pyperclip.paste()

        # 处理表格
        formatted = process_text(raw_text)

        # 将结果回写剪贴板
        pyperclip.copy(formatted)  # 注意这里变量名改为formatted
        print("格式化完成，结果已存入剪贴板！")
    except Exception as e:
        print(f"处理失败: {str(e)}")


def process_text(input_text):
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]

    # 提取有效数据行
    data = []
    for line in lines:
        if re.match(r'^\|.*\|.*\|$', line):
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


if __name__ == "__main__":
    format_table()

