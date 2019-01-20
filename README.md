# AutoLoginTest
Auto login test engine

1) Create a google app from <a href="https://console.developers.google.com">console</a>. Enable Sheet and Drive APIs. Create credentials with <i>Service Account Key</i>
2) Copy the json config file into your project directory
2) Create two spreadsheets
3) Share them with your client email
4) Install requirements.txt
5) Set cron job
<code>11 * * * *  export DISPLAY=:0; /home/pi/.virtualenvs/eksilogin/bin/python /home/pi/Public/eksilogin/run.py > /home/pi/Public/eksilogin/eksilogin.log 2>&1</code>
