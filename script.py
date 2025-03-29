import requests

def fetch_and_filter():
    url = 'https://raw.githubusercontent.com/luoye20230624/ZB/refs/heads/main/iptv_list.txt'
    
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    

# 合并所有的txt文件
file_contents = []
file_paths = ["iptv_list.txt'", "AKTV.txt", "maotv.txt"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)

# 写入合并后的txt文件
with open("zhzb.txt", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))

if __name__ == "__main__":
    fetch_and_filter()
