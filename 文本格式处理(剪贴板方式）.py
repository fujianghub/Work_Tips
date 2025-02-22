import re
from io import StringIO
import pyperclip


def format_table():
    try:
        raw_text = pyperclip.paste()
        formatted = process_text(raw_text)
        pyperclip.copy(formatted)
        print("格式化完成，结果已存入剪贴板！")
    except Exception as e:
        print(f"处理失败: {str(e)}")


def process_text(input_text):
    lines = [line.strip() for line in input_text.split('\n') if line.strip()]

    # 智能识别表头和有效数据
    header = None
    data = []
    for line in lines:
        if re.match(r'^\|.*\|.*\|$', line):
            parts = [p.strip() for p in line[1:-1].split('|')]
            if len(parts) != 2:
                continue

            # 检测表头
            if parts[0].lower() == 'variable_name' and parts[1].lower() == 'value':
                if not header:
                    header = parts  # 保留第一个有效表头
                continue  # 跳过后续表头

            # 过滤数据重复项
            if parts not in data:
                data.append(parts)

    if not header or not data:
        return "未检测到有效表格数据"

    # 动态计算列宽（基于最大值）
    col1_width = max(len(row[0]) for row in [header] + data)
    col2_width = max(len(row[1]) for row in [header] + data)

    # 构建表格框架
    separator = f"+{'-' * (col1_width + 2)}+{'-' * (col2_width + 2)}+"
    format_str = "| {:<%d} | {:<%d} |" % (col1_width, col2_width)

    # 生成最终输出
    output = StringIO()
    output.write(separator + "\n")
    output.write(format_str.format(header[0], header[1]) + "\n")
    output.write(separator + "\n")
    for row in data:
        output.write(format_str.format(row[0], row[1]) + "\n")
    output.write(separator)

    # 保留统计信息
    stats = next((line for line in lines if re.search(r'\d+ rows? in set', line)), None)
    if stats:
        output.write("\n" + stats.split('|')[-1].strip())

    return output.getvalue()


if __name__ == "__main__":
    format_table()