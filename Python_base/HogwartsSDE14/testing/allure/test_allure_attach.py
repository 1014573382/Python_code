import allure 

def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段HTML body块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("E:\photos\1.jpg", name="这是一个图片", attachment_type=allure.attachment_type.JPG)

def test_attach_vedio():
    allure.attach.file("E:\photos\1.mp4", name="这是一个视频", attachment_type=allure.attachment_type.MP4)