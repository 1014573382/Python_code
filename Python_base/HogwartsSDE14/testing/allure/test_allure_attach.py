import allure 

# 在测试报告中插入指定文本，图片或视频

def test_attach_text():
    # 没有name,则会默认生成一个随机字符串当做名字：be155526-09c1-4efd-91ec-ca9ae3061c39-attachment.txt
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段HTML body块</body>", "html测试块", allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file(r"E:\Picture\petimg\01.jpg", name="这是一个图片", attachment_type=allure.attachment_type.JPG)

# def test_attach_vedio():
#     allure.attach.file("E:\photos\1.mp4", name="这是一个视频", attachment_type=allure.attachment_type.MP4)