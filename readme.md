###
Baby Favicon Tool V1.0

网站 favicon 获取工具  

接口：  
1. 获取 favicon 数据，返回 json 格式  
http://127.0.0.1:5000/api/get_favicon?url=oba.by  
返回数据内容：  
```json
[
  {
    "format": "png",
    "height": 300,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-300x300.png",
    "width": 300
  },
  {
    "format": "png",
    "height": 200,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-200x200.png",
    "width": 200
  },
  {
    "format": "png",
    "height": 192,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-200x200.png",
    "width": 192
  },
  {
    "format": "png",
    "height": 32,
    "url": "https://oba.by/wp-content/uploads/2020/09/icon-500-100x100.png",
    "width": 32
  },
  {
    "format": "ico",
    "height": 0,
    "url": "https://oba.by/favicon.ico",
    "width": 0
  },
  {
    "format": "jpg",
    "height": 0,
    "url": "https://h4ck.org.cn/screenshots/obaby_tuya.jpg",
    "width": 0
  }
]
```
2. 直接返回 favicon 链接  
http://127.0.0.1:5000/api/redirect_favicon?url=oba.by  
返回数据内容为上述接口的第一个结果，例如上面的 域名将会直接 302跳转到 https://oba.by/wp-content/uploads/2020/09/icon-500-300x300.png  
如果没有 favicon 将会返回默认连接：https://h4ck.org.cn/wp-content/uploads/2024/09/favicon.png  

安装：  
```shell
1. pip install -r requirement.pip
2. apt install redis-server 
```   
服务依赖 redis，请在启动之前安装 redis 服务   