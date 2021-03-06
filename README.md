# Code Institute: Milestone Project 3 #

## Whey Too Tasty ##
This project has been created for my Milestone Project 3 for the Full Stack Development Diploma at The Code Institute. The purpose of the project is to create a full-stack site that allows users to manage a common dataset about a particular domain, using HTML, CSS and Javascript, Python + Flask and MongoDB.

Whey Too Tasty is a fictional online cookbook for healthy, high-protein recipes. The aim of Whey Too Tasty is to provide a website where users can find and share recipes whilst promoting the website owner’s protein powder product, with the prupose of increasing the sale of this product. Users will interact with the website through being able to create, read, upload and delete recipes.

![Whey Too Tasty2](https://user-images.githubusercontent.com/74603013/121527722-9e4c4800-c9f2-11eb-88a4-2d474e0a148d.png)

My deployed project can be viewed live [here](https://whey-too-tasty.herokuapp.com/).

## UX ## 

### Main Aims ### 
* To create a website that acts as an online cookbook for users to find healthy, high-protein recipes.
* To create a website that provides a quick and simple way for members to create, read, upload and delete recipes within their member account.
* To make a website that uses Javascript to allow the website users to interact with the website.
* To design a website that is both visually appealing and easy to navigate for the wide range of potential users.
* To create a website that provides a good user experience on mobile, tablet and desktop devices.

### User Stories ###
* I am the owner of the website, I want to promote the use of my protein powder supplement in recipes, to sell more of my product.
* I am a dietician wanting to share my healthy, nutritionally-balanced recipes with other people.
* I am new to cooking, I want to find healthy recipes with simple, easy cooking instructions, so I can learn to cook my own meals.
* I am a bodybuilder, I want to find recipes, to cook meals that fit my calorie and macronutrient needs.
* I am a user who has submitted a recipe, I have since improved my recipe and want to update the recipe to improve it.

### The 5 Planes of UX ###
Having created the user stories so that I knew who I was designing my website for, I then followed the user centred design process to create a website that would answer the above user stories.
1.	**Strategy Plane:**
    * When addressing the strategy plane, I focused on who the website users were likely to be and the objectives the website needed to meet to attract these users. I kept in mind the question: Why is the Whey Too Tasty website so special?
        * Reason for the website’s existence – To serve the nutrition and fitness community allowing like-minded people to find, upload and share high-protein recipes.
        * Culture of the audience –Nutrition and fitness community wanting to increase their protein intake which may include:
            1.	People wanting to lose weight.
            2.	People wanting to gain muscle.
            3.	Bodybuilders and physique competitors.
            4.	Sport athletes.
            5.	Personal trainers and the gym community.
            6.  Nutritionists, dieticians etc.
        * User demographic – the website is open to members of all ages who are likely to have a large variation in cooking ability, nutrition requirements, dietary preferences, food budget, cooking equipment etc.  The website branding therefore needs to appeal visually to all ages and genders. It must also be able to be navigated easily as the users could have a wide range of computer competency levels.
    * I researched current recipe websites (specifically allrecipes (http://allrecipes.co.uk/) and BBC Good Food (https://www.bbcgoodfood.com/)) to gather information on what these websites offer their users; the pros and cons that I liked as a user of their website and to identify the features and information they provided. This gave me ideas of how to address my user’s needs but also how I could further improve my user’s experience to add value to the Whey Too Tasty website.

2.	**Scope Plane:**
    * When addressing the scope plane, I focused on what features were to be included on the website and its key functionality to meet the user’s needs. I also needed to combine these with Javascript as per the requirements for my Code Institute MSP3. I kept in mind the question of: Why would a user want this?
	    * Requirements: ability to find high-protein recipes, ability to create, upload, edit and delete high-protein recipes; ability to share high-protein recipes with others; ability for user’s to buy the website owner’s protein powder.
        * Key features (from the user's perspective): an easy-to-use form to search for recipes that meet my needs, a simple process to join as a member, a simple process to log in to my member account, an easy-to-use form to create and upload my own recipes, an easy way of editing my recipes, a simple method to share recipes with others, a simple way to buy the protein powder the website promotes.
        * CRUD functions: To achieve the above requirements and key features I needed to implement the Create, Read, Update & Delete (CRUD) functions for my database. I decided to use them in the following ways:
            1. Create: 
                * Create a new user (register account)
                * Create a new recipe (add recipe)
            2. Read:
                * To search, find and read recipes in the database
            3. Update:
                * Update a recipe (edit recipe)
            4. Delete: 
                * Delete a recipe

3. **Structure Plane:**
    * When addressing the structure plane, I focused on the journey the website would take the users on. I kept in mind the question: What is an intuitive way to navigate through the content and features?
        * How to get there? I knew that my website should include a navbar with tabs to enable users to easily navigate through the website content. There would also be buttons linked to specific parts of the website such as the ‘register’ form to allow users to quickly and easily access the main features.
        * I wanted some of the website like the home page and recipes page to be open to all users, but for some pages like the add recipe page to be visible only to users who were logged in to their account in the website. I decided to have different tabs displaying, depending on whether or not a user was logged in. For example, a user who is already logged in doesn’t want to see ‘Register’ or ‘Login’ options, so instead can see ‘Logout’.
        * How will they move through the website? – user who isn’t logged in. This user can see 4 pages: Home, Recipes, Login and Register. By using this order, the user first learns about the whey protein product the website owner wants to sell, then the user can then see recipes using the product, encouraging them to want to buy the protein powder. Finally, the user has the option of logging in or registering an account to access more website features.
        * How will they move through the website? – user who is logged in. This user can see 5 navbar tabs: Home, Recipes, Profile, Add recipe and Logout. This user can access the home page to see images promoting the product and links to purchase their whey protein, see recipes using the protein powder & where they can edit or delete their own recipes, view their profile to easily navigate around the website, add their own recipes and logout of their account.

4. **Skeleton Plane:**
    * When addressing the skeleton plane, I focused on the keeping the layout design of the website familiar to the users by using a standard layout the users would be use to seeing. I kept in mind the question: What conventions will the user be familiar with?
    * How to style the page? I knew that my website pages should be consistent in style and that they should use a standard page layout. I chose to use features the user would expect to see including: a navbar at the top of the page, a header title at the top of each page, a main body and a footer at the bottom of the page with social media links.

5. **Surface Plane:**
    * When addressing the surface plane, I focused on the website branding and details like the colour, fonts and images. I kept in mind the question: What will be appeal to my users?
        * Images – promoting the whey protein powder the website owner sells and showing high-protein recipes to appeal to the website’s users.
        * Colour scheme – I chose to use the colours of orange and white as these are gender neutral colours that will appeal to people of all ages. They are also strong colours that will stand out from the potentially large number of colours in recipe photos. I used Coolors to create a colour palette from orange and white.
        ![Whey Too Tasty palette](https://user-images.githubusercontent.com/74603013/121207474-37ebec00-c871-11eb-976c-dc9345ede2dd.png)
        * Icons – I chose to use font awesome icons across the pages where it could aid the user’s understanding and for greater visual appeal.
        * Logo – I chose to position the logo in the top left-hand corner of the website (within the navbar) as this is a convention of websites that users have to come to expect.
        * Call to action buttons - I chose to colour the call-to-action buttons in bright colours to attract the user and make them more likely to click them.
        * Carousel – I chose to have an image carousel on the home page to showcase several images that promote the website owner’s whey protein powder. The carousel is interactive to encourage the users to interact with the website. If they are clicking through photos and interacting with the website, this is likely to increase the amount of people who click through to buy the whey protein via the button.
        * Collapsible accordion – I chose to present the recipes in a collapsible accordion. This allows the user to see the recipe name and a quick description. They can then click on the recipe they like to find the other information like ingredients and method, which they are encouraged to do with a dropdown arrow.


### **Wireframes**
Before I started coding my project, I created wireframes using Balsamiq. I created wireframes for mobile, tablet and desktop devices to decide the layout at different screen sizes. I also used the user stories to add more detail to the website to provide a better user experience. 

**Wireframes for mobile devices**
![Mobile device wireframes](https://user-images.githubusercontent.com/74603013/121753697-d646ae80-cb0a-11eb-9986-40260ea9bcff.png)

**Wireframes for tablet devices**
![Tablet device wireframes](https://user-images.githubusercontent.com/74603013/121753991-65ec5d00-cb0b-11eb-9f21-d67f14cf56ae.png)

**Wireframes for desktop devices**
![Desktop device wireframes](https://user-images.githubusercontent.com/74603013/121753910-3fc6bd00-cb0b-11eb-929a-c0268fc7e03e.png)

### **Database structure**
I started my project by getting my data structure in place first.
* The data for this project is stored in my MongoDB database within three collections as follows:

    1. Categories - this stores the recipe category options of Drink, Meal or Snack.
    2. Recipes - when a recipe is added by the user, it is stored in this collection along with the information about the recipe collected from the add recipe or edit recipe form.
    3. Users - when a new user registers an account, it is stored in this collection along with their username and their password that is securely stored via a hashing method.

### **Features**
Features consistent across all the different pages of my project include:

1. **Navbar**
    * The navbar has the Whey Too Tasty logo which, when clicked, returns the user to the home page. On the right-hand side are the navigation tabs linking to each of the pages. The navbar tabs change depending on whether or not the user is logged in, to provide a better user experience by showing them only what they need. The orange (#ff9100) fits with the colour scheme and provides a good contrast for the white-coloured text and logo. A text-shadow effect, further enhances readability. When the user hovers over a navbar tab, the background colour of the tab changes to provide visual feedback as to which tab they are about to click. The navbar collapses to a toggle button on tablet and mobile devices for an improved user experience on smaller screen sizes.

2. **Title**
    * Each page starts with a simple title, that explains the purpose of that page. The text colour (#1f1300) is consistent across all pages and fits with the Coolors palette.

3. **Prompt to buy whey protein and link button**
    * At the bottom of each page, above the footer, is a header prompting the user to buy whey protein by asking "Do you need whey protein?" with a button just below that takes the user to the site owner's whey protein powder shop where they can make their purchase. The header text colour (#1f1300) is consistent across all pages and fits with the Coolors palette. The button colour (#ff6d00) is consistent across all pages, fits with the colour scheme, matches the other main call-to-action buttons and is an obvious colour and centre-aligned for obvious positioning.

4. **Footer**
    * The footer is the same peach colour (#ff6e40) as the closest Materialize match to the Coolors palette. It is the same colour across all pages to provide consistency in design. It includes social media links and copyright information which are coloured (#1f1300) to fit with the rest of the text colour across the website. The footer is the normal place that a user would look for this information. The social media links open a new tab, when clicked by the user, to take them to the corresponding website.

5. **Flash messages**
    * All flash messages are the same in style, font size and colour. They are all full-screen width and located at the top of the page the user is on. The text is centered and large, to be easy to read. The colour is a deep orange to fit the colour theme but attract the user's attention.

6. **Interactive features**
    * When the user hovers over a button, link or Javascript element such as the navbar tabs, buttons, logo, collapsible accordion, social media link icons or image carousel; then the mouse cursor changes from an arrow to a pointed finger cursor to provide a visual indication to the user that they can click on this item and to encourgae them to click it.

Features on the seperate pages include:
1. **Home Page**
    * Includes a carousel of 5 images which all promote the website owner's whey protein product that they are trying to get the website user to purchase. It shows the whey protein being enjoyed by people and being used in recipes. These images are relevant to the purpose of the website and will appeal to the intended website users.

2. **Recipes Page**
    * Includes a search bar that invites the website user to search for a recipe name that they would like to find. Along with two buttons: one to perform their search and the other to reset back to the full recipe list after they have performed a search. The buttons are different colours to make it visually obvious to the user that these buttons have different purposes.
    * Includes a collapsible accordian with the recipe information. When unselected, the accordian header shows the recipe name and recipe description to quickly provide information about that recipe to the user. The user is prompted to expand the collapisble with a dropdown arrow symbol. There is also a utensils font awesome icon that provides a visual indication of a quick to serve meal. When selected the collapsible expands to provide the rest of the recipe information. A header, paragraphs and bold text elements make it easy for the user to read, find and understand the information displayed.

    **Additional features for logged in users**

     * A red delete button in the header of the collapsible, is displayed next to the user's own recipes. The red provides a visual warning that pressing the delete button is an action that will remove the recipe.
     * An orange edit button in the header of the collapsible, is displayed next to the user's own recipes. The orange fits with the colour scheme of the website and is friendlier than the harsh red of the delete button to emphasis that this is an edit not delete option. Pressing this button opens the edit recipe form.

3. **Login page**
    * Includes a login form requiring the user to enter their username and password and then submit their information by pressing the 'login' button to access their account. 
    * Includes a link to the register page if the user doesn't already have an account to login to.
    * If the user enters an incorrect username or password, a flash message appears saying: "Incorrect username and/or password". This is a full-screen width message with an obvious dark orange border at the top of the page to be really obvious to the user.
    * Both the username and password form inputs must be completed before the user can login.

4. **Register page**
    * Includes a register form requiring the user to enter a username and password and then submit their information by pressing the 'register' button to create their account. 
    * Includes a link to the login page if the user already has an account to login to.
    * If the user enters a username that already exists in the database, a flash message appears saying: "Username already exists, please try again". This is a full-screen width message with an obvious dark orange border at the top of the page to be really obvious to the user.
    * The password must be between 8 and 15 characters and include only a-zA-Z0-9.
    * Both the username and password form inputs must be completed before the user can register.

5. **Profile page**
    * Includes an initial flash message welcoming the user. This is a full-screen width message with an obvious dark orange border at the top of the page to be really obvious to the user.
    * Includes a profile box saying "{username's} profile" to personalise the profile page to that user.
    * Includes three image cards to provide visual appeal to the user. Image card one promotes the different whey protein flavours sold by the website owner, with a button encouraging the user to 'shop whey protein' that when clicked opens the website owner's online shop in a new tab. Image card two promotes a recipe made using the site owner's whey protein product. A 'find a recipe' button linked to the recipes page encourages the user to find or search for a recipe. Image card three has a question mark along with an 'add your recipe' button linked to the 'add recipe' form which encourages the user to interact with the website.

6. **Logout**
    * Upon clicking the logout navbar tab, the user is redirected back to the login form. A flash message appears saying: "You have successfully logged out" to confirm to the user that they have logged out. This is a full-screen width message with an obvious dark orange border at the top of the page to be really obvious to the user.

7. **Add recipe**
    * Includes a form that requires all the inputs to be completed before the user can add their recipe.
    * Icons next to some of the form inputs aid the user's understanding of what the field inputs mean.
    * Some inputs like the calories, protein, carbohydrate and fat fields only accept numeric values to encourage the user to complete the form correctly.
    * The recipe category input is a dropdown menu for the user to quickly and easily select one of the categories available in the database.
    * One click at the end of the form via the 'add recipe' button, adds their recipe to the database. This button also has a plus icon to further improve the user experience. Upon clicking the button, the user is returned to the recipes page and a flash message saying: "Recipe successfully added" confirms that their recipe has been included in the database.
    * The icons and button are orange, in keeping with the rest of the website.

8. **Edit recipe**
    * Upon clicking the 'edit' button, the user is directed to the edit recipe form. This looks exactly the same as the add recipe form, so will already be familiar to the user. Furthermore, it is preloaded with the information from the original recipe. This makes it simple for the user to see what the current recipe says and makes editing the recipe a quicker process. 
    * The user has two options: a red 'cancel' button and an orange 'edit recipe' button. The red 'cancel' button has a red cross to enhance the user's understanding of this button's function. Clicking this button returns the user to the recipes page. The orange 'edit recipe' button has an edit icon, again enhancing the user's understanding of the button's purpose. Clicking this button causes a flash message saying: "Recipe successfully updated" to appear.

9. **Delete recipe**
    * Upon clicking the 'delete' button, a modal appears with an obvious 'stop!' header and a message saying: "Are you sure you want to delete this recipe?". The user then has two options: a 'no, save recipe' button, coloured green to indicate that this saves the recipe and a red 'yes, delete recipe' button, coloured red to warn that this removes the recipe. Clicking to save the recipe returns the user to the recipes page. Clicking to delete the recipe also returns the user to the recipe page but this time with a flash message saying: "Recipe successfully deleted".

### **Features changed from wireframes**
* The text content of the website was improved and added to as the project progressed.
* Image carousel on the home page was changed from a scrolling image display to a carousel that the user has to click/swipe to change the image displayed. This was changed to encourage the user to interact with the website more, which is likely to increase their use of the website and also to explore it more and also makes the user more likely to click on button links to the shop if they are already interacting with the site.
* Added a background filled orange square border to the dropdown arrow symbol on the collapsible accordian to make it even more visually obvious to the user that there is more information if the user expands the collapsible. The symbol encourages the user to click on it.
* Added a tooltip to the utensils icon on the collapsible accordian which reads: "quick & easy recipe" to aid the user's understanding of the meaning of this symbol.
* Added a modal that confirms with the user that they really did mean to delete the recipe upon clicking the delete button. This acts as defensive programming to prevent the user accidentally removing the recipe. To delete the recipe, the user now has to confirm on the modal that they do wish to delete, but they also have the option to cancel and keep the recipe if the first click was unintentional.
* Made the Whey Too Tasty logo smaller to fit better on smaller screen sizes, then added a media query to make the logo bigger on tablet and desktop devices to improve the user experience.
* Changed the colour of the text, navbar, footer, footer text/icons and collapsible to fit with the Coolors palette to make the website more visually appealing. 
* Changed the colour of some of the buttons to give greater meaning to the user in accordance with conventions the user would be use to e.g. green is good/safe and red is a warning colour.
* Changed the edit recipe form so that it preloaded the form fields with the information from the current recipe being edited, to improve the user experience by making the editing process quicker, simpler and so the user could see what they had previously put.
* Added flash messages to provide useful feedback to the user e.g. confirming successful registration or incorrect password and/or username.
* Changed the navbar tabs on most tablet-sized devices to the navbar collapsible toggle icon as used on mobile devices as the tabs look too 'cluttered' on smaller tablet screens.
* Added the buy whey protein powder prompt header and button linked to the shop, to all pages not just the home page to increase the chances of the user clicking the link and making a purchase as per the aim of the website.
* Changed to a sticky navbar, so that no matter where on the page the user is, they can access the navbar, this may be useful to the user when lots of recipes have been added to the database, so they can quickly navigate around the website if they have scrolled a long way down the recipe page, rather than having to scroll all the way back up.

### **Future Scope**

I think that there is a lot of potential to further develop this website, which is unfortunately beyond the scope and time frame of this Milestone Project. In the future, I would like to implement the following features:

* Recipe photos to be added to the collapsible to improve the visual appeal of the website, aid the user's website experience and improve their understanding of the recipe.
* Add the ability for users to rate/review the recipes and add these customer reviews to the collapsible for each recipe.
* Add more interactive features such as video demonstrations of making the recipes. This would then open the website up to more users such as those who can't read, are blind or that cannot undertsand the English language but that could watch or listen to a video.
* Add other icons/information to the collapsible accordion such as the time needed to cook the recipe or the cooking skill level required to make it etc. I would then add a toggle switch for these features to the add/edit recipe forms to collect this information, store it in the database and retreive it for displaying on the collapsible.
* Add the ability for a user to reset their password.
* Add the user's own recipes onto their profile page.
* Integrate the user's profile to the whey protein shop so that they can see information such as their whey protein order history and the ability to quickly re-order.

### Technologies Used ###
* HTML5 used for the .html pages
* CSS used to style the html pages.
* Javascript used to make my website interactive with the carousel and collapsible accordian.
* [jQuery](https://api.jquery.com/) javascript library used for my javascript code denoted by $ prefix on script.js.
* [Random Key Gen](https://randomkeygen.com/) to produce the secure passwords used in my project.
* [Coolors](https://coolors.co/616163-17bebb-fafaff-db995a-ff9f1c) to create a professional looking colour palette for my website.
* [Balsamiq](https://balsamiq.com/) used to create my wireframes.
* Jinja - templating language for some of my Python code denoted by {% %}.
* [Materialize](https://materializecss.com/getting-started.html) for the main and mobile navbars, sticky footer, collapsible accordian, carousel, modal, tooltip template, form templates, card templates and grid layout.
* [Canva](https://www.canva.com/) used to create the image for the add a recipe image card on the profile page.
* [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) used to check the validity of my html code for all .html pages.
* [W3C CSS Validation Service](http://jigsaw.w3.org/css-validator/#validate_by_input) used to check the validity of my css code for the style.css file.
* [JSHint](https://jshint.com/) used to check the validity of my javascript code for the script.js files.
* [PEP8 Online](http://pep8online.com/) used to check the PEP8 compliance of my Python code.
* [Am I responsive](http://ami.responsivedesign.is/#) used to check the responsiveness of my design on different screen sizes and for creating the first image in this README file.
* [Paint 3D](https://microsoft-paint-3d.en.softonic.com/) used to crop the screenshots of images added to this README.md file and testing.md file.
* [Google Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) used to generate Lighthouse reports on the performance of all my web pages once the project was deployed.
* [Heroku](https://www.heroku.com/what) to deploy my website.
* [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=bing&utm_campaign=mdb_bs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=415204562&msclkid=9d365b5212331e600c093b9174dbb54f) to create my database used in this project.
* [Pymongo](https://pymongo.readthedocs.io/en/stable/index.html) for getting my MongoDB database to work with my Python code.
* Flash Python microframework used to help write the Python code for this project.
* [Gitpod](https://www.gitpod.io/) to write my project code.
* [GitHub](https://github.com/) remote repository where my project is stored.
* [Font Awesome](https://fontawesome.com/) for the icons used throughout the website.

### **Testing**
The testing that I undertook on my project is detailed in the [testing.md](testing.md) file. 

### **Deploying my project**

 I created my project using Gitpod and deployed my project using the Heroku app hosting platform.

* To deploy my wesbite I completed the following steps:

    1. Typed "pip3 freeze --local > requirements.txt" into the command terminal on my Gitpod workspace.
    2. Typed "echo web: python app.py > Procfile" into the command terminal on my Gitpod workspace.
    3. Opened the requirements.txt file to check all my dependencies were listed.
    4. Opened the Procfile and removed the blank space at the bottom of the file.
    5. Opened Heroku.
    6. Signed into my account.
    7. Created a new app with a unique name that had not already been taken (this project uses 'whey-too-tasty'). 
    8. I then selected the region closest to me: 'Europe'.
    9. Clicked the 'Create app' button.
    10. I opened the 'Settings' tab.
    11. Clicked the 'Reveal Config Variables' button.
    12. I then inputted the Config Vars name and associated value/password for the following:
        * IP
        * MONGO_DBNAME
        * MONGO_URI
        * PORT
        * SECRET_KEY
    13. Clicked the 'Deploy' tab.
    14. Selected the 'Connect to Github' button next to 'Deployment method'.
    15. Ensured my GitHub profile was displayed and then selected my GitHub repository for the project (this project is called KimLHill/MSP3).
    16. Then clicked the 'Connect' button.
    17. Back on Gitpod, I committed the requirements.txt and Procfiles.
    18. I then did a Git push to push them to GitHub.
    19. Back on Heroku, I clicked the 'Enable Automatic Deployment' button.
    20. Clicked 'Deploy Branch'.
    21. Finally, I clicked on the 'View' button to view my deployed project.

### **Using My Project**

To run my project locally you can clone the project.

* To clone my project, complete the following steps:

    1. Open GitHub.
    2. Select my project repository called KimLHill/Kimberley_Hill_MSP2.
    3. Click on the green ‘Code’ button.
    4. Click the clipboard icon next to the url to copy the url link.
    5. Open Git Bash.
    6. Change the current working directory to the location where you want the cloned directory.
    7. Type git clone, and then paste the url link you copied in step 4.
    8. Press enter to create your local clone.

        Alternative methods of cloning my project can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

To make a copy of my project to your GitHub account, you can fork a copy of my project.

* To fork a copy of my project, complete the following steps:

    1. Log in to your GitHub account (or create a new account).
    2. Search for my repository called KimLHill/MSP3.
    3. In the far right-hand corner of the screen at the top of the repository, click the ‘fork’ button next to the fork icon.

    Further information about forking a repository can be found [here](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

### **Credits**
* The website is for a fictional online cookbook, the content is fictional and was created by myself.
* I used this [post](https://stackoverflow.com/questions/37247474/es6-in-jshint-jshintrc-has-esversion-but-still-getting-warning-using-atom) to get the comment to resolve the JSHint warnings cause by esversion: 6.
* I used this [post](https://stackoverflow.com/questions/31575496/prevent-negative-inputs-in-form-input-type-number) to get the min="0" class for ensuring only positive numbers could be added for my numeric form input fields on the add recipe and edit recipe forms.
* I used this [Code Institute Slack thread](https://code-institute-room.slack.com/archives/C7JQY2RHC/p1612694378461500), specifically the code template provided by user Pauld0051 to get the template code that I could modify to get my recipes page to display in reverse order, so that they newest added recipe was displayed at the top of the list.
* Photos used were from [Wheybox's Instagram page](https://www.instagram.com/whey_box/), a link for each image is provided below under Media. 

### Acknowledgements ###
* My Code Institute mentor Seun Owonikoko whose feedback throughout the project influenced my website design, content and features.
* The Code Institute tutorial videos, especially from the 'Mini project | Putting it all together' section in the 'Backend Development' module.
* My family and friends who tested my website on their devices and provided feedback to improve my website.

### Media ###
The images used on my wireframes and website are from:
* [Carousel one](https://www.instagram.com/p/CM2CaBOLJMi/?utm_source=ig_web_copy_link)
* [Carousel two](https://www.instagram.com/p/B9Ytgb7nQ7Q/?utm_source=ig_web_copy_link)
* [Carousel three](https://www.instagram.com/p/CKTfkGgAb-7/?utm_source=ig_web_copy_link)
* [Carousel four](https://www.instagram.com/p/CN4jh4WARzo/?utm_source=ig_web_copy_link)
* [Carousel five](https://www.instagram.com/p/ByuKPdcgCwY/?utm_source=ig_web_copy_link)
* [Shop whey protein image card](https://www.instagram.com/p/BycFMvxlKKj/?utm_source=ig_web_copy_link)
* [Find a recipe image card](https://www.instagram.com/p/CBGFdhgHSNo/?utm_source=ig_web_copy_link)
* [Tablet outline](https://image.freepik.com/free-icon/computer-tablet_318-40639.jpg) used for creating my tablet wireframes.
* Add a recipe image card was created myself using Canva.