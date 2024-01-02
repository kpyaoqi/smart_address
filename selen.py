import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
# 创建Chrome浏览器实例
driver = webdriver.Chrome()
# 打开网页
url = 'https://dune.com/queries/3252037'
driver.get(url)
button_class = "buttonThemes_theme-primary__C0pSI"
button = driver.find_element(By.CLASS_NAME, button_class)
button.click()
#程序打开网页后20秒内手动登陆账户
time.sleep(20)

with open('cookies.txt','w') as cookief:
    #将cookies保存为json格式
    cookief.write(json.dumps(driver.get_cookies()))

driver.add_cookie({'name':'auth-user','value':'yaoqi'})
driver.add_cookie({'name':'auth-refresh','value':'eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.NHaMDTrKJMZNs78JK5k36wTyMTee5W1m7o08aCml9ymOQoYuW36FqWp8RKsxRom7RjCk0vkOqrJZUXpYZ_a3J9-G4-quAajXIbV4BeiaKLyFiYy2s2PLv0ABqS-7-FpHYyIj-MiZQXq7e7Zc3c_jNefRalFmBNy7XmuNo68N-gSmEjICPQrE9cnVVNNd__Nj5pwiQTSv-J6rMWX8WteuaHVVZg1EoErPDo51U9-3h-uiDQDvKAZ-DDudcu8lStCJ2f8JhgLMRU2NPCEU-3zfoVNaUwjAjnuJ1zntetXjOTCKpt3NtRyNxb5Yj1M3lGzlDQMGuxTJ9enEBaXDCfsbWw.HeZhELVkJjRX9pzb.y1x7lOsIuVkTORAUibra8iQ4tzxpcr2pH_x2_j9c2LM1bufIRV9TQYoFGsX7MQpQi8x-hTuXWVkkTF5Rw0Y7GX0ml0gaDRgmD3a4Six8POTEVVFk-ts0vKJdh1LnhiQO8MCYqS7byrfytms1bJfeCd08I-mi8DxWQqskiqSXMU3QE9wcN44zcw3iobU5pwon0akrBUvPdkMmM0nw_7aO6gJeQ_Akjg7nwqcAS0uz_n0rKV1DrPfC0fwoNeRPRuVaEH3NU6hO-rz2ZItXkbBC4H_0G9-PtvTk0OXd-kncB6huIwu-_BhBdW3GHg8CXEAF6dmu0hJ8XPWhUniBmDr8H8tZJH5TsxwpFmP3iOpDS8cHwoCwj5gwmV6B3CUcg_FAk867i9Je1FXAPWWtdwLxrC_pgJ99qaCUleDljXFFdzC1Wr7uHSnLZD0VFsKET9pjxswbaUCA9HEUqdlHHrK38TB2wa2IC0p45WE4JT3mcrtsDcMVEMxdPpMSPzUlXru5EvWmzIKgbE41RCQnTovk-eV2ozWXn7HN6VYXnSYTc97TOv4RErLy_wWMNuz-3XAEoWAF6LYRkK0Mxuwx0l_WkVrjHOF6yCJsxu7qV5T6H8ANkXJWg3gpkun9HuM0T7QjGTldn7viXz8WnQa2ZYoTi40ff_EVnWrEZkYogIQsvlXKcow-js84ViW0Ncm51UC_9rfFPSRteiUK4jI4b-yc79Veb9IBE-kG7sBHUA0syz42UL7Ntn54oONmXzQCFAESeImZA41Ua5o8B5eJnNxoyx0SL3n4hwkag4I1QpGxkpfeVpS83O80NPdWQrLzBFe7g-kTLujoIFMNc8jCXiWzO0FEZVJchnS82_Zqgdt3aPKzsg249reCwsULNDRkpvHhuc1Ypnr3TqNwcUpU8kB72Qc0n1DltGFjBLNSMRNr6umCf27qtrePNzxKR3efl8ctV_NNuWah7erjDdkfts8vlw0p5yqp-Qipw1WqnNSVWsI508JNMLalb9Th_Pl3kqubMVEuTKtWdd07bp-cOsf_x_JdoQk7S708HI2ICn6ht1Tyl5MTmaWheSQReuD_9HPjcGOJOkIzCzNLOXs_jOHExyRj5AjY6ba3b1UnX5Wih8SMR06R_08TjH9eP8fJa_Y_iLsSaMegFLrA9qOcnmh0xrz4lQh1Bq6WJbrdj4mnY1_3AVF60QLoo_OnRZdm_X9reXsQHzIkz7tX3xDOgr9E4ZB73KjdUOrKbRFUsK4FfHE6wgSVY52RwKxgQc8sHa2Q670.-lWTiEZByBbsmXkLix--_g'})
#程序打开网页后20秒内手动登陆账户
time.sleep(30)
# 使用CSS选择器定位带有特定style属性的div元素
style1_value = "height: 22px; top: 154px;"
css1_selector = f'div[style="{style1_value}"] .ace_identifier'
# 查找符合条件的第一个元素
element1 = driver.find_element(By.CSS_SELECTOR, css1_selector)
# 获取元素文本
identifier_text1 = element1.text
# 修改文本内容（这里示例为添加一个后缀），通过执行 JavaScript 来修改
new_text = identifier_text1 + "_modified"
driver.execute_script(f"arguments[0].innerText = '{new_text}';", element1)
print("First ace_identifier in style:", identifier_text1)

# 使用CSS选择器定位带有特定style属性的div元素
style2_value = "height: 22px; top: 198px;"
css2_selector = f'div[style="{style2_value}"] .ace_identifier'
# 查找符合条件的第一个元素
element2 = driver.find_elements(By.CSS_SELECTOR, css2_selector)
if len(element2) == 2:
    identifier_text_second = element2[1]
    print(type(element2))
    print("Second ace_identifier in style:", identifier_text_second.text)
else:
    print("No second ace_identifier element found.")

time.sleep(60)
# 使用class属性定位按钮
button_class = "Button_button__MJ5pb.buttonThemes_button__jfRFC.buttonThemes_theme-tertiary__v7VoN.Button_size-M__fDw4z"
button = driver.find_element(By.CLASS_NAME, button_class)
button.click()

# # 关闭浏览器窗口
# driver.quit()
