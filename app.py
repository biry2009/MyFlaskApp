from flask import Flask, render_template, flash

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("base.html")

@app.route('/about')
def about_page():
    title = "about"
    return render_template("about.html", title=title)

@app.route('/review')
def review_page():
    title = "review"
    return render_template("review.html", title=title)

@app.route('/contact')
def contact_page():
    title = "contact"
    return render_template("contact.html", title=title)

@app.route('/tlds/<domain_name>')
def domain_extension(domain_name):
    return render_template("tld_base.html", domain_name=domain_name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.secret_key = 'here-you-are'
if __name__ == '__main__':
    app.run(debug=True)
