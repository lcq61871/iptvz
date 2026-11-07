import os

input_file = "903.txt"
output_file = "903.m3u"

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit(1)

m3u_lines = ["#EXTM3U\n"]

current_group = "默认分组"

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳过空行或注释
        if not line or line.startswith("#"):
            continue
        
        # 常见 TXT 格式解析： 频道名,播放地址 或 分组,频道名,播放地址
        parts = line.split(",")
        if len(parts) >= 2:
            if len(parts) == 3:
                current_group = parts[0].strip()
                channel_name = parts[1].strip()
                channel_url = parts[2].strip()
            else:
                channel_name = parts[0].strip()
                channel_url = parts[1].strip()
            
            # 组装 M3U 格式
            extinf = f'#EXTINF:-1 group-title="{current_group}",{channel_name}\n'
            m3u_lines.append(extinf)
            m3u_lines.append(f"{channel_url}\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(m3u_lines)

print(f"Successfully converted {input_file} to {output_file}")