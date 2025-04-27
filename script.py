import requests

def fetch_and_filter():
    url = 'https://raw.githubusercontent.com/lcq61871/df1/refs/heads/main/filtered_streams.txt'
    
    # 获取文件内容
    response = requests.get(url)
    content = response.text
    
    # 过滤掉包含 "ipv6" 的行
    filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
    
    # 保存到新文件
    with open('filtered_streams.txt', 'w') as file:
        file.write('\n'.join(filtered_lines))

if __name__ == "__main__":
    fetch_and_filter()
