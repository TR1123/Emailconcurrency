import requests
import threading
import argparse
import time
import sys
import os
from colorama import Fore, Style, init
import random



os.system("cls" if os.name == "nt" else "clear")

init()

VERSION = "1.0.2"
UPDATE_URL = "https://raw.githubusercontent.com/TR1123/ChickFRP-Email/main/1.py"
API_LIST = {
    "chickfrp": {
        "name": "ChickFRP Registration",
        "url": "https://api.chickfrp.com/email_code",
        "method": "POST",
        "param_name": "email"
    },
    "example_api": {
        "name": "Example API",
        "url": "https://api.example.com/endpoint",
        "method": "POST",
        "param_name": "email"
    }
}

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def show_banner():
    print_colored(r"""
 _____              _  _                                                          
|   __| _____  ___ |_|| |   ___  ___  ___  ___  _ _  ___  ___  ___  ___  ___  _ _ 
|   __||     || .'|| || |  |  _|| . ||   ||  _|| | ||  _||  _|| -_||   ||  _|| | |
|_____||_|_|_||__,||_||_|  |___||___||_|_||___||___||_|  |_|  |___||_|_||___||_  |
                                                                             |___| 
[hosted by: https://github.com/TR1123]
""", color=Fore.BLUE)
    print_colored(f"[Version: {VERSION}]", color=Fore.YELLOW)
    print()

def load_proxies(proxy_file):
    
    try:
        with open(proxy_file, 'r') as f:
            proxies = [line.strip() for line in f if line.strip()]
        return proxies
    except Exception as e:
        print(f"{Fore.RED}[-] Error loading proxy file/加载代理文件出错: {str(e)}{Fore.RESET}")
        return None

def send_email(api, email, proxy=None):
    data = {api["param_name"]: email}
    proxies = None
    if proxy:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
    
    try:
        response = requests.post(api["url"], data=data, proxies=proxies, timeout=10)
        print(f"{Fore.GREEN}[+] [INFO] Sent to {email} Status/状态: {response.status_code} {f'Proxy/代理: {proxy}' if proxy else ''}{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error sending to {email}/发送到 {email} 出错: {str(e)} {f'Proxy/代理: {proxy}' if proxy else ''}{Fore.RESET}")

def view_apis():

    print(f"\n{Fore.CYAN}Available API Endpoints/可用API接口:{Fore.RESET}")
    for api_name, api_info in API_LIST.items():
        print(f"\n{Fore.YELLOW}API Name/接口名称: {api_name}{Fore.RESET}")
        print(f"Service/服务: {api_info['name']}")
        print(f"URL/地址: {api_info['url']}")
        print(f"Method/方法: {api_info['method']}")
        print(f"Parameter/参数: {api_info['param_name']}")
    print()

def check_version():

    print(f"\n{Fore.GREEN}Current Version/当前版本: {VERSION}{Fore.RESET}\n")

def update_script():
    
    try:
        print(f"{Fore.YELLOW}[*] Checking for updates/检查更新中...{Fore.RESET}")
        response = requests.get(UPDATE_URL)
        if response.status_code == 200:
            with open(__file__, 'wb') as f:
                f.write(response.content)
            print(f"{Fore.GREEN}[+] Script updated successfully!/脚本更新成功!{Fore.RESET}")
            print(f"{Fore.YELLOW}[*] Please restart the script/请重启脚本{Fore.RESET}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}[-] Failed to download update (HTTP {response.status_code})/下载更新失败 (HTTP {response.status_code}){Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[-] Update failed/更新失败: {str(e)}{Fore.RESET}")

