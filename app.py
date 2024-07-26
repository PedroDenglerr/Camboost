from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/updates')
def update():
    news_updates = get_news_updates()
    return render_template('updates.html', news_updates=news_updates)

@app.route('/updates/<int:update_id>')
def update_detail(update_id):
    news_updates = get_news_updates()
    # Ensure update_id is within valid range
    if 1 <= update_id <= len(news_updates):
        update = news_updates[update_id - 1]  # Adjust for zero-based index
        return render_template('update_detail.html', update=update)
    else:
        return "Update not found", 404

@app.route('/tips')
def tips():
    return render_template("tips.html")

@app.route('/videos')
def videos():
    return render_template("videos.html")

@app.route('/pdfs')
def pdfs():
    return render_template("pdfs.html", mock_pdfs=mock_pdfs, book_pdfs=book_pdfs, writing_pdfs=writing_pdfs, speaking_pdfs=speaking_pdfs, read_pdfs=read_pdfs)


def get_news_updates():
    return [
        {
            'date': '2023-07-15',
            'title': 'Bug Fixes and Enhancements',
            'description': 'We have implemented several bug fixes and performance enhancements.',
            'image': '/static/imagenes/updates/1.jpg',
            'paragraphs': [
                'Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.',
                'Enhanced Security Measures: Upgraded security protocols to safeguard your data and ensure a secure browsing experience.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.',
                'Optimized Load Times: Optimized page load times across various sections of the website, resulting in faster access to content and resources.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.',
                'Backend Refactoring: Leveraging Python, we have refactored critical backend components to improve code efficiency and scalability.',
                'Database Optimization: Implemented database optimizations to streamline data retrieval and storage processes, enhancing overall system performance.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.Improved Stability: We have implemented robust measures to enhance the overall stability of our website, ensuring smoother navigation and reduced downtime.',
                'Algorithmic Improvements: Refined algorithms powering recommendation systems and data processing capabilities, providing more accurate and relevant content suggestions.',
                'User Experience Enhancements: Updated user interface elements for better usability and enhanced user experience, ensuring intuitive navigation and accessibility.',
                'Responsive Design: Enhanced responsiveness across devices, ensuring a seamless browsing experience on desktops, tablets, and mobile devices alike.'
            ]
        },

]

# PDFS SECTION OF DATA BASE - BE CAREFUL #

mock_pdfs = [
        {'date': '2023-01-01', 'title': 'Complete Mock #1', 'img': '/static/imagenes/pdfs/mocks/img/1.jpg', 'pdf_url':'/static/imagenes/pdfs/mocks/1.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Mock #2', 'img': '/static/imagenes/pdfs/mocks/img/2.jpg', 'pdf_url':'/static/imagenes/pdfs/mocks/2.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Mock #3', 'img': '/static/imagenes/pdfs/mocks/img/3.jpg', 'pdf_url':'/static/imagenes/pdfs/mocks/3.pdf'},
]   

book_pdfs = [
        {'date': '2023-03-20', 'title': 'Advanced Grammar Test with Key', 'img': '/static/imagenes/pdfs/books/img/1.jpg', 'pdf_url':'/static/imagenes/pdfs/books/1.pdf'},
        {'date': '2023-03-20', 'title': 'Ready for Advanced workbook with Key', 'img': '/static/imagenes/pdfs/books/img/2.jpg', 'pdf_url':'/static/imagenes/pdfs/books/2.pdf'},
        {'date': '2023-03-20', 'title': 'The Cambridge CAE Course with key', 'img': '/static/imagenes/pdfs/books/img/3.jpg', 'pdf_url':'/static/imagenes/pdfs/books/3.pdf'},
        {'date': '2023-03-20', 'title': 'Common Mistakes at CAE', 'img': '/static/imagenes/pdfs/books/img/4.jpg', 'pdf_url':'/static/imagenes/pdfs/books/4.pdf'},
    # Add more book PDF entries as needed
]

