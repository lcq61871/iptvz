import os

input_file = "903.txt"
output_file = "903.m3u"

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit(1)

# 在文件头声明 M3U 格式，并可以声明支持回放（部分播放器如 TiviMate 需要）
m3u_lines = ['#EXTM3U catchup="append" catchup-days="7" catchup-source=""\n']
current_group = "未分类"

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳过空行和纯注释
        if not line or line.startswith("#ext"):
            continue
        
        # 匹配 `#genre#` 分组行
        if ",#genre#" in line:
            current_group = line.split(",#genre#")[0].strip()
            continue
        
        # 匹配 `频道名,URL` 格式
        parts = line.split(",")
        if len(parts) >= 2:
            channel_name = parts[0].strip()
            channel_url = ",".join(parts[1:]).strip()
            
            # 过滤链接
            if channel_url.startswith(("http://", "https://", "rtp://", "udp://")):
                
                # 【可选逻辑】如果你想针对特定的源（例如名字里带回放，或者特定域名的源）加上回放标记：
                # 比如：如果你的回放源链接包含某个特定关键词，可以给它加 catchup 标签
                # 这里默认给所有源都加上支持 7 天回放的通用扩展属性：
                extinf = f'#EXTINF:-1 group-title="{current_group}" catchup="default" catchup-days="7",{channel_name}\n'
                
                m3u_lines.append(extinf)
                m3u_lines.append(f"{channel_url}\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(m3u_lines)

print(f"Successfully converted {input_file} to {output_file} with catchup support!")
