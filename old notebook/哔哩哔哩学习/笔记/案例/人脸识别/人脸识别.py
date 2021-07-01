'''
#案例一   识别图片
#1.导入cv2库
import cv2
#2.加载图片
image = cv2.imread('./xxx.png')
#3.创建窗口
cv2.namedwindow('face recognition')
#4.显示图片
cv2.imshow('face recognition',image)
#5.暂停窗口
cv2.waitKey(0)
#6.关闭窗口
cv2.destroyAllWindows()



#案例二   识别图片j基础上添加人脸识别：需要添加模型
#1.导入库
import cv2
#2.加载图片
image = cv2.imread('./xxx.png')
#3.加载人脸模型
cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
#4.调整图片灰度(人脸识别，没必要识别颜色，提高灰度会提升识别性能)
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#5.检查人脸
faces = face.detectMultiScale(gray)
#6.标记人脸
for (x,y,w,h) in faces:
    #四个参数：1.图片  2.坐标原点   3.识别大小   4.颜色   5.线宽
    cv2.rectangle(image, (x + y), (x + w, y + h), (0, 255 , 0), 2)
#7.创建窗口
cv2.nemedwindow('face recognition')
#8.显示图片
cv2.imshow('face recognition',image)
#9.暂停窗口
cv2.waitKey(0)
#10.关闭窗口
cv2.destroyAllWindows()


#案例三   调动摄像头
#1.导入库
import cv2
#2.打开摄像头
capture=cv2.VideoCapture(0)
#3.获取摄像头实时画面
cv2.namedWindow('camera')
while True:
    #3.1 读取摄像头帧画面
    ret,frame = capture.read()
    #3.2 显示图片
    cv2.imshow('camera',frame)
    #3.3 暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
#4.释放资源
capture.release()
#关闭窗口
cv2.destroyAllWindows()
'''

# 案例四   调动摄像头
# 1.导入库
import cv2

# 2.加载模型
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
# 3.打开摄像头
captrue = cv2.VideoCapture(0)
# 4.创建窗口
cv2.namedWindow('camera')

# 5.获取摄像头实时画面
while True:
    # 5.1 读取摄像头帧画面
    ret, frame = captrue.read()

    # 5.2 调整图片灰度
    gary = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # 5.3 检查人脸
    faces = face.detectMultiScale(gary)  # (gary,1.1,3,0,(100,100))
    # 5.4 标记人脸
    for (x, y, w, h) in faces:
        # 四个参数：1.图片  2.坐标原点   3.识别大小   4.颜色   5.线宽
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 5.5 显示图片
    cv2.imshow('camera', frame)
    # 5.6 暂停窗口
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
# 6.释放资源
captrue.release()
# 7.关闭窗口
cv2.destroyAllWindows()
