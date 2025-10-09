import random
from typing import Dict, List, Any

class WorkoutRecommender:
    def __init__(self):
        self.exercises_database = self._load_exercises()
        self.goal_recommendations = self._load_goal_recommendations()
    
    def _load_exercises(self) -> Dict[str, List[Dict[str, Any]]]:
        return {
            'beginner': [
                {'name': 'Jumping Jacks', 'duration': '5 minutes', 'calories': 50, 'muscle_groups': ['cardio']},
                {'name': 'Bodyweight Squats', 'duration': '5 minutes', 'calories': 60, 'muscle_groups': ['legs']},
                {'name': 'Push-ups (on knees)', 'duration': '5 minutes', 'calories': 40, 'muscle_groups': ['chest', 'arms']},
                {'name': 'Plank', 'duration': '30 seconds', 'calories': 20, 'muscle_groups': ['core']},
                {'name': 'Lunges', 'duration': '5 minutes', 'calories': 55, 'muscle_groups': ['legs']},
                {'name': 'Mountain Climbers', 'duration': '5 minutes', 'calories': 70, 'muscle_groups': ['cardio', 'core']},
                {'name': 'Modified Burpees', 'duration': '5 minutes', 'calories': 80, 'muscle_groups': ['full_body']},
                {'name': 'High Knees', 'duration': '5 minutes', 'calories': 45, 'muscle_groups': ['cardio']},
                {'name': 'Wall Sits', 'duration': '1 minute', 'calories': 25, 'muscle_groups': ['legs']},
                {'name': 'Arm Circles', 'duration': '2 minutes', 'calories': 15, 'muscle_groups': ['arms']}
            ],
            'intermediate': [
                {'name': 'Burpees', 'duration': '5 minutes', 'calories': 100, 'muscle_groups': ['full_body']},
                {'name': 'Jump Squats', 'duration': '5 minutes', 'calories': 80, 'muscle_groups': ['legs']},
                {'name': 'Push-ups', 'duration': '5 minutes', 'calories': 60, 'muscle_groups': ['chest', 'arms']},
                {'name': 'Plank', 'duration': '60 seconds', 'calories': 40, 'muscle_groups': ['core']},
                {'name': 'Walking Lunges', 'duration': '5 minutes', 'calories': 70, 'muscle_groups': ['legs']},
                {'name': 'Mountain Climbers', 'duration': '5 minutes', 'calories': 85, 'muscle_groups': ['cardio', 'core']},
                {'name': 'Jumping Jacks', 'duration': '5 minutes', 'calories': 60, 'muscle_groups': ['cardio']},
                {'name': 'High Knees', 'duration': '5 minutes', 'calories': 55, 'muscle_groups': ['cardio']},
                {'name': 'Diamond Push-ups', 'duration': '5 minutes', 'calories': 65, 'muscle_groups': ['chest', 'arms']},
                {'name': 'Side Plank', 'duration': '30 seconds each side', 'calories': 30, 'muscle_groups': ['core']}
            ],
            'advanced': [
                {'name': 'Burpees', 'duration': '5 minutes', 'calories': 120, 'muscle_groups': ['full_body']},
                {'name': 'Pistol Squats', 'duration': '5 minutes', 'calories': 100, 'muscle_groups': ['legs']},
                {'name': 'Diamond Push-ups', 'duration': '5 minutes', 'calories': 80, 'muscle_groups': ['chest', 'arms']},
                {'name': 'Plank', 'duration': '90 seconds', 'calories': 60, 'muscle_groups': ['core']},
                {'name': 'Jumping Lunges', 'duration': '5 minutes', 'calories': 90, 'muscle_groups': ['legs']},
                {'name': 'Mountain Climbers', 'duration': '5 minutes', 'calories': 100, 'muscle_groups': ['cardio', 'core']},
                {'name': 'Tuck Jumps', 'duration': '5 minutes', 'calories': 85, 'muscle_groups': ['cardio']},
                {'name': 'High Knees', 'duration': '5 minutes', 'calories': 70, 'muscle_groups': ['cardio']},
                {'name': 'One-Arm Push-ups', 'duration': '5 minutes', 'calories': 90, 'muscle_groups': ['chest', 'arms']},
                {'name': 'L-Sit', 'duration': '30 seconds', 'calories': 40, 'muscle_groups': ['core']}
            ]
        }
    
    def _load_goal_recommendations(self) -> Dict[str, Dict[str, Any]]:
        return {
            'lose_weight': {
                'focus': 'cardio',
                'intensity': 'high',
                'rest_time': '30-45 seconds',
                'tips': [
                    'Focus on cardio exercises',
                    'Increase workout intensity',
                    'Maintain a calorie deficit',
                    'Stay consistent with workouts'
                ]
            },
            'gain_muscle': {
                'focus': 'strength',
                'intensity': 'moderate',
                'rest_time': '60-90 seconds',
                'tips': [
                    'Focus on strength exercises',
                    'Progressive overload',
                    'Eat enough protein',
                    'Allow for rest and recovery'
                ]
            },
            'get_fitter': {
                'focus': 'balanced',
                'intensity': 'moderate',
                'rest_time': '45-60 seconds',
                'tips': [
                    'Mix cardio and strength',
                    'Gradually increase difficulty',
                    'Stay consistent',
                    'Listen to your body'
                ]
            },
            'maintain': {
                'focus': 'maintenance',
                'intensity': 'low-moderate',
                'rest_time': '30-60 seconds',
                'tips': [
                    'Keep current routine',
                    'Mix up exercises',
                    'Stay active daily',
                    'Enjoy the process'
                ]
            }
        }
    
    def generate_workout(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        name = user_data.get('name', 'Friend')
        age = user_data.get('age', 25)
        weight = user_data.get('weight', 70)
        height = user_data.get('height', 170)
        bmi = user_data.get('bmi', 22)
        fitness_level = user_data.get('fitnessLevel', 'beginner')
        goal = user_data.get('goal', 'get_fitter')
        workout_time = user_data.get('workoutTime', 30)
        
        workout_plan = {
            'name': name,
            'age': age,
            'weight': weight,
            'height': height,
            'bmi': round(bmi, 2),
            'fitnessLevel': fitness_level,
            'goal': goal,
            'workoutTime': workout_time,
            'generated_by': 'AI Engine',
            'exercises': [],
            'total_calories': 0,
            'recommendations': []
        }
        
        selected_exercises = self._select_exercises(fitness_level, goal, workout_time)
        workout_plan['exercises'] = selected_exercises
        
        total_calories = sum(exercise.get('calories', 0) for exercise in selected_exercises)
        workout_plan['total_calories'] = total_calories
        
        recommendations = self._get_recommendations(goal, fitness_level, age, bmi)
        workout_plan['recommendations'] = recommendations
        
        goal_info = self.goal_recommendations.get(goal, {})
        workout_plan['tips'] = goal_info.get('tips', [])
        
        return workout_plan
    
    def _select_exercises(self, fitness_level: str, goal: str, workout_time: int) -> List[Dict[str, Any]]:
        available_exercises = self.exercises_database.get(fitness_level, self.exercises_database['beginner'])
        
        max_exercises = min(len(available_exercises), workout_time // 5)
        max_exercises = max(4, max_exercises)  # At least 4 exercises
        
        selected_exercises = []
        
        if goal == 'lose_weight':
            cardio_exercises = [ex for ex in available_exercises if 'cardio' in ex['muscle_groups'] or 'full_body' in ex['muscle_groups']]
            selected_exercises.extend(cardio_exercises[:max_exercises//2])
            
            strength_exercises = [ex for ex in available_exercises if 'cardio' not in ex['muscle_groups']]
            selected_exercises.extend(strength_exercises[:max_exercises//2])
            
        elif goal == 'gain_muscle':
            strength_exercises = [ex for ex in available_exercises if 'cardio' not in ex['muscle_groups']]
            selected_exercises.extend(strength_exercises[:max_exercises])
            
        else:  # get_fitter or maintain
            selected_exercises.extend(available_exercises[:max_exercises])
        
        while len(selected_exercises) < max_exercises and len(selected_exercises) < len(available_exercises):
            remaining_exercises = [ex for ex in available_exercises if ex not in selected_exercises]
            if remaining_exercises:
                selected_exercises.append(random.choice(remaining_exercises))
            else:
                break
        
        time_per_exercise = workout_time // len(selected_exercises)
        for exercise in selected_exercises:
            if 'minutes' in exercise['duration']:
                exercise['duration'] = f"{time_per_exercise} minutes"
        
        return selected_exercises
    
    def _get_recommendations(self, goal: str, fitness_level: str, age: int, bmi: float) -> List[str]:
        recommendations = []
        
        if age < 18:
            recommendations.append("You're young! Focus on building healthy habits.")
        elif age > 50:
            recommendations.append("Consider low-impact exercises and consult a doctor if needed.")
        
        if bmi < 18.5:
            recommendations.append("Focus on building muscle and healthy weight gain.")
        elif bmi > 25:
            recommendations.append("Combine cardio and strength training for best results.")
        
        if fitness_level == 'beginner':
            recommendations.append("Start slow and gradually increase intensity.")
        elif fitness_level == 'advanced':
            recommendations.append("Push yourself but listen to your body.")
        
        goal_info = self.goal_recommendations.get(goal, {})
        if goal_info:
            recommendations.extend(goal_info.get('tips', []))
        
        return recommendations
    
    def get_exercises_for_level(self, fitness_level: str, goal: str) -> List[Dict[str, Any]]:
        exercises = self.exercises_database.get(fitness_level, [])
        
        if goal == 'lose_weight':
            exercises = sorted(exercises, key=lambda x: 1 if 'cardio' in x['muscle_groups'] or 'full_body' in x['muscle_groups'] else 2)
        elif goal == 'gain_muscle':
            exercises = sorted(exercises, key=lambda x: 1 if 'cardio' not in x['muscle_groups'] else 2)
        
        return exercises

