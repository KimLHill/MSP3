import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Routes user to index page as default
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Routing for the recipes page
@app.route("/recipes")
# find recipes from MongoDB database and render to recipes template
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Routing for the register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists within the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # message to alert user that the username already exists
            flash("Username already exists, please try again")
            # return user to register page to try again
            return redirect(url_for("register"))
        
        # else if no existing user, register user
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        # message to alert user that their registration was successful
        flash ("Registration successful")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Routing for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # if username matches a username in database
        if existing_user:
            # check hashed password matches user input, welcome user
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))
        
        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))
            
    return render_template("login.html")


# Routing for the user profile page
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    # if session["user"] cookie is true, return user profile
    if session["user"]:
        return render_template("profile.html", username=username)
    
    # else redirect user to login page
    return redirect(url_for("login"))


# Routing for the logout
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have successfully logged out")
    session.pop("user")
    # redirect user to login page
    return redirect(url_for("login"))


# Routing for the add recipe page
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        is_easy = "on" if request.form.get("is_easy") else "off"
        # get add recipe form inputs to add to database
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "is_easy": is_easy,
            "title_ingredients": request.form.get("title_ingredients"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "title_method": request.form.get("title_method"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_calories": request.form.get("recipe_calories"),
            "recipe_protein": request.form.get("recipe_protein"),
            "recipe_carbohydrate": request.form.get("recipe_carbohydrate"),
            "recipe_fat": request.form.get("recipe_fat"),
            "created_by": session["user"]
        }
        # insert into database
        mongo.db.recipes.insert_one(recipe)
        # success message
        flash("Recipe successfully added")
        # return user to recipe page
        return redirect(url_for("recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# Routing for the edit recipe page
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_easy = "on" if request.form.get("is_easy") else "off"
        # get add recipe form inputs to add to database
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "is_easy": is_easy,
            "title_ingredients": request.form.get("title_ingredients"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "title_method": request.form.get("title_method"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_calories": request.form.get("recipe_calories"),
            "recipe_protein": request.form.get("recipe_protein"),
            "recipe_carbohydrate": request.form.get("recipe_carbohydrate"),
            "recipe_fat": request.form.get("recipe_fat"),
            "created_by": session["user"]
        }
        # find recipe in database and update with new form details
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        # success message
        flash("Recipe successfully updated")
        
    # find the recipe in database
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Routing for the edit recipe page
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # find recipe in database and remove
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    # success message
    flash("Recipe successfully deleted")
    # return user to recipe page
    return redirect(url_for("recipes"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
