from website import create_app #can import from python files

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #srun the flask application, only works when we run this file
                        #when true, it makes changes automatically as being changed
                        #change to false when in production
