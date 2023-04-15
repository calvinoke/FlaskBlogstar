from flaskblog.__init__ import create_app

#from dotenv import load_dotenv, find_dotenv
#load_dotenv(find_dotenv)
#running our app here



app = create_app()





if __name__ == '__main__':
    app.run(debug=True)