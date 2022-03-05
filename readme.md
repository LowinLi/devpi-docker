# docker启devpi服务

## 简要
+ [devpi工具](https://devpi.net/docs/devpi/devpi/stable/%2Bd/index.html)相比其他pypi源工具，有如下特点：
  1. **节省硬盘**：不必完全同步下来公开源的所有包，仅在第一次pip安装时从公开源下载和缓存。
  2. **支持上传接口文档**：上传自己开发pip库时，可以把接口文档也上传到devpi。

+ 本项目旨在用docker容器启动devpi服务。

## 快速开始
+ docker run 方式

```bash
docker run -d --name devpi-lib -p 7104:7104  --env DEVPISERVER_HOST=0.0.0.0 --env DEVPISERVER_PORT=7104 --env DEVPISERVER_ROOT_PASSWORD=password --env DEVPISERVER_USER=lowinli --env DEVPISERVER_PASSWORD=password --env DEVPISERVER_MIRROR_INDEX=pypi --env DEVPISERVER_LIB_INDEX=devpi --env SOURCE_MIRROR_URL=https://pypi.douban.com/simple --restart always --volume volume:/var/lib/devpi lowinli98/devpi:v0.1
```

+ docker-compose 方式

```yaml
version: "2.3"
services:
  devpi-lib:
    container_name: devpi-lib
    image: lowinli98/devpi:v0.1
    expose:
      - 7104
    ports:
      - "7104:7104"
    environment:
      - DEVPISERVER_HOST=0.0.0.0
      - DEVPISERVER_PORT=7104
      - DEVPISERVER_ROOT_PASSWORD=password
      - DEVPISERVER_USER=lowinli
      - DEVPISERVER_PASSWORD=password
      - DEVPISERVER_MIRROR_INDEX=pypi                    # 指定镜像index
      - DEVPISERVER_LIB_INDEX=devpi                      # 指定上传index
      - SOURCE_MIRROR_URL=https://pypi.douban.com/simple # 指定镜像源
    restart: always
    volumes:
      - ./volume:/var/lib/devpi

```

+ 访问devpi
http://0.0.0.0:7104

## 镜像构建目录
[./docker](./docker)

## 打包pip包上传示例目录
[./examples/upload-demo](./examples/upload-demo)

## 本项目特点

1. 可以自由指定MIRROR源，尤其配置大陆pypi源可以提高搜索和下载速度，环境变量：`SOURCE_MIRROR_URL`
2. 通过索引继承方式，对MIRROR的index`DEVPISERVER_MIRROR_INDEX`和个人上传pip库的index`DEVPISERVER_LIB_INDEX`进行统一地址管理
3. 使用了[devpi-semantic-ui](https://github.com/apihackers/devpi-semantic-ui)页面，可以更好的展示pypi库的版本信息、接口文档
4. 在`examples/upload-demo`目录介绍一个例子，打包pip库、`sphnix`生成接口文档，并上传到devpi服务。

## 截图

![](./pics/1.png)

![](./pics/2.png)

![](./pics/3.png)