def main():
    
    class BilingualFormatter(argparse.HelpFormatter):
        def _format_action(self, action):
            if action.help:
                parts = action.help.split('/')
                if len(parts) > 1:
                    action.help = f"{parts[0].strip()} ({parts[1].strip()})"
            return super()._format_action(action)


    parser = argparse.ArgumentParser(
        description="Email Sending Tool/邮件发送工具",
        formatter_class=BilingualFormatter
    )
    
    parser.add_argument(
        "--email", 
        help="Target email address/目标邮箱地址"
    )
    parser.add_argument(
        "--request", 
        type=int, 
        help="Total number of requests/总请求次数"
    )
    parser.add_argument(
        "--requ", 
        type=int, 
        help="Number of requests per cycle/每次循环请求次数"
    )
    parser.add_argument(
        "--time", 
        type=int, 
        help="Cycle interval in seconds/循环间隔时间(秒)"
    )
    parser.add_argument(
        "--input", 
        action="store_true", 
        help="Use interactive input mode/使用交互式输入模式"
    )
    parser.add_argument(
        "--proxy", 
        help="Path to proxy IP file/代理IP文件路径"
    )
    parser.add_argument(
        "--view", 
        action="store_true", 
        help="View available API endpoints/查看可用API接口"
    )
    parser.add_argument(
        "--version", 
        action="store_true", 
        help="Show current version/显示当前版本"
    )
    parser.add_argument(
        "--update", 
        action="store_true", 
        help="Update the script/更新脚本"
    )
    
    args = parser.parse_args()

   
    if args.view:
        view_apis()
        return
    if args.version:
        check_version()
        return
    if args.update:
        update_script()
        return

    show_banner()

   
    proxies = None
    if args.proxy:
        proxies = load_proxies(args.proxy)
        if not proxies:
            print(f"{Fore.RED}[!] Failed to load proxies, exiting.../无法加载代理IP，程序将退出{Fore.RESET}")
            return
        print(f"{Fore.YELLOW}[*] Loaded {len(proxies)} proxy IPs/已加载 {len(proxies)} 个代理IP{Fore.RESET}")

   
    if args.input or (not args.email and not args.request):
      
        email = input(f"{Fore.GREEN}[*] Target email/目标邮箱：{Fore.RESET}")
        total_requests = int(input(f"{Fore.GREEN}[*] Total requests/总请求次数：{Fore.RESET}"))
        loop_requests = int(input(f"{Fore.GREEN}[*] Requests per cycle/每次循环请求次数：{Fore.RESET}"))
        interval = int(input(f"{Fore.GREEN}[*] Cycle interval (seconds)/循环间隔时间(秒)：{Fore.RESET}"))
    else:
    
        if not args.email or not args.request:
            print(f"{Fore.RED}[!] Error: Must provide both --email and --request parameters/错误：必须提供 --email 和 --request 参数{Fore.RESET}")
            return
        
        email = args.email
        total_requests = args.request
        loop_requests = args.requ if args.requ else total_requests
        interval = args.time if args.time else 0

    print(f"{Fore.YELLOW}[*] Starting to send emails to {email}/开始发送邮件到 {email}{Fore.RESET}")
    print(f"{Fore.YELLOW}[*] Total requests/总请求次数: {total_requests}{Fore.RESET}")
    print(f"{Fore.YELLOW}[*] Requests per cycle/每次循环请求次数: {loop_requests}{Fore.RESET}")
    print(f"{Fore.YELLOW}[*] Cycle interval/循环间隔时间: {interval} seconds/秒{Fore.RESET}")

    remaining_requests = total_requests
    loop_count = 0

    while remaining_requests > 0:
        loop_count += 1
        current_batch = min(loop_requests, remaining_requests)
        
        print(f"{Fore.CYAN}[*] Cycle {loop_count}, sending {current_batch} requests/第 {loop_count} 轮循环，发送 {current_batch} 次请求{Fore.RESET}")
        
        threads = []
        for i in range(current_batch):
            proxy = random.choice(proxies) if proxies else None
            t = threading.Thread(target=send_email, args=(API_LIST['chickfrp'], email, proxy))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()

        remaining_requests -= current_batch
        
        if remaining_requests > 0 and interval > 0:
            print(f"{Fore.YELLOW}[*] Waiting {interval} seconds for next cycle.../等待 {interval} 秒后进行下一轮...{Fore.RESET}")
            time.sleep(interval)

    print(f"{Fore.YELLOW}[*] All requests completed/所有请求已完成{Fore.RESET}")

if __name__ == "__main__":
    main()