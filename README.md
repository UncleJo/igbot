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
* Simply import the library and make and object.
  ```
  import igbot
  bot = igbot(True) #True will not open the browser. False will open the browser.  
  ```
 * Login via and run the Checklist
   ```
   bot.login("username","password")
   bot.pre_checklist()
   ```
### Docuentation
* Coming soon. Gotta make more features
