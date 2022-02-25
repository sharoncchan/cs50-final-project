# Address Book Web Application
#### Video Demo:  https://www.youtube.com/watch?v=aqMAvZ_veL0

# CS50 Final Project - Address Book Web Application

My project is an address book web application which provides a platform for users to store their contacts details such as the name, address, email and phone number.

Technologies used:

- Frontend
 - HTML
 - CSS
 - Javascript
 - Bootstrap

- Backend
 - Flask (Python)
 - Sqlite3

## How does the webpage works?

The user can register for an account. During registration the user need to enter these fields:

- Name
- Password: There are certain requirements to be fulfilled and the text below indicate the live view of which conditions are fulfilled
- Password(again): User to retype the password. This re-typed password will be matched with the password
- email

After the user has registered for an account and has successfully logged in, the user can accss the homepage which shows the contacts in their address book and details. They can search for the name by using the search button and the table will dsiplay the details of the name accordingly

### Sessions

The webpage uses sessions to confirm that user is registered.

### Database

Database stores all users details and the conatcts of each users


Each of the files contains:

**Static:**
- `styles.css` - the styling for the webpage

**Templates:**
- `apology.html` - html page to render the apology when user input is incorrect/ not accepted
- `contact.html` - html page to render the details when user clicks on the contact link
- `index.html` - html page to render the homepage when user successfully log in
- `layout.html` - html page which renders the layout of the web application which other html pages will extend from
- `login.html` - html page to render the page for user to log in
- `new.html` - html page to render the page for user to add new contacts in their address book
- `register.html` - html page to render the page for user to register for an account


**Main file**:
- `application.py` - the main code for the controller of the web application
- `addressbook.db` - the database to store the details of the users and contacts
- `helpers.py`- functions which are imported into application.py