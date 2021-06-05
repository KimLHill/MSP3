![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome KimLHill,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidently make it public then you can create a new one with _Regenerate API Key_.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

---

Happy coding!




# Code Institute: Milestone Project 3 #

## Whey Too Tasty ##
This project has been created for my Milestone Project 3 for the Full Stack Development Diploma at The Code Institute. The purpose of the project is to create a full-stack site that allows your users to manage a common dataset about a particular domain, using HTML, CSS and Javascript, Python + Flask and MongoDB.

Whey Too Tasty is a fictional online cookbook for healthy, high-protein recipes. The purpose of Whey Too Tasty is to provide a website where user’s can find and share recipes whilst promoting the website owner’s protein powder product. User’s will interact with the website through being able to  create, upload, edit, delete, find and share recipes.

My deployed project can be viewed live here.

## UX ## 

### Main Aims ### 
* To create a website that acts as an online cookbook for user’s to find healthy, high-protein recipes.
* To create a website that provides a quick and simple way for members to create, read, upload and delete recipes within their member account.
* To make a website that uses Javascript to allow the website users to interact with the website.
* To design a website that is both visually appealing and easy to navigate for the wide range of potential users.
* To create a website that provides a good user experience on mobile, tablet and desktop devices.

### User Stories ###
* I am the owner of the website, I want to promote the use of my protein powder supplement in recipes, to sell more of my product.
* I am a dietician wanting to share my healthy, nutritionally-balanced recipes with other people.
* I am new to cooking, I want to find healthy recipes with simple, easy cooking instructions, so I can learn to cook my own meals.
* I am a bodybuilder, I want to find recipes, to cook meals that fit my calorie and macronutrient needs.
* I am a gym user who wants to gain muscle, I want to find high-protein recipes using ingredients I already have.
* I am a personal trainer, I want to find and share healthy, high-protein recipes with my clients.

### The 5 Planes of UX ###
Having created the user stories so that I knew who I was designing my website for, I then followed the user centred design process to create a website that would answer the above user stories.
1.	Strategy Plane:
    * When addressing the strategy plane, I focused on who the website users were likely to be and the objectives the website needed to meet to attract these users. I kept in mind the question: Why is the Whey Too Tasty website so special?
        * Reason for the website’s existence – To serve the nutrition and fitness community allowing like-minded people to find, upload and share high-protein recipes.
        * Culture of the audience –Nutrition and fitness community wanting to increase their protein intake which may include:
            1.	People wanting to lose weight.
            2.	People wanting to gain muscle.
            3.	Bodybuilders and physique competitors.
            4.	Sport athletes.
            5.	Personal trainers and the gym community.
        * User demographic – the website is open to members of all ages who are likely to have a large variation in cooking ability, nutrition requirements, dietary preferences, food budget, cooking equipment etc.  The website branding therefore needs to appeal visually to all ages and genders. It must also be able to navigated easily as the users could have a wide range of computer competency levels.
    * I researched current recipe websites (specifically allrecipes (http://allrecipes.co.uk/) and BBC Good Food (https://www.bbcgoodfood.com/)) to gather information on what these websites offer their users; the pros and cons that I liked as a user of their website and to identify the features and information they provided. This gave me ideas of how to address my user’s needs but also how I could further improve my user’s experience to add value to the Whey Too Tasty website.


2.	Scope Plane:
    * When addressing the scope plane, I focused on what features were to be included on the website and its key functionality to meet the user’s needs. I also needed to combine these with Javascript as per the requirements for my Code Institute MSP3. I kept in mind the question of: Why would a user want this?
	    * Requirements: ability to find high-protein recipes, ability to create, upload, edit and delete high-protein recipes; ability to share high-protein recipes with others; ability to store recipes in my member account, ability for user’s to buy the website owner’s protein powder.
        * Key features: an easy-to-use form to search for recipes that meet my needs, an simple process to join as a member, a simple process to log in to my member account, an easy-to-use form to create and upload my own recipes, an easy way of editing recipes, a simple method to share recipes with others, a simple way to buy the protein powder the website promotes.

### Technologies Used ###
* [Random Key Gen](https://randomkeygen.com/) to produce the secure passwords used in my project.
* [Coolors](https://coolors.co/616163-17bebb-fafaff-db995a-ff9f1c) to create a professional looking colour palette for my website.
* [Balsamiq](https://balsamiq.com/) used to create my wireframes.
* Jinja - templating language for some of my Python code.
* [jQuery](http://code.jquery.com/)
* [Materialize](https://materializecss.com/getting-started.html) for the main and mobile navbars, accordian collapsible, tooltip template and register form template.
