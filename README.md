
# Emailconcurrency concurrent DDOS

`Version: 1.0.2` | [GitHub Repository](https://github.com/TR1123/Emailconcurrency)




```
 _____              _  _                                                          
|   __| _____  ___ |_|| |   ___  ___  ___  ___  _ _  ___  ___  ___  ___  ___  _ _ 
|   __||     || .'|| || |  |  _|| . ||   ||  _|| | ||  _||  _|| -_||   ||  _|| | |
|_____||_|_|_||__,||_||_|  |___||___||_|_||___||___||_|  |_|  |___||_|_||___||_  |
                                                                             |___|
[hosted by: https://github.com/TR1123]

[Version: 1.0.2]
```
## ！！ 一次性发送超100封邮件以上，不会被视为垃圾邮件！！


## ！！ API目前接口任然有效！！


## 运行效果  

## 只利用公开API接口进行发送已达到骚扰效果！


<img width="1115" height="628" alt="QQ20250717-152612" src="https://github.com/user-attachments/assets/f10909c4-1686-4d77-a65b-e48b06396938" />
↑
↓
<img width="833" height="778" alt="QQ20250717-152633" src="https://github.com/user-attachments/assets/eb8c3696-0e33-43b6-8b67-218cf4e6533d" />







## 功能概述

一个多线程邮件发送工具，支持：
- 批量发送邮件请求
- 代理IP轮换
- 多API接口支持
- 交互式/命令行参数两种模式

## 安装要求

```bash
pip install requests colorama
```

## API接口配置

```python
API_LIST = {
 },
    "example_api": {
        "name": "Example API",
        "url": "https://api.example.com/endpoint",
        "method": "POST",
        "param_name": "email"
    }
}
```

## 使用说明

### 命令行参数

| 参数 | 描述 |
|------|------|
| `--email` | 目标邮箱地址 |
| `--request` | 总请求次数 |
| `--requ` | 每次循环请求次数 |
| `--time` | 循环间隔时间(秒) |
| `--input` | 使用交互式输入模式 |
| `--proxy` | 代理IP文件路径 |
| `--view` | 查看可用API接口 |
| `--version` | 显示当前版本 |
| `--update` | 更新脚本 |

### 使用示例

1. **命令行模式**：
```bash
python Emailconcurrency.py --email test@example.com --request 100 --requ 10 --time 5 --proxy proxies.txt
```

2. **交互模式**：
```bash
python Emailconcurrency.py --input
```

3. **查看API接口**：
```bash
python Emailconcurrency.py --view
```

## 代码结构

### 核心函数

- `load_proxies(proxy_file)` - 加载代理IP列表
- `send_email(api, email, proxy)` - 发送邮件请求
- `view_apis()` - 显示可用API接口
- `check_version()` - 检查当前版本
- `update_script()` - 自动更新脚本

### 多线程处理

```python
threads = []
for i in range(current_batch):
    proxy = random.choice(proxies) if proxies else None
    t = threading.Thread(target=send_email, args=(API_LIST['chickfrp'], email, proxy))
    threads.append(t)
    t.start()
```

## 代理文件格式

每行一个代理IP，格式：
```
ip:port
username:password@ip:port
```


## 联系

```bash
Telegram ： @☆☆☆☆☆☆☆☆
```









