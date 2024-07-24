from flask import Flask, render_template, request, flash, redirect, url_for
from contactForm import ContactForm , validators # Adjust the import if needed

app = Flask(__name__)
app.secret_key = 'devkey'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            flash("Form submitted successfully!")
            # Process form data here
            return redirect(url_for('success'))  # Redirect to avoid re-submit
        else:
            flash("All fields are required.")
            return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)
@app.route('/success')
def success():
    return render_template('success.html')
if __name__ == '__main__':
    app.run(port=5001, debug=True)
