import re

input_file = "MYsql目录 (2).txt"
output_file = "processed_" + input_file

# 尝试不同编码格式（按优先级排序）
encodings_to_try = ['utf-8-sig', 'gbk', 'utf-16', 'ansi']

for encoding in encodings_to_try:
    try:
        with open(input_file, "r", encoding=encoding) as f_in:
            lines = f_in.readlines()
        break  # 成功读取则跳出循环
    except UnicodeDecodeError:
        continue
else:
    raise ValueError("无法解码文件，请手动检查编码格式。")

# 处理并写入新文件
with open(output_file, "w", encoding="utf-8") as f_out:
    for line in lines:
        cleaned_line = re.sub(r"\s*-\d+$", "", line.rstrip("\n"))
        f_out.write(cleaned_line + "\n")

print(f"处理完成！结果已保存到 {output_file}")
