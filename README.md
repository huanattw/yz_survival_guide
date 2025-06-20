# YZ survival guide

## 點名機器人
### 準備工作
一台手機,安裝 [proxypin](https://github.com/wanghongenpin/proxypin/blob/main/README_CN.md) 或是習慣的抓包軟體
> 記得一定要在手機抓，電腦抓不到
> 只能抓 app 的 token 網頁版沒用
### 抓包教學
1. 先開起抓包，登入元智app
2. 找到 post https://portalx.yzu.edu.tw/NewPortal/api/Auth/CheckUserToken 的這筆封包，點下去。
3. 進到 Request，就可以找到 Token，並且去 https://www.urlencoder.org 進行編碼
5. 把第13行的 YOUR_TOKEN 換成剛剛找到的 token，把85行改成館別(程式碼在 check.py)

## 科技選課
可以參考 [這個 repo](https://github.com/Doem/yzuCourseBot)

