import os

def merge_files(input_files, output_file):
    try:
        # 删除旧txt
        if "dszb.tv" in input_files and os.path.exists("dszb.tv"):
            os.remove("dszb.tv")
            print("Old dszb.tv deleted.")

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
    input_files = ["hnzb.txt", "list.tv"]  
    output_file = "dszb.tv"
    merge_files(input_files, output_file)
