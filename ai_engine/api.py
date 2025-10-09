from flask import Flask, request, jsonify
from flask_cors import CORS
from recommender import WorkoutRecommender

app = Flask(__name__)
CORS(app)
workout_recommender = WorkoutRecommender()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'FitGenie AI Engine is running!',
        'engine': 'Python Flask'
    })

@app.route('/generate-workout', methods=['POST'])
def generate_workout():
    try:
        user_data = request.get_json()
        required_fields = ['name', 'age', 'weight', 'height', 'fitnessLevel', 'goal', 'workoutTime']
        for field in required_fields:
            if field not in user_data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        workout_plan = workout_recommender.generate_workout(user_data)
        return jsonify(workout_plan)
    except Exception as e:
        return jsonify({'error': 'Failed to generate workout plan'}), 500

@app.route('/get-exercises', methods=['POST'])
def get_exercises():
    try:
        data = request.get_json()
        fitness_level = data.get('fitnessLevel', 'beginner')
        goal = data.get('goal', 'get_fitter')
        exercises = workout_recommender.get_exercises_for_level(fitness_level, goal)
        return jsonify({
            'fitnessLevel': fitness_level,
            'goal': goal,
            'exercises': exercises
        })
    except Exception as e:
        return jsonify({'error': 'Failed to get exercises'}), 500

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.get_json()
        weight = float(data.get('weight'))
        height = float(data.get('height'))
        height_in_meters = height / 100
        bmi = weight / (height_in_meters * height_in_meters)
        
        if bmi < 18.5:
            category = "Underweight"
            recommendation = "Focus on building muscle and healthy weight gain"
        elif bmi < 25:
            category = "Normal weight"
            recommendation = "Maintain your healthy lifestyle"
        elif bmi < 30:
            category = "Overweight"
            recommendation = "Focus on cardio and strength training to lose weight"
        else:
            category = "Obese"
            recommendation = "Start with low-impact exercises and consult a doctor"
        
        return jsonify({
            'bmi': round(bmi, 2),
            'category': category,
            'recommendation': recommendation
        })
    except Exception as e:
        return jsonify({'error': 'Failed to calculate BMI'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