writing_pdfs = [
        {'date': '2023-01-01', 'title': 'How to pass the CAE Writing - Book', 'img': '/static/imagenes/pdfs/writing/img/1.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/1.pdf'},
        {'date': '2023-01-01', 'title': 'CAE Writing Guide - Book', 'img': '/static/imagenes/pdfs/writing/img/2.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/2.pdf'},
        {'date': '2023-01-01', 'title': 'Intercambio Idiomas Online Essay Writing - Book', 'img': '/static/imagenes/pdfs/writing/img/3.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/3.pdf'},
        {'date': '2023-01-01', 'title': 'What policies can we follow to reduce traffic in the town centre? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/4.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/4.pdf'},
        {'date': '2023-01-01', 'title': 'What measures can individuals take to reduce their environmental footprint? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/5.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/5.pdf'},
        {'date': '2023-01-01', 'title': 'What changes can improve the education system? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/6.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/6.pdf'},
        {'date': '2023-01-01', 'title': 'What would be the benefits of a new local TV station? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/7.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/7.pdf'},
        {'date': '2023-01-01', 'title': 'How can individuals protect the environment through their home energy policy? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/8.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/8.pdf'},
        {'date': '2023-01-01', 'title': 'What steps can individuals take to lead a healthier lifestyle? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/9.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/9.pdf'},
        {'date': '2023-01-01', 'title': 'How can technology enhance the learning experience in schools? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/10.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/10.pdf'},
        {'date': '2023-01-01', 'title': 'What urban planning measures can make cities more livable and sustainable? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/11.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/11.pdf'},
        {'date': '2023-01-01', 'title': 'How can working from home be beneficial? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/12.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/12.pdf'},
        {'date': '2023-01-01', 'title': 'How can workplace flexibility benefit both employees and employers? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/13.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/13.pdf'},
        {'date': '2023-01-01', 'title': 'How should the new government money be spent locally? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/14.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/14.pdf'},
        {'date': '2023-01-01', 'title': 'What subjects can we add to our school curriculum? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/15.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/15.pdf'},
        {'date': '2023-01-01', 'title': 'Who should we invite to come and give the annual Spring Term Talk? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/16.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/16.pdf'},
        {'date': '2023-01-01', 'title': 'Which businesses should be given tax incentives to open here? - Part 1', 'img': '/static/imagenes/pdfs/writing/img/17.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/17.pdf'},
        {'date': '2023-01-01', 'title': 'Writing Part 2 - #1', 'img': '/static/imagenes/pdfs/writing/img/18.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/18.pdf'},
        {'date': '2023-01-01', 'title': 'Writing Part 2 - #2', 'img': '/static/imagenes/pdfs/writing/img/19.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/19.pdf'},
        {'date': '2023-01-01', 'title': 'Writing Part 2 - #3', 'img': '/static/imagenes/pdfs/writing/img/20.jpg', 'pdf_url':'/static/imagenes/pdfs/writing/20.pdf'},
]

speaking_pdfs = [
        {'date': '2023-01-01', 'title': 'CAE SPEAKING PRACTICE - Complete Book #1', 'img': '/static/imagenes/pdfs/speaking/img/1.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/1.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #1', 'img': '/static/imagenes/pdfs/speaking/img/2.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/2.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #2', 'img': '/static/imagenes/pdfs/speaking/img/3.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/3.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #3', 'img': '/static/imagenes/pdfs/speaking/img/4.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/4.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #4', 'img': '/static/imagenes/pdfs/speaking/img/5.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/5.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #5', 'img': '/static/imagenes/pdfs/speaking/img/6.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/6.pdf'},
        {'date': '2023-01-01', 'title': 'CAE Speaking materials - Advance material', 'img': '/static/imagenes/pdfs/speaking/img/7.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/7.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #6', 'img': '/static/imagenes/pdfs/speaking/img/8.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/8.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #7', 'img': '/static/imagenes/pdfs/speaking/img/9.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/9.pdf'},
        {'date': '2023-01-01', 'title': 'CAE SPEAKING PRACTICE - Complete Book #2', 'img': '/static/imagenes/pdfs/speaking/img/10.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/10.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #8', 'img': '/static/imagenes/pdfs/speaking/img/11.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/11.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #9', 'img': '/static/imagenes/pdfs/speaking/img/12.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/12.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #10', 'img': '/static/imagenes/pdfs/speaking/img/13.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/13.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Speaking #11', 'img': '/static/imagenes/pdfs/speaking/img/14.jpg', 'pdf_url':'/static/imagenes/pdfs/speaking/14.pdf'},
]

