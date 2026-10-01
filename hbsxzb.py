import requests

# 远程文件 Raw 链接地址
DSZB_URL = "https://raw.githubusercontent.com/lcq61871/iptvz/main/dszb.txt"
OUTPUT_STREAMS_URL = (
    "https://raw.githubusercontent.com/lcq61871/df1/main/output_streams.txt"
)

# 目标输出文件名
OUTPUT_FILE = "904.txt"


def get_remote_content(url, description):
    """
    拉取远程文件文本内容
    """
    print(f"🌐 正在获取 {description}...")
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200 and response.text.strip():
            print(f"✅ 成功拉取 {description}")
            return response.text.strip()
        else:
            print(f"⚠️ 拉取 {description} 失败 (HTTP {response.status_code})")
            return ""
    except Exception as e:
        print(f"❌ 请求 {description} 异常: {e}")
        return ""


def main():
    print("🚀 开始合并流程...")
    combined_content = []

    # 1. 获取 dszb.txt 内容（放在前面）
    dszb_text = get_remote_content(DSZB_URL, "dszb.txt")
    if dszb_text:
        combined_content.append(dszb_text)

    # 2. 获取 output_streams.txt 内容（放在后面）
    output_streams_text = get_remote_content(
        OUTPUT_STREAMS_URL, "output_streams.txt"
    )
    if output_streams_text:
        combined_content.append(output_streams_text)

    # 3. 合并并保存为 904.txt
    if combined_content:
        final_text = "\n\n".join(combined_content)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(final_text)
        print(f"\n🎉 合并成功！已生成文件: {OUTPUT_FILE}")
    else:
        print("\n⚠️ 未能获取到任何有效内容，未生成文件。")


if __name__ == "__main__":
    main()