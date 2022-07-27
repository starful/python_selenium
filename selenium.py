from selenium import webdriver
import chromedriver_binary
import time
import concurrent.futures

# pip install selenium
# pip install chromedriver-binary==84.0.4147.135

def driverfunc(order,count):
	# count = 1
	options = webdriver.ChromeOptions()
	driver = webdriver.Chrome(chrome_options=options)
	driver.get('http://art-alb-1230944688.ap-northeast-1.elb.amazonaws.com/#/cmn0060')
	time.sleep(2)


	id = driver.find_element_by_xpath("/html/body/app-root/app-cmn0060/div/div[2]/form/input[1]")
	id.send_keys("Test15" + str(count))
	password = driver.find_element_by_xpath("/html/body/app-root/app-cmn0060/div/div[2]/form/input[2]")
	password.send_keys("Test001")

	time.sleep(1)

	# ログインボタンをクリック
	login_button = driver.find_element_by_xpath("/html/body/app-root/app-cmn0060/div/div[2]/form/button")
	login_button.click()

	time.sleep(2)
	# サイト内で他の画面に遷移させたければ
	# driver.get('画面遷移させたいURL')

	logout_button = driver.find_element_by_xpath("/html/body/app-root/app-mainpage/main/div/header/app-cmn0010/div/div/div/div/a/button")
	logout_button.click()
	driver.close()
	# count = count + 1

# 並列実行するテストケースの配列
# このサンプルはあくまでも書き方サンプルなのでデータは適当
testcase = [1,2,3,4,5,6,7,8,9,10]

# 並列実行するexecutorを用意する。
# max_workers が最大の並列実行数
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
count = 1
for t in testcase:
    executor.submit(driverfunc,t,count)
    count = count + 1