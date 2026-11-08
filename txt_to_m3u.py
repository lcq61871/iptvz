import os

input_file = "903.txt"
output_file = "903.m3u"

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    exit(1)

# 写入 M3U 文件头
m3u_lines = ["#EXTM3U\n"]
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
            
            # 过滤有效的直播链接
            if channel_url.startswith(("http://", "https://", "rtp://", "udp://")):
                
                # 判断链接中是否包含 :8767 端口
                if ":8767" in channel_url:
                    # 仅给带有 :8767 的源加上 7 天回放参数
                    extinf = (
                        f'#EXTINF:-1 group-title="{current_group}" '
                        f'catchup="append" '
                        f'catchup-days="7" '
                        f'catchup-source="?playseek=${{(b)yyyyMMddHHmmss}}-${{(e)yyyyMMddHHmmss}}",'
                        f'{channel_name}\n'
                    )
                else:
                    # 其他源保持普通标签
                    extinf = f'#EXTINF:-1 group-title="{current_group}",{channel_name}\n'
                
                m3u_lines.append(extinf)
                m3u_lines.append(f"{channel_url}\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(m3u_lines)

print(f"Successfully converted {input_file} to {output_file} with selective catchup support!")
