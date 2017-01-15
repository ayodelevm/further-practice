from selenium import webdriver
import time

cdriver = webdriver.Chrome(executable_path="C:\Chromedriver\chromedriver.exe")

url = 'http://tvshows4mobile.com/Scorpion'

cdriver.get(url)

old_new = cdriver.find_element_by_xpath('/html/body/div/div[9]/a[1]')
old_new.click()

all_season = cdriver.find_elements_by_partial_link_text('Season 0')

for a in all_season:
    a.click()
    time.sleep(5)
    
    old_new = cdriver.find_element_by_xpath('/html/body/div/div[9]/a[1]')
    old_new.click()
    
    episode_result = cdriver.find_element_by_xpath('/html/body/div/div[7]/div[4]/div[2]/div[2]')
    episode_result_num = int(episode_result.get_attribute("textContent"))
    page_num =(int(episode_result_num/10)) + 1

    url = cdriver.current_url

    for page in range(1, page_num+1):
        new_url = url + 'page{0}'.format(page)
        
        episode_list_string = cdriver.find_element_by_class_name('page_desc')
        episode_list_result = episode_list_string.get_attribute("textContent")
        episode_list_var = str(episode_list_result)
        episode_list = episode_list_var.split()
        episode_num1 = int(episode_list[1])
        episode_num2 = int(episode_list[3])
        
        
        div_nums = [1,2,3,5,6,7,9,10,11,13]
        for episode in range(episode_num1-1, episode_num2):
            anchor_uri = '/html/body/div/div[12]/div[' + str(div_nums[episode]) + ']/a'
            all_episode = cdriver.find_element_by_xpath(anchor_uri.format(episode))
            all_episode.click()
            time.sleep(3)

            mp4_link = cdriver.find_element_by_partial_link_text('.mp4')
            mp4_link.click()

            time.sleep(5)


            cdriver.execute_script("window.history.go(-1)")

            
        cdriver.get(new_url)
    
else:
    time.sleep(1000)
    cdriver.quit()




  
