# NFL Inactive Checker

Write a codebase to automatically check for inactivate players and send me a text message.

## Pre-requisite

Install the necessary requirements from the requirements file.  

```bash
pip install -r requirements.txt
```

In order for this to work, the user wuold require a `login_info.json` file under the `src` folder. That folder will be responsible for handling the login to the site. Please use your browser and https://curlconverter.com/ to extract the JSON representation of your site's cookie and headers.

![Alt text](/assets/image.png)


## How to run 

After you have initiated login, run the following command:

```bash
cd src
python main.py
```

It will generate an output similar to this:

```python
{'Questionable': ['Breece Hall RB - NYJ Q ', 'Amari Cooper WR - CLE Q View News '], 'Inactive': [], 'Out': [], 'Injured Reserved': [], 'Doubtful': []}
```

You can use this information to your liking on how to you want to deliver it to yourself. Whether through AWS and any other Cloud hosted platform or even your own server.
Setup a CRON job that run this command every Sunday/Monday/Thursday before the games and relay that information to yourself either through text and/or email. 