# **Testing**

## **User Stories**
I tested the user stories based on the users outlined in the User Stories section of my README.md file.

1. **User 1** - I am the owner of the website, I want to promote the user of my protein powder supplement in recipes, to sell more of my product.

	This user promotes their protein powder supplement in several ways. Firstly, on the home page when the user arrives at the website, the first thing they see if a carousel displaying a selection of images that clearly show and promote this user’s product. At the bottom of every page is a header asking website users “Do you need whey protein?” and a button below that provides a quick and easy link to this user’s shop selling where customers can buy the protein powder.

2. **User 2** - I am a dietician wanting to share my healthy, nutritionally-balanced recipes with other people.

	This user can achieve their goal by firstly creating an account via the registration page and then selecting the ‘Add recipe’ tab where they will find the form to upload their own recipes. The form includes method, ingredients as well as calories and macronutrient (protein, carbohydrate and fat) information to show that the recipes are nutritionally-balanced. By clicking the ‘Add recipe’ button, this user shares their recipe with other people to achieve their goal.

3. **User 3** - I am new to cooking, I want to find healthy recipes with simple, easy cooking instructions, so I can learn to cook my own meals.

	This user can achieve their goal by selecting the ‘Recipes’ tab on the navbar or clicking the ‘Find recipes’ button on the home page, which will take them to the recipes page. This user can then search for recipes by name or description. To easily identify simple and easy recipes, the utensils icon provides quick visual feedback that it is an easy recipe. A tooltip stating “Quick & easy recipe” further helps this user to identify simple recipes suitable for them as a new cook.

4. **User 4** - I am a bodybuilder, I want to find recipes, to cook meals that fit my calorie and macronutrient needs.

	This user can find recipes via selecting the ‘Recipes’ tab on the navbar or clicking the ‘Find recipes’ button on the home page, which will take them to the recipes page. This user can then click on a recipe (which they are prompted to do by the dropdown arrow symbol) which displays further information on the recipe, including the calorie and macronutrient (protein, carbohydrate & fat) information that this user wants.

5. **User 5** - I am a user who has submitted a recipe, I have since improved my recipe and want to update the recipe to improve it.

	This user can achieve their goal by firstly logging in to their account, which takes them to their profile page.  This user can then click the ‘Recipes’ button in their profile page or the ‘Recipes’ tab on the navbar. On the recipes page, this user will see a ‘Delete’ and an ‘Edit’ button next to the recipes that they have added. This user can select the ‘Edit’ button and make their desired changes. They can then either press the ‘Cancel’ button to discard their changes or click the ‘Edit recipe’ button to make their changes.

## **HTML Validation**
I passed all my html code through the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input).

On all .html pages I had validation errors of: "Bad value" relating to my use of {{ url_for}} internal links for Python. These errors were to be expected as the html validator was not expecting to find these in html code. I therefore left the code the same and these errors still exist.

