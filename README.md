# FB_crawler
### The project is to practice using python selenium crawler to automatically publish articles and attach pictures in Linux system. When disasters occur, the government often uses mobile phone text messages to warn the public, but as usage habits change, social media is also one of the tools for notifications. It is hoped that in the future it can be used as one of the warning means for the prevention of natural disasters, such as earthquakes, landslides, tsunamis, etc. It should be noted that social software such as Facebook often has security protools to prevent crawlers, so it is still necessary to crawl in social media for justifiable purpose and motivation.

# Installation
* Install selenium module
```
$ pip install selenium
```
* Download and install the browser
```
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
$ sudo yum google-chrome-stable_current_x86_64.rpm
$ google-chrome --version
```
* Download and install the corresponding webdriver (google chrome version 112 in my case)
```
$ wget https://chromedriver.storage.googleapis.com/112.0.5615.49/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ sudo mv chromedriver /usr/local/bin/
$ chromedriver --version
```

# Execution
$ python fb_crawler.py

