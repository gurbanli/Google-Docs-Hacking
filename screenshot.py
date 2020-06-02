import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


changeScroll = """
    followers = document.querySelector('div.kix-appview-editor');
    followers.scrollTo(0, {});
    """
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=chrome_options)
scroll = -30000
count = 1
driver.get("https://docs.google.com/document/d/1fPQ8IXt2XAzZv-NzW7rzyhviFVvCu5KJcBp09dL4Et8/preview")
time.sleep(10)
while scroll <= 173779:
    if scroll == 150000:
        break
    scroll += 30000
    scrolled = changeScroll.format(scroll)
    driver.execute_script(scrolled)
    print(scrolled)
    time.sleep(2)
    if scroll == 150000:
        height = 30000
    else:
        height = 30000
    driver.set_window_size(1920, height)
    time.sleep(2)
    driver.save_screenshot(f"screenshot{count}.png")

    count += 1
driver.quit()
