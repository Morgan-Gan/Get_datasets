vscode bugs:
(1) 没有python编译环境和运行按键，查看安装的python插件是否失效。 ————》 安装另一个版本，重新开启软件
（2）debug不能调试，是因为.vscode中有lunch.json属于C++调试报错，去掉即可。

################################# 比特大陆：模型量化 ###########################################

## attention Bug

1. 在比特大陆转换 u/bmodel 模型时，配置文件.cfg 中的 batch = 1
2. 在比特大陆平台图片.JPG 不能读出，必须转化成.jpg 读出
3. 在平台上运行算法，模型必须先加密
4. 在比特大陆平台，多个 model 之间的名字不能一样 INT8.model/INT8A.model
5. cv::bmcv::uploadMat(cls_mat_roi); 保存图片才不会出错，针对 mat 对象，需要刷新
6. 在 git 上拖到 Windows 上.so 库会损坏，Windows 上无权限管理。分 2 次拖，Windows 上上传，linux 上修改测试。

公司 git 推送代码：
Hint: To automatically insert Change-Id, install the hook:
remote: gitdir=$(git rev-parse --git-dir); scp -p -P 29418 ganhaiyang@10.100.13.21:hooks/commit-msg ${gitdir}/hooks/
remote: And then amend the commit:
remote: git commit --amend
(1)走读-》Pubulish Edit
(2)添加修改点，测试点-》Commit Message

## 制作 mdb 数据集

convert*imageset --shuffle --resize_height=416 --resize_width=416 / 20210205jingdianmao_val.txt img_lmdb
file:///Z:/common2/%E6%A8%A1%E5%9E%8B%E9%87%8F%E5%8C%96/%E6%A8%A1%E5%9E%8B%E9%87%8F%E5%8C%96*%E6%89%93%E7%94%B5%E8%AF%9D%E6%A8%A1%E5%9E%8B(YOLOV3).html

################################# map 平台测试工具 ###########################################
Z:\common2\AI_Server\test_tool

## 模型发布流程：

1. 模型量化-in8 ——> 模型加密
   模型量化保存（-dump_dist）中间文件：
   calibration_use_pb release --model darknet_model_bmnetd_test_fp32.prototxt --weights darknet_model_bmnetd.fp32umodel --iterations 50 -dump_dist=last.th --bitwidth TO_INT8

模型量化加载（-load_dist)中间文件：
calibration_use_pb release --model darknet_model_bmnetd_test_fp32.prototxt --weights darknet_model_bmnetd.fp32umodel --iterations 1000 -load_dist=last.th --bitwidth TO_INT8

2.  模型路径：\\10.100.11.208\iot\AI 版本发布\算法集成\bit\vehicle\vehicle_V1.2_20210225_encrypt
    发布平台：Bitman
    应用场景：车辆检测相关

修改点：
存在问题：
本地服务器无法正常测试，出现很多 多余的 目标框，设备端验证不存在该问题。
配置文件：见 model_cfg.json
精确度指标：

3.平台端实例
Z:\common2\技术文档\场景文档\确认 OK 4.检测流程
Z:\likeliang\bitmain\bitmain_1209\bmnnsdk2-bm1684_v2.2.0\QK_AI_Box\external\aicore\core\object_detector

5.阈值

################################# 比特大陆测试数据 ###########################################
Z:\ganhaiyang\Alg_Proj\2.2.0_20201117_042200\bmnnsdk2\bmnnsdk2-bm1684_v2.2.0\QK_AI_Box\external\aicore\sample_test\build\sample_object_detector

模型发布：
\\10.100.11.208\iot\AI 版本发布\算法集成\bit\ele_cap_protection_shoes

模型备份：
Z:\common2\模型发布\模型发布-bit\ele_clothes

## ############# hand_smoke#####################################

yolo v4 是 5 层输出的，yolo v3 用三层输出。
Y:\jiadongfeng\AI\darknet_v4
./darknet detector test cfg/smoke.data cfg/smoke_5l_test.cfg backup/smoke/smoke_5l_10500.weights /home/os/window_share/common2/dataset/hand_smoke/test/images -thresh 0.3 -out /home/os/window_share/common2/dataset/hand_smoke/test/images_out/ | tee /home/os/window_share/common2/dataset/hand_smoke/test/smoke.txt

大版本：运行 frameworks：
（1）在 QK_AI_Box 上设置编译器，运行 source build/envsetup.sh
(2) 编译及安装库 make --》 make install 注意：编译大版本不能用 make -j16 编译，报错！
（3）盒子配置：http://192.168.3.13/#/login 用户名/密码：admin 123456

# ################ bitman

1. 测试例子
   Z:\ganhaiyang\Alg_Proj\2.2.0_20201117_042200\bmnnsdk2\bmnnsdk2-bm1684_v2.2.0\examples\YOLOv3_object\cpp_cv_bmcv_bmrt_postprocess\yolov3.cpp
   make -f Makefile.arm
2. AIScene 架构
   AIScene 是接口类。对外提供 AiScene。ComScene 是场景通用类，封装通用操作。
   集成关系：AiScene--->ComScene---->SmokeScene
3. 查看日志（gdb 调试)
   build/envsetup.sh --》export BUILD_DEBUG=no 改为 yes 可定位到具体行号
   （1）关掉服务： sudo systemctl stop AICoreDaemon.service(不用重启)
   （2）打开 root：sudo -i
   （3）设置路径：export LD_LIBRARY_PATH=/system/ai_monitor/lib:$LD_LIBRARY_PATH;export PATH=/system/ai_monitor/bin:$PATH
   （4）gdb ai_system -》r 按 Enter -》bt 按 Enter 到具体的行号

   sample_test 调试：
   （1）gdb --args ./slowfast_test image imgs.txt sf18_pytorch_cpu/compilation.bmodel （--args 运行秩序文件带参数）
   /workspace# bin/x86/bmrt_test --context_dir=context/ -----> fp32model(转 bmodel 生成的文件夹)
   （2）-》r 运行； -》bt 按 Enter 到具体的行号； f 0 查看函数；p i； p inputs[0]
   模型自检：bmrt_test --bmodel=int8model_352/yolov3_f32_officeperson.bmodel -----》模型输入数据全为 0
   bmrt_test --context bmodel_dir
   该命令主要用于对 bmodel 的运行与结果精度比对。其中 bmodel_dir 应包含 compilation.bmodel(转换后的 bmodel)，io_info.dat(模型的输入输出信息)，input_ref_data.dat(模型的输入数据)，output_ref_data.dat(模型的输出参考数据)
   如果 bmoodel_dir 不包含输入与输出数据，可以加--compare=0 或者用如下命令
   bmrt_test --bmodel xxx.bmodel

4. log 文件中建立.debug 文件，不会下载模型，要删除
   /data/ai_monitor/log
   /data/ai_monitor/simulate/video/channels 删除视频

5. 问题反馈
   \\10.100.11.208\iot\比特大陆\问题汇总

6. 刷新的 SDK 版本
   （1）参考文件 1：\\10.100.11.208\PUB_Tool\360OS 系统框架组文档目录\XT_IOTOS\BitMain\360OS\制作全量 SD 卡升级软件与 OTA 升级包
   制作全量 SD 卡升级软件与 OTA 升级包流程.html

（2）参考文件 2：\\10.100.11.208\PUB_Tool\360OS 系统框架组文档目录\XT_IOTOS\BitMain\360OS
BitMain 环境搭建.html
