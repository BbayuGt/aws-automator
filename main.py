from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Login detail (put your email and password here)
useremail = ""
userpw = ""
#instance id, make it ["id1", "id2"] if you need more than 1 instance
instanceid = ["i-0c496c7d304c44428"]
#interval (in second) [Default 60 * 60 (1 hour)]
interval = 60 * 30

while 1:
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	import platform
	if platform.system() == "Linux":
		print("Linux detected!")
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument("--remote-debugging-port=9222")
	
	# Optional argument, if not specified will search path.
	driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
	
	driver.get("https://www.awseducate.com/signin/SiteLogin")
	
	# Login
	username = driver.find_element_by_name(
	    "loginPage:siteLogin:loginComponent:loginForm:username")
	password = driver.find_element_by_name(
	    "loginPage:siteLogin:loginComponent:loginForm:password")
	
	username.send_keys(useremail)
	password.send_keys(userpw)
	driver.find_element_by_class_name("loginText").click()
	
	# goto aws vocareum
	while 1:
	    try:
	        driver.find_element_by_link_text("AWS Account").click()
	        break
	    except:
	        print("wait")
	
	while 1:
	    try:
	        driver.find_element_by_link_text("AWS Educate Starter Account").click()
	        break
	    except:
	        print("wait")
	
	# Move to new tab
	driver.switch_to.window(driver.window_handles[1])
	
	# opennaws
	while 1:
	    try:
	        driver.find_element_by_id("awsbtn").click()
	        break
	    except:
	        print("wait")
	
	
	# Move to new tab
	time.sleep(5)
	driver.switch_to.window(driver.window_handles[2])
	
	#Loop to other id
	for x in instanceid:
	
		# open ec2 link
		while 1:
		    try:
		        driver.get(
		            "https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#InstanceDetails:instanceId="+x)
		        break
		    except:
		        print("wait")
		
		#click start if stopped
		driver.switch_to.frame("compute-react-frame")
		element = WebDriverWait(driver  , 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'awsui-button-dropdown-container')))
		driver.find_elements_by_class_name("awsui-button")[3].click()
		try:
			driver.find_elements_by_class_name("awsui-button-dropdown-item")[1].click()
			print(f"{x} is now UP!")
		except:
			print(f"{x} is still UP!")
	
	print(f"All Done! Closing browser to free up RAM!")
	print(f"Will try again in {interval} Second!")
	driver.quit()
	time.sleep(interval)
 