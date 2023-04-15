import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog.__init__ import mail
from flask import current_app



def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn= random_hex + f_ext
	#including the extension on our profile_pic file
	#To save the pics we upload from the website, we need to create a profile_pic file
	picture_path = os.path.join (current_app.root_path, 'static/profile_pic', picture_fn)
	form_picture.save(picture_path)
	#Resizing large images using Pillow(PIL)
	#PIL.Image.Image.draft method to configure the file reader 
	# (where applicable), and finally resizes the image.
	output_size= (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn




#creating a method for sending reset password.
def send_reset_email(user):
    token= user.get_reset_token()
    msg= Message('Password Reset Request',
                 sender= 'calvinoker8@gmail.com',
                 recipients= [user.email])
    msg.body= f'''To reset your password, visit the following link:
    {url_for('users.reset_token', token= token, _external= True)}
    if you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)