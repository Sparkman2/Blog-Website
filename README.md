# Blog-Website
The website I created is a blog. In this website, you have to login to post. 
You cannot make a post if you login, so If you try to go to the post page without logging in, it will give you an unauthorized page. 
The posts are organized from the latest and the top to the earliest at the bottom. 
Basically, you just get to see what everyone who uses this posts!

# Running the Project
Download the project from Github. I use an IDE (Pycharm) and open the folder of the project.
Make sure to run requirments.txt or to download all the packages.
To run the code you can either run app.py on the IDE or use the code "python app.py"

# Navigation
When you run the app first then you will be taken to main page where it has all the posts. You can’t create a post until you login.
You go to the register and create and account but if the username you wanted is taken, it will not let you create an account.
Once you create an account you go to the login page and then type in the username and password you created.
You can also click the remember me button if you want to stay logged in. Once you successfully login, you can create a post.

# URLS
http://127.0.0.1:5000/index  This is the home page

http://127.0.0.1:5000/login   This is the login page

http://127.0.0.1:5000/register   This is the register page

http://127.0.0.1:5000/post   This is the post page, you can only access while logged in
