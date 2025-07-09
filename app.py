from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rules
rules = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! Ask me anything about Tamizhan Skills.",
    "good morning": "Good morning! Hope you're doing well.",
    "good evening": "Good evening! How can I assist you?",
    "about tamizhan": "Tamizhan Skills is an initiative offering various skill development courses.",
    "tamizhan skills": "Tamizhan Skills is an initiative offering various skill development courses.",
    "courses": "We offer courses in Python, Web Development, AI, Communication, and more!",
    "enroll": "You can enroll through our official website or contact support.",
    "duration": "Most courses last between 4 to 12 weeks.",
    "certificate": "Yes, we provide certificates upon successful course completion.",
    "fees": "Most courses are free. Some premium courses may have a small fee.",
    "support": "You can contact support at support@tamizhanskills.org.",
    "ok": "Thank you, buddy!",
    "thanks": "You're welcome! Let me know if you need anything else.",
    "thank you": "You're welcome! Happy to help.",
    "how to join": "You can join by signing up on our website and choosing your preferred course.",
    "contact": "Reach us at support@tamizhanskills.org or call +91-9876543210.",
    "location": "We are based in Tamil Nadu, India but offer online courses worldwide.",
    "timings": "You can access the courses anytime! They're fully online and flexible.",
    "job assistance": "Yes, we provide guidance and assistance with job opportunities after course completion.",
    "internship": "Some courses include internship opportunities. Check the course details for more info.",
    "ai course": "Our AI course covers Machine Learning, Deep Learning, and real-world projects.",
    "web development": "Our Web Development course teaches HTML, CSS, JavaScript, Flask, and more.",
    "python": "Our Python course is beginner-friendly and also includes advanced concepts."
}


def chatbot_response(user_input):
    user_input = user_input.lower()
    for key, response in rules.items():
        if key in user_input:
            return response
    return "Sorry, I didn't understand that. Can you try again?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form["msg"]
    response = chatbot_response(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
