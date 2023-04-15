from flask import (render_template, url_for, flash,
	               redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog.__init__ import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts= Blueprint('posts', __name__)


@posts.route("/post/new", methods = ['GET', 'POST'])
#login_reuired decorator requires a user to be logged in.
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		post = Post(title = form.title.data, content = form.content.data, author = current_user)
		#adding the new post to the database will make it accessible to the admin user
		db.session.add(post)
		db.session.commit()
		flash('Your post has been created successfully.', 'success')
		return redirect(url_for('main.Home'))
	return render_template('create_post.html', title = 'New Post', form = form, legend = 'New Post')


#grabbing a route with the id of the post and the name of the post to the post model.
@posts.route("/post/<int:post_id>")
def postid(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('postid.html', title = post.title, post = post)

#route for updating the post status
@posts.route("/post/<int:post_id>/update", methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit:
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated successfully.', 'success')
        return redirect (url_for('posts.postid', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        return render_template('create_post.html', title = 'Update Post', form = form, legend = 'Update Post')


#route for deleting the post status
@posts.route("/post/<int:post_id>delete", methods = ['POST'])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	#registered and current user should update the status of the post otherwise abort the request.
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Your post has been deleted successfully.', 'success')
	return redirect(url_for('main.Home'))

