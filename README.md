# 💪 FitGenie - Personal Fitness Assistant

A beginner-friendly fitness application that generates personalized workout plans based on your goals, fitness level, and available time.

## 🎯 What is FitGenie?

FitGenie is a simple web application that acts like your personal fitness trainer. You tell it about yourself (age, weight, fitness level, goals), and it creates a custom workout plan just for you!

## 🏗️ Project Structure

```
fitgenie-beginner/
│
├── frontend/                  # Frontend files (HTML, CSS, JavaScript)
│   ├── index.html             # Main landing page
│   ├── style.css              # CSS (dark + gold theme)
│   └── app.js                 # JavaScript for form & API calls
│
├── backend/                   # Java backend with Spring Boot & Maven
│   ├── pom.xml                # Maven configuration
│   └── src/
│       └── main/java/
│           └── FitGenieApplication.java    # All backend code in one file
│
├── ai_engine/                 # Python AI engine
│   ├── api.py                 # Flask app to generate workouts
│   ├── recommender.py         # Simple AI logic (rule-based)
│   └── requirements.txt       # Python dependencies
│
└── README.md                  # This file - setup instructions
```

## 🚀 How to Run FitGenie

### Prerequisites

Make sure you have these installed on your computer:

1. **Java 17 or higher** - Download from [Oracle](https://www.oracle.com/java/technologies/downloads/) or [OpenJDK](https://openjdk.org/)
2. **Python 3.8 or higher** - Download from [python.org](https://www.python.org/downloads/)
3. **Maven** - Download from [maven.apache.org](https://maven.apache.org/download.cgi)
4. **Web Browser** - Any modern browser (Chrome, Firefox, Safari, Edge)

### Step 1: Start the Python AI Engine

1. Open your terminal/command prompt
2. Navigate to the `ai_engine` folder:
   ```bash
   cd fitgenie-beginner/ai_engine
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Python server:
   ```bash
   python api.py
   ```

   You should see: `Running on http://127.0.0.1:5000`

### Step 2: Start the Java Backend

1. Open a **new** terminal/command prompt window
2. Navigate to the `backend` folder:
   ```bash
   cd fitgenie-beginner/backend
   ```

3. Run the Java application:
   ```bash
   mvn spring-boot:run
   ```

   You should see: `FitGenie Backend is running on http://localhost:8080`

### Step 3: Open the Frontend

1. Open your web browser
2. Navigate to the `frontend` folder in your file explorer
3. Double-click on `index.html` to open it in your browser
   
   **OR** open your browser and go to:
   ```
   file:///path/to/fitgenie-beginner/frontend/index.html
   ```

### Step 4: Use FitGenie!

1. Fill out the form with your information:
   - Name, Age, Weight, Height
   - Fitness Level (Beginner/Intermediate/Advanced)
   - Goal (Lose Weight/Gain Muscle/Get Fitter/Maintain)
   - Available Workout Time

2. Click "Generate My Workout Plan"

3. Get your personalized workout! 💪

## 🔧 Troubleshooting

### If the Python AI Engine won't start:
- Make sure Python is installed: `python --version`
- Install Flask: `pip install Flask Flask-CORS`
- Check if port 5000 is already in use

### If the Java Backend won't start:
- Make sure Java is installed: `java -version`
- Make sure Maven is installed: `mvn --version`
- Check if port 8080 is already in use

### If the frontend won't connect:
- Make sure both backend services are running
- Check the browser console for error messages
- Try refreshing the page

## 🎨 Features

- **Personalized Workouts**: Based on your fitness level and goals
- **Multiple Fitness Levels**: Beginner, Intermediate, Advanced
- **Flexible Time**: 15-90 minute workout options
- **Smart Recommendations**: AI-powered exercise selection
- **Beautiful UI**: Dark theme with gold accents
- **Responsive Design**: Works on desktop and mobile

## 🧠 How It Works

1. **Frontend** (HTML/CSS/JavaScript): Collects user information and displays results
2. **Java Backend**: Handles requests and can generate basic workouts
3. **Python AI Engine**: Uses smart algorithms to create personalized workout plans
4. **Fallback System**: If one service is down, the others still work!

## 🎯 Fitness Goals Supported

- **Lose Weight**: Cardio-focused workouts with high calorie burn
- **Gain Muscle**: Strength-focused exercises for muscle building
- **Get Fitter**: Balanced mix of cardio and strength training
- **Maintain**: Easy maintenance workouts to stay in shape

## 🏃‍♀️ Exercise Types

### Beginner Level:
- Jumping Jacks, Bodyweight Squats, Modified Push-ups
- Planks, Lunges, Mountain Climbers

### Intermediate Level:
- Burpees, Jump Squats, Regular Push-ups
- Side Planks, Walking Lunges

### Advanced Level:
- Pistol Squats, Diamond Push-ups, One-Arm Push-ups
- L-Sits, Tuck Jumps

## 🔄 How the AI Works

The AI engine uses simple rule-based logic (perfect for beginners to understand):

1. **Analyzes** your fitness level, goal, and available time
2. **Selects** appropriate exercises from a database
3. **Calculates** workout duration for each exercise
4. **Provides** personalized tips and recommendations
5. **Estimates** calorie burn for the workout

## 📱 Browser Compatibility

- ✅ Chrome
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Java 17, Spring Boot 3.2.0
- **AI Engine**: Python 3.8+, Flask 2.3.3
- **Build Tool**: Maven
- **Styling**: Custom CSS with dark/gold theme

## 🎓 Learning Objectives

This project is designed to teach:
- **Web Development**: HTML, CSS, JavaScript
- **Backend Development**: Java Spring Boot, REST APIs
- **AI/ML Basics**: Rule-based recommendation systems
- **Full-Stack Integration**: Connecting frontend, backend, and AI services
- **Project Structure**: Organizing code in a professional way

## 🤝 Contributing

This is a beginner project, but if you want to improve it:
1. Add more exercise variations
2. Improve the AI recommendation logic
3. Add user accounts and workout history
4. Create a mobile app version
5. Add more fitness goals and customization

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Need Help?

If you get stuck:
1. Check the troubleshooting section above
2. Make sure all services are running
3. Check the console for error messages
4. Try restarting the services
5. Ask for help from your instructor or classmates

---

**Happy Working Out! 💪**

*Remember: Always consult with a healthcare professional before starting any new exercise program.*
