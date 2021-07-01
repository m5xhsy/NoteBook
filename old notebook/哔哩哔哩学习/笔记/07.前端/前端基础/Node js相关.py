#1 安装Node js         自带npm
#2 初始化 npm init      用npm init --yes直接生成package.json
'''
A:\aaa>npm init
package name: (aaa)                         项目名字是否为aaa
version: (1.0.0)                            依赖版本是否为1.0.0修改的话直接写比如version: (1.0.0)1.0.1回车
description:                                描述
entry point: (index.js)                     项目入口文件是否为index.js
test command:                               测试（过）
git repository:                             git（过）
keywords:                                   关键字（模糊查询）
author:                                     作者
license: (ISC)                              认证证书
About to write to A:\aaa\package.json:      在文件夹里面生成package.json
{
  "name": "aaa",
  "version": "1.0.0",
  "description": "sd",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
'''
安装命令 npm install bootstrap -S 或者npm install bootstrap --save
卸载命令 npm uninstall bootstrap -S



GitHub的包安装 npm install
打包  npm run build
运行服务器 npm run dev