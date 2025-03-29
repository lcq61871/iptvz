def merge_files(file1, file2, output_file):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            content1 = f1.read()
            content2 = f2.read()
        
        with open(output_file, 'w', encoding='utf-8') as out:
            out.write(content1 + '\n' + content2)
        
        print(f"合并完成，文件已保存为 {output_file}")
    except Exception as e:
        print(f"合并文件时出错: {e}")

if __name__ == "__main__":
    merge_files('aktv.txt', 'maotv.txt', 'hbzb.txt')
