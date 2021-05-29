from selenium import webdriver

# Using Chrome webdrvier
path = '/Users/Pradhyumn/Downloads/chromedriver'
min_connections = 50
driver = webdriver.Chrome(path)
driver.get('https://www.linkedin.com/login')

# Log into Linkdin
username = driver.find_element_by_id('username')
# Replace '*******' with username 
username.send_keys('*******')
password = driver.find_element_by_id('password')
# Replace '*******' with password 
password.send_keys('*******')
button = driver.find_element_by_tag_name('button')
button.submit()

# Navigate to My Network
network = driver.find_element_by_link_text('My Network')
network.click()
driver.implicitly_wait(10)

# Minimize Messaging box
header = driver.find_element_by_class_name('msg-overlay-bubble-header')
buttons = header.find_elements_by_tag_name('button')
buttons[3].click()

# Send connection requests
try:
    attr = lambda section :section.find_element_by_tag_name('span').text
    find_con_button = lambda section : section.find_element_by_tag_name('footer').find_element_by_tag_name('button')
    sections = driver.find_elements_by_class_name('discover-entity-type-card__bottom-container')
    mutual_con = [attr(section) for section in sections]
    sections = [section for section in sections if ('connections' in attr(section))]
    sections = [section for section in sections if (int(attr(section).split(' ')[0])>= min_connections)]
    mutual_con = [attr(section) for section in sections]
    mutual_con = [int(num.split(' ')[0]) for num in mutual_con]
    connect_buttons = [find_con_button(section) for section in sections]
    [button.click() for button in connect_buttons]
except:
    driver.quit()