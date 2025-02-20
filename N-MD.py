import re
import sys


def convert_line(line):
    """转换单行目录格式到Markdown（保留数字章节）"""
    line = line.rstrip('\n')  # 去除换行符
    if not line.strip():
        return ""

    # 匹配缩进、数字章节和标题
    match = re.match(r'^(\t*)(\d+(?:\.\d+)*)\s+(.*)$', line)
    if not match:
        return f"<!-- 格式错误: {line} -->"  # 注释不符合格式的行

    tabs, number, title = match.groups()
    indent_level = len(tabs)

    # 计算Markdown标题级别（1-6级）
    md_level = min(indent_level + 1, 6)

    return f"{'#' * md_level} {number} {title}"


def add_section_spaces(lines):
    """在章节层级变化时添加空行"""
    formatted = []
    prev_level = 0

    for line in lines:
        if not line.strip() or line.startswith('<!--'):
            continue

        current_level = line.count('#', 0, line.find(' '))
        if current_level < prev_level:
            formatted.append('')
        formatted.append(line)
        prev_level = current_level

    return formatted


def txt_to_md(input_file, output_file):
    """主转换函数"""
    with open(input_file, 'r', encoding='utf-8') as f_in:
        raw_lines = f_in.readlines()

    # 转换每行内容
    md_lines = [convert_line(line) for line in raw_lines]

    # 添加段落间距
    formatted_lines = add_section_spaces(md_lines)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(formatted_lines))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python toc_converter.py 输入文件.txt 输出文件.md")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    txt_to_md(input_file, output_file)
    print(f"转换完成！结果已保存到 {output_file}")
