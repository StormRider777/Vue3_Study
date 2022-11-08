# Win7 32位旗舰版安装node.js vue3 @vue/cli5
## 1.安装 node.js 12.22版本,13以上版本不能正常安装@vue/cli,14以上版本系统最低要求win8
## 2.下载的node.js
### 历史版本:https://nodejs.org/zh-cn/download/releases/ ,选择12.22.12,
### 这个版本能安装vue3及脚手架,
### 下载node-v12.22.12-win-x86.zip,解压,不必setup,在c: 建立 Node_JS文件夹,将解压文件放进该目录下.  
## 3.配置npm: 
### Node_JS文件夹下创建  node_cache  node_global文件
### 设置全局包目录:
### npm config set prefix “c:\Node_JS\node_global” 
### 设置缓存目录
### npm config set cache “c:\Node_JS\node_cache”  
### 设置淘宝 安装包镜像:
### npm config set registry https://registry.npm.taobao.org
### 查看配置文件:
#### Npm config ls
### 查看node 版本
#### node –v
### 查看npm 版本
####   npm –v
### 配置文件在用户文档夹内 搜索 .npmrc
## 4.安装vue3
### Npm install –g vue
### 安装 @vue/cli
### npm install –g @vue/cli
### 查看vue的版本: npm info vue
### 查看@vue/cli 版本 vue -V  或 vue –version
## 5.使用脚手架创建 vue3项目:
### 在cmd 中 切换到 F:盘,或其他盘,不要在C:盘
### Vue create vue3_study 
### 在f:盘下 生成了 vue3_study项目 ,npm run serve 看看是否正常启动.

## 6.Github: 
### https://github.com/StormRider777/Vue3_Study.git 
# vue3_study



