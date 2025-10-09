#  FitGenie - Personal Fitness Assistant

A beginner-friendly fitness application that generates personalized workout plans based on your goals, fitness level, and available time.

##  What is FitGenie?

FitGenie is a simple web application that acts like your personal fitness trainer. You tell it about yourself (age, weight, fitness level, goals), and it creates a custom workout plan just for you!

##  Project Structure

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

##  Features

- **Personalized Workouts**: Based on your fitness level and goals
- **Multiple Fitness Levels**: Beginner, Intermediate, Advanced
- **Flexible Time**: 15-90 minute workout options
- **Smart Recommendations**: AI-powered exercise selection
- **Beautiful UI**: Dark theme with gold accents
- **Responsive Design**: Works on desktop and mobile

##  How It Works

1. **Frontend** (HTML/CSS/JavaScript): Collects user information and displays results
2. **Java Backend**: Handles requests and can generate basic workouts
3. **Python AI Engine**: Uses smart algorithms to create personalized workout plans
4. **Fallback System**: If one service is down, the others still work!

##  Fitness Goals Supported

- **Lose Weight**: Cardio-focused workouts with high calorie burn
- **Gain Muscle**: Strength-focused exercises for muscle building
- **Get Fitter**: Balanced mix of cardio and strength training
- **Maintain**: Easy maintenance workouts to stay in shape

##  Exercise Types

### Beginner Level:
- Jumping Jacks, Bodyweight Squats, Modified Push-ups
- Planks, Lunges, Mountain Climbers

### Intermediate Level:
- Burpees, Jump Squats, Regular Push-ups
- Side Planks, Walking Lunges

### Advanced Level:
- Pistol Squats, Diamond Push-ups, One-Arm Push-ups
- L-Sits, Tuck Jumps

##  How the AI Works

The AI engine uses simple rule-based logic (perfect for beginners to understand):

1. **Analyzes** your fitness level, goal, and available time
2. **Selects** appropriate exercises from a database
3. **Calculates** workout duration for each exercise
4. **Provides** personalized tips and recommendations
5. **Estimates** calorie burn for the workout

##  Browser Compatibility

-  Chrome
-  Firefox
-  Safari
-  Edge
-  Mobile browsers

##  Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Java 17, Spring Boot 3.2.0
- **AI Engine**: Python 3.8+, Flask 2.3.3
- **Build Tool**: Maven
- **Styling**: Custom CSS with dark/gold theme


##  Contributing

This is a beginner project, but if you want to improve it:
1. Add more exercise variations
2. Improve the AI recommendation logic
3. Add user accounts and workout history
4. Create a mobile app version
5. Add more fitness goals and customization



---

**Happy Working Out! **

*Remember: Always consult with a healthcare professional before starting any new exercise program.*

