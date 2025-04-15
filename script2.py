import requests

def fetch_and_filter():
    urls = [
        'https://raw.githubusercontent.com/luoye20230624/ZB/refs/heads/main/iptv_list.txt',
        'https://raw.githubusercontent.com/lcq61871/df1/refs/heads/main/filtered_streams.txt',
        'https://raw.githubusercontent.com/ngdikman/hksar/refs/heads/main/dianxin.txt'
    ]

    all_filtered_lines = []

    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"请求失败：{url}，状态码：{response.status_code}")
            continue

        content = response.text
        filtered_lines = [line for line in content.splitlines() if 'ipv6' not in line.lower()]
        all_filtered_lines.extend(filtered_lines)

    # 保存到新文件
    with open('hnzb.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(all_filtered_lines))

    print("所有过滤后的内容已保存到 hnzb.txt")

if __name__ == "__main__":
    fetch_and_filter()
