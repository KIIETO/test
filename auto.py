from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
# 打开登录页面
driver.get('http://localhost:8080/books_msg/login.html')

# 等待页面加载
time.sleep(2)







time.sleep(1)
# 查找登录按钮并点击
login_button = driver.find_element(By.CLASS_NAME, 'layui-btn-normal')
login_button.click()


time.sleep(2)
input("按回车键继续...")

driver.quit()
