
def get_valid_img(request):
    ###### 方法一
    # with open('static/image/image.png','rb') as f:
    #     data = f.read()

    ###### 方法二
    # from PIL import Image
    # image = Image.new('RGB',(100,30),'red')       #(125,255,255)
    # f = open('static/image/valid.png','wb')
    # image.save(f,'png')
    # with open('static/image/valid.png', 'rb') as f:
    #     data = f.read()

    ###### 方法三
    # from PIL import Image
    # from io import BytesIO  #磁盘内存
    # image = Image.new('RGB',(100,30),'red')
    # f = BytesIO()     #内存句柄
    # image.save(f,'png')
    # data = f.getvalue()


    ###### 方法四
    # from PIL import Image,ImageDraw,ImageFont
    # from io import BytesIO  # 磁盘内存
    # image = Image.new('RGB', (100, 30), 'red')
    # draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype('/static/font/simkai.ttf',26)
    # draw.text((17,2),'aSbD2',(0,255,255),font=font)
    # f = BytesIO()  # 内存句柄
    # image.save(f, 'png')
    # data = f.getvalue()

    ######方法五
    from PIL import Image, ImageDraw, ImageFont
    from io import BytesIO  # 磁盘内存
    import random
    lit_str = []
    valid = ''

    for i in range(2):
        num = str(random.randint(0,9))
        str_upper = chr(random.randint(65,90))
        str_lower = chr(random.randint(97,122))
        lit_str.append(num)
        lit_str.append(str_lower)
        lit_str.append(str_upper)
    random.shuffle(lit_str)
    for i in lit_str:
        valid += i
    print(valid)
    request.session['valid'] = valid
    width = 100
    height = 35
    img = Image.new('RGB', (width, height), (0, 150, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/static/font/simkai.ttf', 26)    #定义字体和大小
    draw.text((10, 4), valid, (0, 255, 255), font=font)         #定义起始位置，验证码，颜色，字体
    for i in range(5):          #添加线
        x1 = random.randint(0,width)
        x2 = random.randint(0,width)
        y1 = random.randint(0,height)
        y2 = random.randint(0,height)
        draw.line((x1,x2,y1,y2),fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    for i in range(80):         #加躁点
        draw.point([random.randint(0,width),random.randint(0,height)],fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        x = random.randint(0,width)
        y = random.randint(0,height)
        draw.arc((x,y,x+4,y+4),0,90,fill = (random.randint(0,255),random.randint(0,255),random.randint(0,255)))


    f = BytesIO()  # 内存句柄
    img.save(f, 'png')
    data = f.getvalue()
    return HttpResponse(data)


#验证码的保存用session


#html中切换验证码
$('#image').click(function () {
                $('#image')[0].src += "?";
                {#$('#image')[0].src = "http://127.0.0.1:8000/app/get_valid_img/"#}
            })

