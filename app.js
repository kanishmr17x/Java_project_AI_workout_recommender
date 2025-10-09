document.addEventListener('DOMContentLoaded', function() {
    const userForm = document.getElementById('userForm');
    userForm.addEventListener('submit', handleFormSubmit);
});

function handleFormSubmit(event) {
    event.preventDefault();
    const formData = getFormData();
    showLoading();
    sendToBackend(formData);
}

function getFormData() {
    const name = document.getElementById('name').value;
    const age = parseInt(document.getElementById('age').value);
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseInt(document.getElementById('height').value);
    const fitnessLevel = document.getElementById('fitnessLevel').value;
    const goal = document.getElementById('goal').value;
    const workoutTime = parseInt(document.getElementById('workoutTime').value);
    
    const heightInMeters = height / 100;
    const bmi = weight / (heightInMeters * heightInMeters);
    
    const userData = {
        name: name,
        age: age,
        weight: weight,
        height: height,
        bmi: bmi,
        fitnessLevel: fitnessLevel,
        goal: goal,
        workoutTime: workoutTime
    };
    
    return userData;
}

function showLoading() {
    document.querySelector('.form-section').style.display = 'none';
    document.getElementById('resultSection').style.display = 'none';
    document.getElementById('loading').style.display = 'block';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function sendToBackend(userData) {
    fetch('http://localhost:8080/api/generate-workout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Java backend not available, trying Python backend...');
        }
        return response.json();
    })
    .then(data => {
        hideLoading();
        showWorkoutResult(data);
    })
    .catch(error => {
        fetch('http://localhost:5000/generate-workout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Python backend not available either');
            }
            return response.json();
        })
        .then(data => {
            hideLoading();
            showWorkoutResult(data);
        })
        .catch(pythonError => {
            hideLoading();
            showLocalWorkout(userData);
        });
    });
}

function showWorkoutResult(workoutData) {
    const resultSection = document.getElementById('resultSection');
    const workoutResult = document.getElementById('workoutResult');
    
    let workoutHTML = `
        <div class="workout-plan">
            <h3>Hello ${workoutData.name || 'there'}! Here's your personalized workout:</h3>
            <p><strong>Goal:</strong> ${formatGoal(workoutData.goal)}</p>
            <p><strong>Duration:</strong> ${workoutData.workoutTime} minutes</p>
            <p><strong>Difficulty:</strong> ${formatFitnessLevel(workoutData.fitnessLevel)}</p>
            
            <h4>Your Workout Plan:</h4>
            <ul>
    `;
    
    if (workoutData.exercises && workoutData.exercises.length > 0) {
        workoutData.exercises.forEach(exercise => {
            workoutHTML += `<li>${exercise.name} - ${exercise.duration || exercise.sets} ${exercise.duration ? 'minutes' : 'sets'}</li>`;
        });
    } else {
        workoutHTML += `<li>No specific exercises provided by backend</li>`;
    }
    
    workoutHTML += `
            </ul>
            
            <h4>Tips:</h4>
            <ul>
                <li>Start with a 5-minute warm-up</li>
                <li>Rest 30-60 seconds between exercises</li>
                <li>Finish with a 5-minute cool-down</li>
                <li>Listen to your body and adjust as needed</li>
            </ul>
        </div>
    `;
    
    workoutResult.innerHTML = workoutHTML;
    resultSection.style.display = 'block';
}

function showLocalWorkout(userData) {
    const resultSection = document.getElementById('resultSection');
    const workoutResult = document.getElementById('workoutResult');
    
    const exercises = generateSimpleWorkout(userData);
    
    let workoutHTML = `
        <div class="workout-plan">
            <h3>Hello ${userData.name}! Here's your personalized workout:</h3>
            <p><strong>Goal:</strong> ${formatGoal(userData.goal)}</p>
            <p><strong>Duration:</strong> ${userData.workoutTime} minutes</p>
            <p><strong>Difficulty:</strong> ${formatFitnessLevel(userData.fitnessLevel)}</p>
            
            <h4>Your Workout Plan:</h4>
            <ul>
    `;
    
    exercises.forEach(exercise => {
        workoutHTML += `<li>${exercise}</li>`;
    });
    
    workoutHTML += `
            </ul>
            
            <h4>Tips:</h4>
            <ul>
                <li>Start with a 5-minute warm-up</li>
                <li>Rest 30-60 seconds between exercises</li>
                <li>Finish with a 5-minute cool-down</li>
                <li>Listen to your body and adjust as needed</li>
            </ul>
        </div>
    `;
    
    workoutResult.innerHTML = workoutHTML;
    resultSection.style.display = 'block';
}