read_pdfs = [
        {'date': '2023-01-01', 'title': 'UOE Exercise #1', 'img': '/static/imagenes/pdfs/ruo/img/1.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/1.pdf'},
        {'date': '2023-01-01', 'title': 'CAE 70 Exercises', 'img': '/static/imagenes/pdfs/ruo/img/2.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/2.pdf'},
        {'date': '2023-01-01', 'title': 'UOE Part 4 Exercises #1', 'img': '/static/imagenes/pdfs/ruo/img/3.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/3.pdf'},
        {'date': '2023-01-01', 'title': 'CAE Test 11 Use of English', 'img': '/static/imagenes/pdfs/ruo/img/4.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/4.pdf'},
        {'date': '2023-01-01', 'title': 'UOE Exercise #2', 'img': '/static/imagenes/pdfs/ruo/img/5.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/5.pdf'},
        {'date': '2023-01-01', 'title': 'UOE Exercise #3', 'img': '/static/imagenes/pdfs/ruo/img/6.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/6.pdf'},
        {'date': '2023-01-01', 'title': 'Ready for CAE coursebook with Key', 'img': '/static/imagenes/pdfs/ruo/img/7.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/7.pdf'},
        {'date': '2023-01-01', 'title': 'UOE Part 4 Exercises #2', 'img': '/static/imagenes/pdfs/ruo/img/8.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/8.pdf'},
        {'date': '2023-01-01', 'title': 'Examining Workers Exploitation Exercise', 'img': '/static/imagenes/pdfs/ruo/img/9.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/9.pdf'},
        {'date': '2023-01-01', 'title': 'Lionel Messi: The Football Legend Exercise', 'img': '/static/imagenes/pdfs/ruo/img/10.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/10.pdf'},
        {'date': '2023-01-01', 'title': 'CAE Practice Tests with Key', 'img': '/static/imagenes/pdfs/ruo/img/11.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/11.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Mock with key #1', 'img': '/static/imagenes/pdfs/ruo/img/12.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/12.pdf'},
        {'date': '2023-01-01', 'title': 'Complete Mock with key #2', 'img': '/static/imagenes/pdfs/ruo/img/13.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/13.pdf'},
        {'date': '2023-01-01', 'title': 'Exam Essentials Practice Test with Key', 'img': '/static/imagenes/pdfs/ruo/img/14.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/14.pdf'},
        {'date': '2023-01-01', 'title': 'Practice Test Plus 2 with Key', 'img': '/static/imagenes/pdfs/ruo/img/15.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/15.pdf'},
        {'date': '2023-01-01', 'title': 'Certificate in Advance English with Key', 'img': '/static/imagenes/pdfs/ruo/img/16.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/16.pdf'},
        {'date': '2023-01-01', 'title': 'Oclock with Key', 'img': '/static/imagenes/pdfs/ruo/img/17.jpg', 'pdf_url':'/static/imagenes/pdfs/ruo/17.pdf'},
]

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/caeai')
def ai():
    return render_template('ai.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/fqas')
def fqas():
    return render_template('fqas.html')

if __name__ == '__main__':
    app.run(debug=True)