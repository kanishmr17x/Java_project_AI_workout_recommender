# Java_project_AI_workout_recommender
##  Functions Used in Project

### 1. **UserProfile (Entity)**
- `getId() / setId(Long id)` → Manage user ID  
- `getAge() / setAge(int age)` → Access user’s age  
- `getHeight() / setHeight(double height)` → Access height (cm)  
- `getWeight() / setWeight(double weight)` → Access weight (kg)  
- `getGender() / setGender(String gender)` → Access gender  
- `getFitnessGoal() / setFitnessGoal(String goal)` → Get/set user’s goal (e.g., weight loss, strength)  
- `getLevel() / setLevel(String level)` → Get/set fitness level  
- `getWorkoutDuration() / setWorkoutDuration(int mins)` → Duration of workouts  
- `getEquipment() / setEquipment(String equipment)` → Available equipment  

---

### 2. **Workout (Entity)**
- `getId() / setId(Long id)` → Workout ID  
- `getName() / setName(String name)` → Exercise name (e.g., Push-ups)  
- `getMuscleGroup() / setMuscleGroup(String group)` → Targeted muscle group  
- `getDifficulty() / setDifficulty(String difficulty)` → Beginner / Intermediate / Advanced  
- `getEquipment() / setEquipment(String equipment)` → Equipment required  
- `getDuration() / setDuration(int duration)` → Estimated workout duration  

---

### 3. **WorkoutRecommenderService (Service Layer)**
- `recommendWorkouts(UserProfile user)`  
  - Input: UserProfile  
  - Output: List of recommended workouts  
  - Logic: Filters workouts by level, equipment, and goal  

- `matchGoal(String goal, String muscleGroup)`  
  - Matches workouts to fitness goals  
  - Example:  
    - *weight_loss → cardio/compound movements*  
    - *strength → strength-based workouts*  

- `safe(String input)`  
  - Utility to avoid null errors and normalize strings  

---

### 4. **WorkoutController (REST Controller)**
- `getRecommendations(UserProfile user)`  
  - Endpoint: `POST /api/recommend`  
  - Accepts JSON body of `UserProfile`  
  - Returns: JSON list of workouts  

---

### 5. **DataLoader (Config)**
- `seedWorkouts(WorkoutRepository repo)`  
  - Seeds default workouts into the database when the app starts  

---

##  Example API Call
**POST** `/api/recommend`  
Request:
```json
{
  "age": 25,
  "height": 175,
  "weight": 70,
  "gender": "male",
  "fitnessGoal": "strength",
  "level": "beginner",
  "workoutDuration": 45,
  "equipment": "dumbbells,bodyweight"
}
