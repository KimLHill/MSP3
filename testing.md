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

### **Testing Compatibility With Browsers**
I manually tested the website on Microsoft Edge, Google Chrome and Mozilla Firefox browsers. I checked that buttons, links, the form inputs, responsiveness and design worked as planned.

### **Testing Compatibility With Different Devices**
I manually tested the website on a mobile and desktop device. I sent the link for my deployed website to family, who also checked the website on their devices. The website worked for the variety of mobile and desktop devices tested. I didn't have access to a tablet device, so I tested this via the 'Inspect accessibility properties' option when right-clicking on the website and choosing the ipad view.

## **Bugs Found In Testing**
* On the profile page, the image cards were different heights and two of the headings were more than one line length. 

![uneven image card lengths](https://user-images.githubusercontent.com/74603013/121676720-e16af180-caac-11eb-993c-3f1995600b36.png)

I fixed the different height problem by adding the class of 'large' to all three of the image cards. This is a Materialize class for setting a fixed height to the cards. This made them the same height which looked better. However, the different line lengths of the headings didn't look good to me. I tried changing to a smaller h6 header and also just using bold text, but the headings still required two lines. As I liked the three image cards being displayed next to each other on a desktop device, I didn't want to change the grid layout col value. Instead I opted for shorter one-line headings on all three image cards. This has the added benefit of being short and catchy so the user is more likely to read it! I also added the class of center-align for the heading and paragraph which further improved the visual appeal of the profile page.

![better image cards](https://user-images.githubusercontent.com/74603013/121677488-d795be00-caad-11eb-9548-3818a4bcb9ce.png)

* On the add recipe and edit recipe form, the calories, protein, carbohydrate and fat form fields still allowed letters to be entered. I wanted these fields to be numeric values only to prompt the user to enter the correct information. I realised this was because I had the type="text" so I changed this to type="number". This then corrected the error and also added a helpful up/down arrows to help the user change the value, as well as allow manual input.

![text to numeric add recipe change](https://user-images.githubusercontent.com/74603013/121678444-1aa46100-caaf-11eb-88ba-de0b3e7bcb1d.png)

However, this created another problem in that these form fields could then allow (even encourage) the user to enter a negative value which is clearly incorrect and undesirable. I then added the class of min="0" to makesure that the validation only allowed positive numbers to be entered. I used this [post](https://stackoverflow.com/questions/31575496/prevent-negative-inputs-in-form-input-type-number) to get understand that the min class was required for allowing only positive values.




