#main/routes.py
from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/Home")
def Home():
    page = request.args.get('page',1, type = int)
    #creating a post variable to grab all the posts from the database.
    posts = Post.query.order_by(Post.date_posted.desc()).paginate( page = page, per_page = 5 )
    return render_template('home.html', posts = posts)

@main.route("/about")
def About():
    return render_template('about.html', title = 'Abouted')

@main.route("/contact")
def Contact():
    return render_template('contact.html', title = 'Contact_us')