![url-for-error](https://user-images.githubusercontent.com/74603013/121496716-a2686d80-c9d2-11eb-9293-d15cea8cf930.png)

![HTML Validator errors](https://user-images.githubusercontent.com/74603013/121495128-43eebf80-c9d1-11eb-8051-f7d91e6eda2d.png)

I also had errors of: "Text not allowed in element ul in this context." This error related to the use of Jinja templating and is needed to determine which navbar tabs are displayed according to whether or not the user is logged into their account. I therefore chose to keep the code the same and these errors still exist.


![li-error](https://user-images.githubusercontent.com/74603013/121496243-2e2dca00-c9d2-11eb-852c-e25f6f3e368a.png)

On all .html pages except for the base.html page I had errors relating to the lack of declaring the lang, doctype and header elements. This is because these pages were extending from the base.html template. I therefore chose not to change my code and these errors still exist, but are to be expected.


![extending-from-base-template-error](https://user-images.githubusercontent.com/74603013/121497369-481bdc80-c9d3-11eb-8680-0b7ffa44191f.png)


1. **base.html**
	* I was shown a warning of: "unclosed element div". This related to a missing </div> tag in the footer that I added to fix this error.
	* I was shown another warning of: "unclosed element div" and in the same section of code an error of: "stray end tag nav" and an error of: "end tag seen, but there were open elements". When I checked my code, I had put the closing </nav> and </div> in the incorrect positions and order. I corrected this code and the errors were fixed.

2. **index.html**
	* I was shown errors of: "An img element must have an alt attribute, except under certain conditions." for all my carousel images as I had forgotten to add an alt tag. I corrected these errors by adding alt tags to describe each of my carousel images.

3. **add_recipe.html**
	* I was shown errors of: "No space between attributes." These related to the sttributes in my form input fields. I added the necessary space between these attributes and this resolved these errors.
	* I was shown an error of: Attribute pattern not allowed on element textarea at this point. This related to my calories field where I had tried to restrict the user input to only numeric values. This error was caused because I had used a textinput that didn't support the pattern attribute. I changed this to an input instead of text area and this corrected the issue. I also manually tested this by trying to enter letters into the form and a red error was displayed. I then updated the recipe protein, carbohydrate and fat fields to an input text also, and applied the password attribute to reestrict these fields to numeric values only as well.
	* I also had errors of: "Text not allowed in element select in this context." This error related to the use of Jinja templating and is needed to display the recipe category options for the user to select from. I therefore chose to keep the code the same and these errors still exist.

	![select error](https://user-images.githubusercontent.com/74603013/121500693-73ec9180-c9d6-11eb-9a16-b20681953a90.png)

4. **edit_recipe.html**
	* I was shown errors of: "No space between attributes." These related to the sttributes in my form input fields. I added the necessary space between these attributes and this resolved these errors.
	* I also had errors of: "Text not allowed in element select in this context." This error related to the use of Jinja templating and is needed to display the recipe category options for the user to select from. I therefore chose to keep the code the same and these errors still exist.
	* I also had errors relating to: "label element with multiple labelable descendants" and "Duplicate ID is_easy" this was because I have two options for the is_easy, depending on whether or not the is_easy toggle was on or off in the original recipe in the database. As only one of these options will be correct, this will not be a problem. I proved this by deleting on of the options from the code in the validator and then re-running the checks and the errors were gone. However, as this option is needed, I have left my code and so the errors still exist.

	![is_easy error](https://user-images.githubusercontent.com/74603013/121505159-8072e900-c9da-11eb-863e-6947a1ebe452.png)

4. **login.html**
	* No further errors found (except the common ones across all .html pages as explained above).

5. **profile.html**
	* I was shown errors of: "An img element must have an alt attribute, except under certain conditions." for all my image card images as I had forgotten to add an alt tag. I corrected these errors by adding alt tags to describe each of my image card images.

6. **recipes.html**
	* No further errors found (except the common ones across all .html pages as explained above).

7. **register.html**
	* No further errors found (except the common ones across all .html pages as explained above).

## **CSS Validation**
I passed my css code from style.css through the [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input). No errors were found.

## **Javascript Validation**
I passed my javascript code from script.js through [JSHint](https://jshint.com/).
	 * There were no errors, but I was shown two warnings:
        1. Both warnings related to 'Eversion 6'. I researched this and found this [post](https://stackoverflow.com/questions/37247474/es6-in-jshint-jshintrc-has-esversion-but-still-getting-warning-using-atom) giving this comment /*jshint esversion: 6 */ to add to the top of the javascript code to reswolve the warnings. I added this comment at the top of my js code and the warnings disappeared.

## **PEP8 Validation**
I passed my Python code from app.py and env.py through [PEP8 Online](http://pep8online.com/).

1. **app.py**
	* The following errors and warnings were found:

![PEP 8 results app py](https://user-images.githubusercontent.com/74603013/121512987-3d1c7880-c9e2-11eb-81d7-a81652419834.png)

I corrected these errors and the PEP8 test passed.

![PEP8 success](https://user-images.githubusercontent.com/74603013/121515059-a3a29600-c9e4-11eb-9af2-a6acfbe3a2dd.png)

2. **env.py**
	* I was shown the following warning:

![PEP8 env py](https://user-images.githubusercontent.com/74603013/121515681-5d9a0200-c9e5-11eb-9b42-375578dc1848.png)

However, even splitting the line onto a seperate line, the password was still too long to be PEP8 compliant. I therefore chose to not edit my code as this password is needed to access the MONGO_URI.

## **Manual Testing of features**
The following manual tests were carried out on Microsoft Edge, Google Chrome and Mozilla Firefox:
* Social media links were clicked on to make sure that they open in a new tab at the correct corresponding landing page.
* Navbar items were clicked on from each page to make sure that they navigate to the correct page.
* All buttons and links were clicked on to check that they take the user to the correct page.
* Clicking on the Whey Too Tasty logo in the navbar returns the user back to the home page.
* Checked the mouse cursor changed from an arrow to a pointed finger when the user could click/swipe on an item like buttons, links, image carousel, collapsible accordian etc.

### **Testing the image carousel**
* I tested to makesure the user could see the outline of other images to prompt them to click/swipe to see the full carousel. I then made sure that they could click/swipe to rotate through the 5 images.


![image carousel](https://user-images.githubusercontent.com/74603013/121683992-04e66a00-cab6-11eb-9e69-00be80fa8a60.png)

### **Testing the collapsible accordian**
* I first checked that the header of the collapsible contained the recipe name, recipe description, 'is easy' utensils icon (if this had been turned on when adding the recipe) and the dropdown arrow with background styling.

![accordian headers](https://user-images.githubusercontent.com/74603013/121685005-54796580-cab7-11eb-97ad-6651a4eba9b3.png)

* I then checked that the that the tool tip reading: "quick & easy recipe" was displayed when the user hovered over the utensils icon on recipes with this displayed.

![tooltip](https://user-images.githubusercontent.com/74603013/121685258-9e624b80-cab7-11eb-98b4-26f7cc6d3a2e.png)

* I then checked that the collapsible expanded to display the rest of the recipe information when the relevant recipe header was clicked on. I also made sure that this information was displayed with the correct formatting as planned, for example with spaces between the paragraphs and bold text for the ingredients and method.

![expanded collapsible](https://user-images.githubusercontent.com/74603013/121685575-0153e280-cab8-11eb-92f1-770d199b8b0c.png)

### **Testing the search bar functionality**
* I first checked that the search bar was displaying as intended with the orange search icon, placeholder 'search recipes' text and a green 'reset' button and orange 'search' button.

![search bar](https://user-images.githubusercontent.com/74603013/121685914-6dcee180-cab8-11eb-948d-41c6bac7784d.png)

* I then performed a search for 'smoothie', by typing 'smoothie' into the search bar and clicking the 'search' button and checking that only recipes containing the word smoothie in the name or description were displayed to the user.

![smoothie search](https://user-images.githubusercontent.com/74603013/121686154-bab2b800-cab8-11eb-88a2-894c83ad7892.png)

* I then clicked the reset button to test that I was returned to the recipes page and that all the recipes were displayed.

![reset search](https://user-images.githubusercontent.com/74603013/121686327-ecc41a00-cab8-11eb-8529-5606c1775ce9.png)

* I then tried to perform a search without having entered any text into the search bar. As expected, the search was not performed and a prompt to complete the field was displayed to the user as well as a red line to further indicate a problem.

![empty search error](https://user-images.githubusercontent.com/74603013/121689467-8a6d1880-cabc-11eb-9b55-5adc4f9beb2d.png)

* I then performed a search for something that I knew was not in the recipe database. I entered the word 'hello' and clicked the 'search' button. I could then confirm that a message was displayed telling the user "No results found". This text is displayed in a red colour to provide a further visual indication of a problem.

![no search results](https://user-images.githubusercontent.com/74603013/121689633-c30cf200-cabc-11eb-8083-fdbcfbb6eea1.png)

### **Testing the edit recipe form**
* Firstly I logged in as a user who had added recipes to the database. I then navigated to the recipes page and ensured that I could see 'edit' and 'delete' buttons in the collapsible accordian header, but only on the recipes that I had added and not on all recipes. 


![edit my recipes](https://user-images.githubusercontent.com/74603013/121690210-770e7d00-cabd-11eb-954a-fff530856608.png)

* I then clicked on the edit button to ensure that I was taken to the 'Edit recipe' form. I also checked that this form was displaying as intended with the category selection menu, had retrieved the information from the original recipe and was displaying these correctly in each form input field, had ornage coloured icons next to the full wdith form fields and a clickable 'edit recipe' button or cancel button both with icons.

![edit recipe form](https://user-images.githubusercontent.com/74603013/121690579-eedca780-cabd-11eb-92cd-b3d71efbada9.png)

* I then clicked the 'cancel' button to confirm that I was returned to the recipe page.
* I then reclicked the'edit' button to re-access the 'edit recipe' form. I made sure that I could select options from the recipe category dropdown.

![edit category selection](https://user-images.githubusercontent.com/74603013/121690872-4844d680-cabe-11eb-9f78-2588dd73d520.png)

* I then filled out the form whilst performing several checks. I left the recipe description blank, entered a text (not numeric) value into the calories field and entered a negative number into the protein field. These three fields were correctly coloured red to provide a visual error indication to the user and checked that the validation and type input code was working. I also tested the toggle switch to makesure I could change this. I then tried to click the 'edit recipe' button and confirmed that it would not let me because of the errors in my input.

![testing edit recipe fields](https://user-images.githubusercontent.com/74603013/121691591-154f1280-cabf-11eb-9d1b-3e4b7418797e.png)

* I corrected the errors and clicked the 'edit recipe' button. I then confirmed that the flash message displayed with the correct message to confirm to the user that the recipe had been edited.

![flash edited message](https://user-images.githubusercontent.com/74603013/121692280-dd949a80-cabf-11eb-904e-21a5dfb857e9.png)

* I then navigated to the recipes page and confirmed that the edited 'nectarine & seed museli' recipe could be seen and that it had replaced the old 'fav drink' recipe. I thene xpanded the collapsible to ensure the full edited recipe details were displayed and correct.

![muesli recipe](https://user-images.githubusercontent.com/74603013/121692581-20567280-cac0-11eb-8c0e-f3b323bd4157.png)

### **Testing the delete recipe functionality**
* I clicked the red 'delete' button next to the recipe I wanted to delete. I confirmede that a modal appeared and displayed the correct information, warning the user that they were about to delete the recipe and providing two button options 'no, save recipe' and 'yes, delete recipe'. This proved the defensive programming functionality was working to prevent a one-click accidental deletion of a recipe by a user. I also checked the colours of the buttons were correct - green to save the recipe, red warning colour for the delete recipe button.

![delete modal](https://user-images.githubusercontent.com/74603013/121693004-9b1f8d80-cac0-11eb-8931-982f7ab12dae.png)

* I clicked on the 'no, save recipe' button and confirmed that I was returned to the recipes page and that I could still see my recipe in the list.
* Before deleting a recipe from the database, I first checked my MongoDB account which showed that there were 12 recipes in the recipes database.

![12 recipes](https://user-images.githubusercontent.com/74603013/121695689-33b70d00-cac3-11eb-9051-48267fe9f002.png)

* I then re-clicked the 'delete' button next to the recipe I wanted to delete on the recipes page and this time clicked the 'yes, delete recipe' button on the modal. I then confirmed that I was taken back to the recipes page, that the flash message was displayed with the correct message and that I could only see 11 not 12 reckipes in the database with the correct recipe having been removed from the list.

![deleted flash message](https://user-images.githubusercontent.com/74603013/121696962-7e855480-cac4-11eb-82ae-856bf4e24b1b.png)

* I then re-checked my recipes database on MongoDB to confirm that there were only 11 recipes now in the database.

![11 recipes](https://user-images.githubusercontent.com/74603013/121697220-be4c3c00-cac4-11eb-9627-4a1197d6b8d5.png)

### **Testing the add recipe functionality**
* I clicked on the 'add recipe' navbar tab and confirmed that this opened the 'Add recipe' form. I confirmed that the form was displaying as intended and looked the same as the 'edit recipe' form for consistency to the user experience, with the exception of the different title and 'Add recipe' button with correct icon.

![add recipe form](https://user-images.githubusercontent.com/74603013/121697850-5f3af700-cac5-11eb-9a83-11dbcbb756e9.png)

* I then ensured that the user had to choose a category or else a red error was displayed.

![choose category error](https://user-images.githubusercontent.com/74603013/121698085-93aeb300-cac5-11eb-8cd4-1d40e2699219.png)

* I madesure that the category dropdown displayed the correct information, that any empty fields were displayed red, that the numeric only inputs only allowed positive numbers, that toggle switch could be changed to on or off and that I couldn't add my recipe with the 'add recipe' button if all the fields weren't completed.

![incorrect form inputs](https://user-images.githubusercontent.com/74603013/121698712-2d766000-cac6-11eb-8aad-55589e124344.png)

* I then correctly completed the form and clciked the 'add recipe' button. I confirmed that I was taken to the recipes page, that a flash message confirming to the user that the recipe had been added and that I could see my newly added recipe as the first recipe in the list. I also confirmed that I had the option to 'edit' or 'delete' my newly added recipe.

![added recipe flash message](https://user-images.githubusercontent.com/74603013/121699613-02404080-cac7-11eb-91aa-08209a2ad7bd.png)

* I then clicked on my recipe to expand the collapsible and checked that my recipe details could be seen and matched what I had entered into the form.

![new recipe](https://user-images.githubusercontent.com/74603013/121699949-52b79e00-cac7-11eb-8925-8bb2e7bcf391.png)

* I checked back on my MongoDB recipes database to confirm that the number of recipes was back up to 12 recipes and that I could see the details of my newly added recipe in the database.

![back to 12 recipes](https://user-images.githubusercontent.com/74603013/121700393-c5287e00-cac7-11eb-9c35-94894bd5750b.png)
![new recipe in db](https://user-images.githubusercontent.com/74603013/121700402-c6f24180-cac7-11eb-8890-eca537014835.png)

* Finally I checked that I could view all 12 recipes on the recipe page.

![12 recipes displayed](https://user-images.githubusercontent.com/74603013/121700674-0d47a080-cac8-11eb-8f25-b5c4ab2b5959.png)

### **Testing the profile page**
* I navigated to the profile page and made sure that the correct username profile message was shown for the user I was signed in as (kimle), that I could see all the image card correctly and that all the image card buttons took me to the correct link or form as expected.

![profile page](https://user-images.githubusercontent.com/74603013/121700870-39632180-cac8-11eb-9dc4-ab9848ca010c.png)

### **Testing the logout functionality**
* I clicked the 'logout' navbar tab and confirmed that I was taken to the login page, that a flash message confirmed to the user that they had successfully logged out of their account and that the navbar tabs had changed so that I could no longer access the profile page or add recipe form.

![logout flash message](https://user-images.githubusercontent.com/74603013/121701340-b42c3c80-cac8-11eb-9630-00391663ae6f.png)

* I also checked that when I went to the recipes page, having logged out of my account, that I no longer had the option to 'edit' or 'delete' my recipes.

![cant change recipes](https://user-images.githubusercontent.com/74603013/121701765-26048600-cac9-11eb-9fe5-8da88f0afd46.png)

### **Testing the register functionality**
* Firstly I checked my MongoDB users database which showed that I had 7 registered users in the database.

![7 users](https://user-images.githubusercontent.com/74603013/121702452-cbb7f500-cac9-11eb-883b-c06acf4a6ff4.png)

* On the register page, I tried to submit the register form without filling in a username or password. Then I tried to only complete one field but not both fields and again tried to register. As expected, I couldn't register a new suer and the fields were highlighted red to show the user that this information were required fields.

![register no fields completed](https://user-images.githubusercontent.com/74603013/121703258-8e079c00-caca-11eb-82ec-c2a124c71198.png)

* I then confirmed that if I didn't use a password that met the password requirements (between 8-15 characters) that I couldn't register and the user was alerted to the problem

![register password error](https://user-images.githubusercontent.com/74603013/121704924-1cc8e880-cacc-11eb-8518-7b045c55496d.png)

* I then added a valid username and password and clicked the 'register' button to confirm that I was taken to the profile page, that the successful registration flash message displayed with the correct message and the profile display matched the username that I had signed in with (George). 

![register george](https://user-images.githubusercontent.com/74603013/121705716-d627be00-cacc-11eb-9622-134bd268f7b1.png)
![flash message registered](https://user-images.githubusercontent.com/74603013/121705719-d7f18180-cacc-11eb-8675-feea4b866d50.png)

* Finally I confirmed in my MongoDB users database that there were now 8 registered users and that George was showing in the database. I could also confirm that the password displayed in the database was using the secure hashed passwords instead of the password inputted by the user.

![users database](https://user-images.githubusercontent.com/74603013/121706202-4d5d5200-cacd-11eb-8a4d-a4d4cbbeb636.png)

### **Testing the login functionality**
* Having logged out from the previous test, I tried to login as kimle but using an incorrect password, then clicked the 'login' button. This confirmed that I couldn't login and that a flash message displayed telling the user that an incorrect either username or password had been submitted so that the user didn't know which was correct or incorrect for added security.

![flash message login error](https://user-images.githubusercontent.com/74603013/121706767-d8d6e300-cacd-11eb-834b-797169122538.png)

* I then tried again with the correct username and password and confirmed that I was taken to the profile page, that the flash mesage displayed correctly welcoming the correct user and that the profile page header also displayed the correct username for the user I was logged in as (kimle).

![welcome flash message](https://user-images.githubusercontent.com/74603013/121707195-3c611080-cace-11eb-83a9-64fa4e376d26.png)

### **Testing Compatibility With Browsers**
I manually tested the website on Microsoft Edge, Google Chrome and Mozilla Firefox browsers. I checked that buttons, links, the form inputs, carousel, collapsible accordion, responsiveness and design worked as planned.

### **Testing Compatibility With Different Devices**
I manually tested the website on a mobile and desktop device. I sent the link for my deployed website to family, who also checked the website on their devices. The website worked for the variety of mobile and desktop devices tested.  I checked that the different grid layouts for the different screen sizes worked as expected and that the logo size, padding and navbar toggle worked as expected. I didn't have access to a tablet device, so I tested this via the 'Inspect accessibility properties' option when right-clicking on the website and choosing the ipad view.

## **Problems Resolved During Testing**
* On the profile page, the image cards were different heights and two of the headings were more than one line length. 

![uneven image card lengths](https://user-images.githubusercontent.com/74603013/121676720-e16af180-caac-11eb-993c-3f1995600b36.png)

I fixed the different height problem by adding the class of 'large' to all three of the image cards. This is a Materialize class for setting a fixed height to the cards. This made them the same height which looked better. However, the different line lengths of the headings didn't look good to me. I tried changing to a smaller h6 header and also just using bold text, but the headings still required two lines. As I liked the three image cards being displayed next to each other on a desktop device, I didn't want to change the grid layout col value. Instead I opted for shorter one-line headings on all three image cards. This has the added benefit of being short and catchy so the user is more likely to read it! I also added the class of center-align for the heading and paragraph which further improved the visual appeal of the profile page.

![better image cards](https://user-images.githubusercontent.com/74603013/121677488-d795be00-caad-11eb-9548-3818a4bcb9ce.png)

* On the add recipe and edit recipe form, the calories, protein, carbohydrate and fat form fields still allowed letters to be entered. I wanted these fields to be numeric values only to prompt the user to enter the correct information. I realised this was because I had the type="text" so I changed this to type="number". This then corrected the error and also added a helpful up/down arrows to help the user change the value, as well as allow manual input.

![text to numeric add recipe change](https://user-images.githubusercontent.com/74603013/121678444-1aa46100-caaf-11eb-88ba-de0b3e7bcb1d.png)

However, this created another problem in that these form fields could then allow (even encourage) the user to enter a negative value which is clearly incorrect and undesirable. I then added the class of min="0" to makesure that the validation only allowed positive numbers to be entered. I used this [post](https://stackoverflow.com/questions/31575496/prevent-negative-inputs-in-form-input-type-number) to understand that the min class was required for allowing only positive values.

* When my project was deployed live on Heroku, I noticed the internet tab still read 'Task Manager' from having followed the Code Institute tutorials to create my base template. I changed the title on the base.html to read Whey Too Tasty to reflect the website. 

![tab](https://user-images.githubusercontent.com/74603013/121682830-79b8a480-cab4-11eb-9f45-0aaed6534f08.png)

* Whilst it was not a problem as such, when a user added a recipe it would be displayed at the bottom of the recipe page. This meant that the user had to scroll to the bottom of the recipe list or use the search functionality to get to their newly added recipe. This could have become a problem once there were lots of recipes in the database. To resolve this problem I added a sort function in my Python code to display the recipes in reverse order, so that the last recipe added was displayed as the first recipe on the recipes page. I used this [Code Institute Slack thread](https://code-institute-room.slack.com/archives/C7JQY2RHC/p1612694378461500) for advice on how to achieve this.

## **Testing with Google Chrome Lighthouse**
I generated a Lighthouse report for each of my pages to analyse the web page's performance and get tips for improving the user experience.


![Lighthouse Report Home](https://user-images.githubusercontent.com/74603013/121755214-879b1380-cb0e-11eb-99bc-433fa343fa13.png)
![Lighthouse Report Recipes](https://user-images.githubusercontent.com/74603013/121755223-8f5ab800-cb0e-11eb-8b69-ea40534e33ef.png)
![Lighthouse Report profile](https://user-images.githubusercontent.com/74603013/121755230-941f6c00-cb0e-11eb-9c5f-0396ad8d1fbf.png)
![Lighthouse Report add recipe](https://user-images.githubusercontent.com/74603013/121755235-971a5c80-cb0e-11eb-9515-6b892718fc6b.png)
![Lighthouse Report Login](https://user-images.githubusercontent.com/74603013/121755246-9c77a700-cb0e-11eb-862d-4d960a571ba6.png)
![Lighthouse Report register](https://user-images.githubusercontent.com/74603013/121755250-9eda0100-cb0e-11eb-949d-14bad5c65405.png)

The Lighthouse reports highlighted some areas that could be improved, these were:
* The performance on the home page and profile page were amber. The detail of the report advised to: "Avoid enormous network payloads" this was due to the very large size of the images in the carousel on the home page and the image cards on the profile page. These were also slowing my page loading speeds. If this was a real website then this would need to be addressed before launching the website. In the future I could perhaps try a way to compress the images before adding them into my code.
* The accessibility for the profile and add recipe pages could be improved. The advised that: "background and foreground colours don't have a sufficient contrast ratio". For the profile page this is because the images in the image cards don't contrast enough with the white background. To overcome this issue in the future I could try adding a border to the image card or adding a contrasting background colour behind the image cards. For the add recipe page, this was because the form blended into the white background. Again to overcome this issue in the future I could add a border to the form, change the form colour or add a background colour behind the form.
* 






