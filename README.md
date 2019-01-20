# AutoLoginTest
Auto login test engine

1) Create a google app from <a href="https://console.developers.google.com">console</a>. Enable Sheet and Drive APIs. Create credentials with <i>Service Account Key</i>
2) Copy the json config file into your project directory
2) Create two spreadsheets with the names in run.py file
3) Share them with your client email
4) Install requirements.txt
6) Download related biggest sized (security version) chromedriver from <a href="https://launchpad.net/ubuntu/trusty/+package/chromium-chromedriver">here</a>. Manually install it <code>sudo dpkg -i Downloads/chromedriver851831581.deb</code> 
5) Set cron job <br>
<code>11 * * * *  export DISPLAY=:0; /home/pi/.virtualenvs/eksilogin/bin/python /home/pi/Public/eksilogin/run.py > /home/pi/Public/eksilogin/eksilogin.log 2>&1</code>