function generateSimpleWorkout(userData) {
    const exercises = [];
    const timePerExercise = Math.floor(userData.workoutTime / 8);
    
    if (userData.fitnessLevel === 'beginner') {
        exercises.push(`Jumping Jacks - ${timePerExercise} minutes`);
        exercises.push(`Bodyweight Squats - ${timePerExercise} minutes`);
        exercises.push(`Push-ups (on knees if needed) - ${timePerExercise} minutes`);
        exercises.push(`Plank - ${Math.max(30, timePerExercise * 30)} seconds`);
        exercises.push(`Lunges - ${timePerExercise} minutes`);
        exercises.push(`Mountain Climbers - ${timePerExercise} minutes`);
        exercises.push(`Burpees (modified) - ${timePerExercise} minutes`);
        exercises.push(`High Knees - ${timePerExercise} minutes`);
    } else if (userData.fitnessLevel === 'intermediate') {
        exercises.push(`Burpees - ${timePerExercise} minutes`);
        exercises.push(`Jump Squats - ${timePerExercise} minutes`);
        exercises.push(`Push-ups - ${timePerExercise} minutes`);
        exercises.push(`Plank - ${Math.max(60, timePerExercise * 30)} seconds`);
        exercises.push(`Walking Lunges - ${timePerExercise} minutes`);
        exercises.push(`Mountain Climbers - ${timePerExercise} minutes`);
        exercises.push(`Jumping Jacks - ${timePerExercise} minutes`);
        exercises.push(`High Knees - ${timePerExercise} minutes`);
    } else {
        exercises.push(`Burpees - ${timePerExercise} minutes`);
        exercises.push(`Pistol Squats (assisted if needed) - ${timePerExercise} minutes`);
        exercises.push(`Diamond Push-ups - ${timePerExercise} minutes`);
        exercises.push(`Plank - ${Math.max(90, timePerExercise * 30)} seconds`);
        exercises.push(`Jumping Lunges - ${timePerExercise} minutes`);
        exercises.push(`Mountain Climbers - ${timePerExercise} minutes`);
        exercises.push(`Tuck Jumps - ${timePerExercise} minutes`);
        exercises.push(`High Knees - ${timePerExercise} minutes`);
    }
    
    return exercises;
}

function formatGoal(goal) {
    const goals = {
        'lose_weight': 'Lose Weight',
        'gain_muscle': 'Gain Muscle',
        'get_fitter': 'Get Fitter',
        'maintain': 'Maintain Current Shape'
    };
    return goals[goal] || goal;
}

function formatFitnessLevel(level) {
    const levels = {
        'beginner': 'Beginner',
        'intermediate': 'Intermediate',
        'advanced': 'Advanced'
    };
    return levels[level] || level;
}

function resetForm() {
    document.getElementById('userForm').reset();
    document.getElementById('resultSection').style.display = 'none';
    document.querySelector('.form-section').style.display = 'block';
}

function showSuccessMessage(message) {
    const form = document.getElementById('userForm');
    const successDiv = document.createElement('div');
    successDiv.className = 'success-message';
    successDiv.textContent = message;
    form.insertBefore(successDiv, form.firstChild);
    
    setTimeout(() => {
        if (successDiv.parentNode) {
            successDiv.parentNode.removeChild(successDiv);
        }
    }, 5000);
}

function showErrorMessage(message) {
    const form = document.getElementById('userForm');
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    form.insertBefore(errorDiv, form.firstChild);
    
    setTimeout(() => {
        if (errorDiv.parentNode) {
            errorDiv.parentNode.removeChild(errorDiv);
        }
    }, 5000);
}
