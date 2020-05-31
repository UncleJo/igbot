# IGBot

### Installation
* IGBot pip package
  ```
  pip install igbot
  ```
* [Download Geckodriver for Mozilla Firefox ](https://github.com/mozilla/geckodriver/releases)and move it to /usr/local/bin using the command below. (Note - Geckodriver is just a single file named 'Geckodriver')
  ```
  sudo mv geckodriver /usr/local/bin
  ```
### Usage
* Simply import the library and make an object.
  ```
  import igbot
  bot = igbot(True) #True will not open the browser. False will open the browser.  
  ```
 * Login via and run the Checklist
   ```
   bot.login("username","password")
   bot.pre_checklist()
   ```
### Features
* Login/Logout (v0.1)
* DM a person (v0.1.2)
* Follow/Unfollow a person (v0.1.3)
* Fetch Followers and Following list (v0.2.1)
* Follow Mass Users Over Time (Coming Soon)
* Like and Comment Module (Coming Soon)

### Documentation
* Coming soon. Gotta make more features
