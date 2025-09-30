def test_heroku_title():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    mybrowser = utility.get_browser();
    //mybroswer = webdriver.Firefox()
    mybroswer.get(utility.get_url()) #
    assert 'Internet' in mybroswer.title
    mybroswer.quit()

def test_heroku_heading():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    mybroswer = webdriver.Firefox()
    mybroswer.get('https://the-internet.herokuapp.com/')
    heading = mybroswer.find_element(By.TAG_NAME, 'h1')
    assert 'Welcome' in heading.text
    mybroswer.quit()
        
def test_heroku_subtitle():
    pass
    
def test_heroku_number_of_examples():
    pass