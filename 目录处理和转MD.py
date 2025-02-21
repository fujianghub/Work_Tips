import re


def detect_file_encoding(file_path):
    """自动检测文件编码"""
    encodings = ['utf-8-sig', 'gb18030', 'utf-16', 'iso-8859-1']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                f.read()
            return enc
        except UnicodeDecodeError:
            continue
    return None


def process_directory(input_file, output_file):
    # 检测文件编码
    encoding = detect_file_encoding(input_file)
    if not encoding:
        raise ValueError("无法检测文件编码，请手动指定编码格式")

    with open(input_file, 'r', encoding=encoding) as f:
        lines = f.readlines()

    output = []
    for line in lines:
        # 去除行尾页码（支持1-3位数字，支持负号开头）
        cleaned = re.sub(r'\s+-?\d{1,3}\s*$', '', line.rstrip())

        # 计算缩进层级（按制表符数量）
        indent_level = len(cleaned) - len(cleaned.lstrip('\t'))

        # 移除行首空白字符
        content = cleaned.lstrip('\t')

        # 生成Markdown标题（自动保持大纲编号）
        md_header = '#' * (indent_level + 1) + ' ' + content
        output.append(md_header)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))


# 使用示例
process_directory('zabbix.txt', 'Zabbix.md')