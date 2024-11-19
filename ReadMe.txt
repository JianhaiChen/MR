========================================
README: 按基因分组脚本 (Split eQTL Data by Gene Script)
========================================

本脚本用于将输入的 eQTL 数据按指定列（基因名列）分组，并将每组数据保存为单独的制表符分隔文件 (.tsv)。

This script splits the input eQTL data by the specified column (gene name column) 
and saves each group into a separate tab-separated file (.tsv).

----------------------------------------
运行环境要求 (Requirements):
----------------------------------------

1. Python >= 3.6
2. 必要的 Python 库 (Required Python Libraries):
   - pandas

安装依赖库的命令 (Command to install dependencies):
   pip install pandas

----------------------------------------
脚本功能 (Script Functionality):
----------------------------------------

1. 将输入的 eQTL 数据按基因名分组。
2. 每个基因的数据保存为一个独立的 .tsv 文件。
3. 每个文件保留原始数据的列名，且以基因名命名。

1. Split the input eQTL data by gene name.
2. Save data for each gene into a separate .tsv file.
3. Retain the original column names in each file, named after the gene.

----------------------------------------
输入参数说明 (Input Parameters):
----------------------------------------

1. --input:
   输入文件路径 (Path to the input CSV file).
   示例 (Example): ../eQTLchr1_1Mb.csv

2. --output_dir:
   输出文件夹路径 (Path to the output directory).
   示例 (Example): ./output_files

3. --gene_col:
   基因名字列的索引 (Index of the column containing gene names).
   注意：列索引从 1 开始计数 (Note: Index starts from 1).
   示例 (Example): 7

----------------------------------------
运行示例 (Run Example):
----------------------------------------

假设输入文件路径为 "../eQTLchr1_1Mb.csv"，基因名位于第 7 列。
Assume the input file is located at "../eQTLchr1_1Mb.csv" and gene names are in column 7.

运行命令 (Run Command):
   python split_genes.py --input ../eQTLchr1_1Mb.csv --output_dir ./output_files --gene_col 7

----------------------------------------
输出结果 (Output Results):
----------------------------------------

- 按基因分组的制表符分隔文件 (.tsv) 将保存到指定的输出文件夹中。
- 每个文件的命名格式为 `{gene_name}.tsv`，例如 `CDK11A.tsv`。
- 每个文件包含原始数据的列名和该基因的所有行。

- Tab-separated files (.tsv) grouped by gene will be saved in the specified output directory.
- Each file is named as `{gene_name}.tsv`, e.g., `CDK11A.tsv`.
- Each file contains the original column names and all rows for the specific gene.

----------------------------------------
注意事项 (Notes):
----------------------------------------

1. 输入文件必须为 CSV 格式，列名必须唯一。
   The input file must be in CSV format with unique column names.

2. 基因列索引的范围必须在有效范围内（从 1 到列总数）。
   The gene column index must be within the valid range (from 1 to total number of columns).

3. 确保输出目录具有写入权限。如果不存在，会自动创建。
   Ensure the output directory is writable. It will be created automatically if it doesn't exist.

4. 所有输出文件以制表符分隔，适配 MR 分析需求。
   All output files are tab-separated for compatibility with MR analysis.

----------------------------------------
问题排查 (Troubleshooting):
----------------------------------------

1. 输入文件未找到 (Input file not found):
   错误信息 (Error Message):
      FileNotFoundError: 输入文件未找到: ../eQTLchr1_1Mb.csv
   解决方法 (Solution):
      检查输入文件路径是否正确，确保文件存在。
      Check the input file path and ensure the file exists.

2. 无效的基因列索引 (Invalid gene column index):
   错误信息 (Error Message):
      Invalid gene column index: 8. Valid range: 1 to 12.
   解决方法 (Solution):
      检查基因列索引是否正确，索引从 1 开始计数。
      Verify the gene column index. It starts from 1.

3. 缺少必要的 Python 库 (Missing required Python library):
   错误信息 (Error Message):
      ModuleNotFoundError: No module named 'pandas'
   解决方法 (Solution):
      使用以下命令安装 pandas:
      Use the following command to install pandas:
         pip install pandas

----------------------------------------
作者信息 (Author Information):
----------------------------------------

作者 (Author): Jian-Hai Chen
单位 （affiliation） 芝加哥大学 The University of Chicago
日期 (Date): 11-19-2024
联系 (Contact): jianhaichen@uchicago.edu

========================================