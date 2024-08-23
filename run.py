from flaskr import create_app  # Replace 'your_package_name' with the actual package name

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)