from PIL import Image, ImageDraw, ImageFont


# 一行多少汉字
lineWordCount = 18
# 行间距
heightBetweenLine = 45


def gen_img(size=None):
    if size is None:
        size = 400
        # 生成大小为400x400RGBA是四通道图像，RGB表示R，G，B三通道，A表示Alpha的色彩空間
    image = Image.new(mode='RGBA', size=(400, 400), color=(255, 55, 55))
    # ImageDraw.Draw 简单平面绘图
    draw_table = ImageDraw.Draw(im=image)
    # 直接显示图片
    image.show()


def pic_open(filepath):
    # 图片打开与显示
    image = Image.open(filepath)
    return image


def get_size(image):
    # 获取图像的宽和高
    width, height = image.size
    return width, heitht


def pic_text(filepath, size, text, setFont, fillColor, filename, direction=None):
    print(filepath, size, text, setFont, fillColor)
    # 打开图片
    image = pic_open(filepath)
    # 新建绘图对象
    draw = ImageDraw.Draw(image)
    # 显示图片
    image.show()

    seq = 1

    while True:
        if seq * lineWordCount >= len(text):
            draw.text((size[0], size[1] + heightBetweenLine * (seq-1)),
                      text[(seq-1)*lineWordCount: len(text)],
                      font=setFont, fill=fillColor, direction=None)
            break
        else:
            draw.text((size[0], size[1] + heightBetweenLine * (seq-1)),
                      text[(seq-1)*lineWordCount: seq * lineWordCount],
                      font=setFont, fill=fillColor, direction=None)

        seq = seq + 1


    image.show()
    # 保存
    pic_save(image, filename)


def pic_save(image, filename):
    # 保存
    image.save(filename)


if __name__ == "__main__":
    size = None
    # gen_img()

    # ** ImageFont模块**
    # 选择文字字体和大小
    setFont = ImageFont.truetype('/System/Library/Fonts/Hiragino Sans GB.ttc', 30)
    # 设置文字颜色
    fillColor = "red"  # 蓝色

    text = "【上交所：本周对短时间内集中申卖加剧股价异动等行为重点监控】财联社7月30日讯，上交所公告，本周沪市共发生拉抬打压、虚假申报等73起证券异常交易行为，上交所对此采取了书面警示等自律监管措施；对短时间内集中申卖加剧股价异常波动等影响市场正常交易秩序、误导投资者交易决策的异常交易行为实施重点监控，依规及时采取自律监管措施。"
    text = text.replace("财联社","")
    text = text.replace("新浪财经", "")
    text = text.replace("腾讯财经", "")
    text = text.replace("东方财富", "")

    if len(text) > lineWordCount *10:
        print("WARNING -- 文本超过10行 展示不友好，请截短掉以下内容----")
        print(text[lineWordCount * 10 : len(text)])
    else:
        size = (106, 302)
        filepath = "/Users/leewow/run/mine/代马数据/代马快讯/model.png"
        filename = "/Users/leewow/run/mine/代马数据/代马快讯/model_test.png"

        # 打开图片
        image = pic_open(filepath)
        # 添加文字
        pic_text(filepath, size, text, setFont, fillColor, filename, direction=None)