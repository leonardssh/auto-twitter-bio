# auto-twitter-bio
☁️ Automatized Twitter biography using openweathermap.org API

Remember to 🌟 this Github if you 💖 it.

## Installation

### [Twitter] Get API Keys and Tokens

There is a lot to explain and it would be a waste of time, you better take a look right here: [how-to-get-twitter-api-key](https://elfsight.com/blog/2020/03/how-to-get-twitter-api-key/)

After you have completed all the steps and obtained the API Keys and Tokens, copy and paste them into your **config.json** file (`consumer_key`, `consumer_secret`, `access_token`, `access_token_secret` fields).

### [OpenWeatherMap] Get your application key

You have to get your **openweathermap.org api key**, to allow your app to get the weather of your favourite city. Register [here](https://openweathermap.org/home/sign_up), then go on [your dashboard](https://home.openweathermap.org/api_keys) to get your key. Copy and paste it in your **config.json** file (`weather` field).

### [Crontab] Run the script every 5 minutes

You have to edit the **crontab table** using `crontab -e`. Then, add the following line to this file:  
```sh
*/5 * * * * cd /path/to/auto-twitter-bio && /usr/bin/python3 /path/to/auto-twitter-bio/main.py >> ~/twitter-cron.log 2>&1
```
This will run the script and update your biography every 5 minutes.

### That's it

Congratulations, you have successfully installed Automatized Twitter Biography. Feel free to open an issue if necessary!

Thanks to **[Androz2091](https://github.com/Androz2091)** for the base code.
