# AutoLoginTest
Auto login test engine

1) Create a google app from <a href="https://console.developers.google.com">console</a>. 
2) Create a new project
<img src="https://i.imgur.com/dbL1sdr.jpg">

3) Enable Sheet and Drive APIs. Create credentials with <i>Service Account Key</i>
<img src="https://i.imgur.com/zg0bPHp.png">

4) Created service account needs at least "editor" permission to add rows to the spreadsheet
<img src="https://i.imgur.com/hv87jYm.png">

5) Copy the json config file into your project directory
6) Create two spreadsheets with the names in run.py file
7) Share them with your client email
8) Install requirements.txt
9) Download related biggest sized (security version) chromedriver from <a href="https://launchpad.net/ubuntu/trusty/+package/chromium-chromedriver">here</a>. Manually install it <code>sudo dpkg -i Downloads/chromedriver851831581.deb</code> 
10) Set cron job <br>
<code>11 * * * *  export DISPLAY=:0; /home/pi/.virtualenvs/eksilogin/bin/python /home/pi/Public/eksilogin/run.py > /home/pi/Public/eksilogin/eksilogin.log 2>&1</code>
Note: Display=:0 is necessary for run webdriver with headless mode in crontab.
