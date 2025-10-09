package com.fitgenie;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@SpringBootApplication
@RestController
@CrossOrigin(origins = "*")
public class FitGenieApplication {

    public static void main(String[] args) {
        SpringApplication.run(FitGenieApplication.class, args);
    }

    @PostMapping("/api/generate-workout")
    public Map<String, Object> generateWorkout(@RequestBody UserData userData) {
        Map<String, Object> workoutPlan = new HashMap<>();
        workoutPlan.put("name", userData.getName());
        workoutPlan.put("goal", userData.getGoal());
        workoutPlan.put("fitnessLevel", userData.getFitnessLevel());
        workoutPlan.put("workoutTime", userData.getWorkoutTime());
        
        List<Map<String, String>> exerciseList = createExerciseList(userData.getFitnessLevel(), userData.getWorkoutTime());
        workoutPlan.put("exercises", exerciseList);
        
        List<String> helpfulTips = Arrays.asList(
            " Start with a 5-minute warm-up",
            " Rest between exercises",
            " Finish with a cool-down",
            " Listen to your body"
        );
        workoutPlan.put("tips", helpfulTips);
        
        return workoutPlan;
    }

    private List<Map<String, String>> createExerciseList(String fitnessLevel, int totalWorkoutTime) {
        List<Map<String, String>> exerciseList = new ArrayList<>();
        int timeForEachExercise = totalWorkoutTime / 6;
        
        if ("beginner".equals(fitnessLevel)) {
            exerciseList.add(makeNewExercise("Jumping Jacks", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Squats", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Push-ups (on knees)", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Plank", "30 seconds"));
            exerciseList.add(makeNewExercise("Lunges", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("High Knees", timeForEachExercise + " minutes"));
        } else if ("intermediate".equals(fitnessLevel)) {
            exerciseList.add(makeNewExercise("Burpees", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Jump Squats", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Push-ups", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Plank", "60 seconds"));
            exerciseList.add(makeNewExercise("Walking Lunges", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("High Knees", timeForEachExercise + " minutes"));
        } else {
            exerciseList.add(makeNewExercise("Burpees", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Pistol Squats", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Diamond Push-ups", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Plank", "90 seconds"));
            exerciseList.add(makeNewExercise("Jumping Lunges", timeForEachExercise + " minutes"));
            exerciseList.add(makeNewExercise("Tuck Jumps", timeForEachExercise + " minutes"));
        }
        
        return exerciseList;
    }
    
    private Map<String, String> makeNewExercise(String exerciseName, String howLongToDoIt) {
        Map<String, String> singleExercise = new HashMap<>();
        singleExercise.put("name", exerciseName);
        singleExercise.put("duration", howLongToDoIt);
        return singleExercise;
    }

    @GetMapping("/api/health")
    public Map<String, String> healthCheck() {
        Map<String, String> healthReport = new HashMap<>();
        healthReport.put("status", "healthy");
        healthReport.put("message", "FitGenie backend is running perfectly!");
        healthReport.put("emoji", "$");
        return healthReport;
    }

    public static class UserData {
        public String name;
        public int age;
        public double weight;
        public int height;
        public double bmi;
        public String fitnessLevel;
        public String goal;
        public int workoutTime;
        
        public UserData() {}
        
        public String getName() { return name; }
        public String getFitnessLevel() { return fitnessLevel; }
        public String getGoal() { return goal; }
        public int getWorkoutTime() { return workoutTime; }
    }
}
