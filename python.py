# 这是一个Python示例程序，演示诈骗分子如何非法读取你的网页信息，这里只是一个很简单的事例，实际可能有很多反破解等机制
#作者秋冷鹤白，唯一作者，仅用于学习交流

def main():
    # 初始化后台列表
    houtai = []
    
    print("网址打包工具 - Python示例")
    print("输入'访问后台'可以查看所有打包的网址")
    print("输入'退出'可以结束程序\n")
    
    while True:
        user_input = input("请输入要打包的网址(或命令): ").strip()
        
        if user_input.lower() == "退出":
            print("程序结束")
            break
        elif user_input.lower() == "访问后台":
            if not houtai:
                print("后台目前没有存储任何网址")
            else:
                print("\n后台存储的所有网址:")
                for idx, url in enumerate(houtai, 1):
                    print(f"{idx}. {url}")
            print()
        else:
            # 简单的网址验证（示例中不做完整验证）
            if user_input.startswith(('http://', 'https://')):
                houtai.append(user_input)
                print(f"网址 '{user_input}' 已成功打包！\n")
            else:
                print("请输入有效的网址（应以http://或https://开头）\n")

if __name__ == "__main__":
    main()