"""
========================================
脚本功能 (Script Functionality):
========================================
该脚本将 eQTL 数据按指定列（基因名列）分组，并将每组数据保存为制表符分隔的 CSV 文件。

输入参数 (Input Parameters):
1. --input: 输入文件路径 (Path to the input CSV file).
   示例 (Example): ../eQTLchr1_1Mb.csv
2. --output_dir: 输出文件夹路径 (Path to the output directory).
   示例 (Example): ./output_files
3. --gene_col: 指定基因名字列的索引 (Index of the column containing gene names).
   注意：列索引从 1 开始计数 (Note: Index starts from 1).
   示例 (Example): 7

运行示例 (Run Example):
python split_genes.py --input ../eQTLchr1_1Mb.csv --output_dir ./output_files --gene_col 7

错误处理 (Error Handling):
- 如果缺少必要参数，脚本会提示使用说明。
- 如果输入文件不存在，脚本会报错。
- 如果基因列索引无效，脚本会提示列索引范围。

输出结果 (Output Results):
- 按基因分组的制表符分隔文件将保存到指定的输出文件夹中。
- 每个文件名以基因名命名 (e.g., CDK11A.tsv)。

========================================
"""
import pandas as pd
import os
import argparse

# 设置命令行参数解析 (Setup argument parsing)
parser = argparse.ArgumentParser(description="Split eQTL data by gene.")
parser.add_argument("--input", required=True, help="Path to the input CSV file.")  # 输入文件路径
parser.add_argument("--output_dir", required=True, help="Path to the output directory.")  # 输出文件夹路径
parser.add_argument("--gene_col", type=int, required=True, help="Index of the column containing gene names (1-based).")  # 基因列索引

# 解析参数 (Parse arguments)
args = parser.parse_args()

# 获取参数值 (Retrieve argument values)
input_file = args.input
output_dir = args.output_dir
gene_col_index = args.gene_col - 1  # 转换为 Python 的 0-based 索引 (Convert to 0-based index)

# 检查输出文件夹是否存在，如果不存在则创建 (Ensure output directory exists)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 加载输入文件 (Load the input CSV file)
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    raise FileNotFoundError(f"输入文件未找到: {input_file} (Input file not found: {input_file})")

# 检查基因列索引是否有效 (Validate gene column index)
if gene_col_index < 0 or gene_col_index >= df.shape[1]:
    raise ValueError(f"无效的基因列索引: {gene_col_index + 1} (Invalid gene column index: {gene_col_index + 1}). "
                     f"索引范围 (Valid range): 1 到 (to) {df.shape[1]}.")

# 获取基因列名 (Retrieve the column name for the gene column)
gene_col_name = df.columns[gene_col_index]
print(f"使用列 '{gene_col_name}' 作为基因列 (Using column '{gene_col_name}' as the gene column).")

# 按基因分组并保存为制表符分隔的文件 (Group by gene and save to tab-separated files)
for gene, group in df.groupby(gene_col_name):
    output_file = os.path.join(output_dir, f"{gene}.tsv")
    group.to_csv(output_file, sep="\t", index=False)  # 输出为制表符分隔文件
    print(f"保存基因数据到文件: {output_file} (Saved gene data to file: {output_file})")

print(f"所有基因处理完成，文件保存在 {output_dir} (All genes processed. Files are saved in {output_dir}).")
