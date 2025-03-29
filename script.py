import requests

def fetch_and_filter():
    url = 'https://raw.githubusercontent.com/luoye20230624/ZB/refs/heads/main/iptv_list.txt'
    
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
        # 保存到新文件
    with open('live_ipv4.txt', 'w') as file:
        file.write('\n'.join(filtered_lines))


    # ================= 第二部分：追加特殊文件 =================
    special_files = ["AKTV.txt", "maotv.txt"]
    for file in special_files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                # 保持原文件完整结构
                content = []
                current_category = ""
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.endswith("#genre#"):
                        current_category = line
                        content.append(f"\n{current_category}")
                    else:
                        content.append(line)
                
                if content:
                    final_content.append("\n".join(content))
                    print(f"已追加文件: {file} (共{len(content)}行)")

    # ================= 写入最终文件 =================
    with open("iptv_list.txt", "w", encoding='utf-8') as f:
        f.write("\n\n".join(final_content))

if __name__ == "__main__":
    fetch_and_filter()
