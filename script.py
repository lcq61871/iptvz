import requests

def fetch_and_filter(url, output_file):
    response = requests.get(url)
    
    print(f"Fetching {url} -> Status Code: {response.status_code}")  # 打印状态码
    response.raise_for_status()  # 确保请求成功，否则报错
    
    content = response.text
    print(f"Content preview ({len(content)} bytes):\n", content[:500])  # 预览部分数据
    
    # 过滤 "ipv6"
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 如果过滤后仍然有数据，则写入文件
    if filtered_lines:
        with open(output_file, 'w', encoding="utf-8") as file:
            file.write('\n'.join(filtered_lines))
        print(f"✅ File saved: {output_file}")
    else:
        print(f"⚠️ No valid content found, file {output_file} not created.")

if __name__ == "__main__":
    fetch_and_filter('https://raw.githubusercontent.com/luoye20230624/ZB/refs/heads/main/iptv_list.txt', 'live_ipv4.txt')
    fetch_and_filter('https://raw.githubusercontent.com/ngdikman/hksar/refs/heads/main/dianxin.txt', 'dx.txt')
