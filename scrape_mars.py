




    # coding: utf-8
def scrape():


    import time
    from splinter import Browser
    from bs4 import BeautifulSoup
    import pandas as pd
    mars={}


    # In[2]:


    executable_path={"executable_path":'/usr/local/bin/chromedriver'}
    browser=Browser("chrome",**executable_path,headless=False)
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    news_title =soup.find('div',class_="content_title").get_text()
    news_p=soup.find('div',class_="article_teaser_body").get_text()


    # In[3]:


    


    # ##  NASA Mars News

    # In[4]:


    # Scrape news titles and teaser_body from the website

    news_title =soup.find('div',class_="content_title").get_text()
    new_p=soup.find('div',class_="article_teaser_body").get_text()


    # # Featured Image

    # In[6]:


    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(1)

    browser.click_link_by_partial_text("more info")

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")


    # In[7]:


    image=soup.find('figure',class_="lede")
    image_url=image.find('a')['href']


    featured_image_url="https://www.jpl.nasa.gov"+str(image_url)
    featured_image_url


    # # Mars Weather

    # In[8]:


    executable_path={"executable_path":'/usr/local/bin/chromedriver'}
    browser=Browser("chrome",**executable_path,headless=False)
    url="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")


    # In[9]:


    tweet_text=soup.find('p',class_="tweet-text")
    tweet_text
    mars_weather=tweet_text.get_text()
    mars_weather


    # # Mars Facts

    # In[10]:


    df=pd.read_html("http://space-facts.com/mars/")[0]
    


    # In[11]:


    df.columns=["Description","Facts"]
    


    # In[12]:


    df.set_index('Description',inplace=True)
    


    # In[13]:


    table=df.to_html()
    


    # In[14]:


    table=table.replace("\n","")
    table


    # # Mars Hemispheres

    # In[117]:


    executable_path={"executable_path":'/usr/local/bin/chromedriver'}
    browser=Browser("chrome",**executable_path,headless=False)
    hemi_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)

    time.sleep(1)



    hemi_html = browser.html
    hemi_soup = BeautifulSoup(hemi_html,"html.parser")



    image_title=[]
    image_titles=hemi_soup.find_all('div',class_='description')


    for title in image_titles:
        image_title.append(title.find('h3').text)
    image_title


    image_url=[]
    for i in range(len(image_title)):
        
        
        hemi_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(hemi_url)
        browser.click_link_by_partial_text(image_title[i])
        html_click= browser.html


        soup_click  = BeautifulSoup(html_click, 'html.parser')
        url_click = soup_click.find_all('img', class_= "wide-image")


        image_urls= url_click[0]['src']
        image_url.append(f"https://astrogeology.usgs.gov/{image_urls}")
        
        


    dictionary=dict(zip(image_title,image_url))
    dictionary



    # In[118]:


    hemisphere_image_urls=[]

    for key ,value in dictionary.items():
        hemis_dict={}
        hemis_dict['title']=key
        hemis_dict['img_url']=value
        hemisphere_image_urls.append(hemis_dict)
    hemisphere_image_urls


    # In[ ]:



    mars["facts_table"]=table
    mars["featured_image_url"]=featured_image_url
    mars["mars_weather"]=mars_weather
    mars["news_title"]=news_title
    mars["news_paragraph"]=news_p
    mars["hemisphere_image_urls"]=hemisphere_image_urls

    return mars


