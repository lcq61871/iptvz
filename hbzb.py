import os

def merge_files(input_files, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file in input_files:
                if os.path.exists(file):
                    with open(file, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read() + '\n')  # 添加换行符确保内容区分
                else:
                    print(f"Warning: {file} does not exist.")
        print(f"Merged file saved as {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_files = ["hnzb.txt", "maotv.txt", "dianxin.txt"]
    output_file = "hbzb.txt"
    merge_files(input_files, output_file)
