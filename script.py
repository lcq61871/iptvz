import requests

def fetch_and_filter(url, output_file):
    # 获取文件内容
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件
    with open(output_file, 'w', encoding="utf-8") as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter('https://raw.githubusercontent.com/luoye20230624/ZB/refs/heads/main/iptv_list.txt', 'live_ipv4.txt')
    fetch_and_filter('https://raw.githubusercontent.com/ngdikman/hksar/refs/heads/main/dianxin.txt', 'dx.txt')
