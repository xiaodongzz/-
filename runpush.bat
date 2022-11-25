@echo off
E:
cd \博士 2021\0 智能家用健康管理机器人 ZXD
git add -A
git commit -m "%date% %time%"
git push -u origin master
echo 数据上传完成！！！ 
pause