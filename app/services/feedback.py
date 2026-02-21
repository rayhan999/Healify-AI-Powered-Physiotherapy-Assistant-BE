from typing import List, Dict

# Joint names mapping
JOINT_NAMES = {
    0: 'nose', 11: 'left_shoulder', 12: 'right_shoulder',
    13: 'left_elbow', 14: 'right_elbow',
    15: 'left_wrist', 16: 'right_wrist',
    23: 'left_hip', 24: 'right_hip',
    25: 'left_knee', 26: 'right_knee',
    27: 'left_ankle', 28: 'right_ankle'
}

# Exercise-specific feedback
EXERCISE_FEEDBACK = {
    'jumping_jack': {
        15: "Raise your left arm higher - it's not reaching overhead",
        16: "Raise your right arm higher - it's not reaching overhead",
        13: "Extend your left arm more fully",
        14: "Extend your right arm more fully",
        11: "Keep your left shoulder stable",
        12: "Keep your right shoulder stable",
        25: "Spread your left leg wider",
        26: "Spread your right leg wider",
        23: "Keep your left hip aligned",
        24: "Keep your right hip aligned",
        0: "Keep your head steady and look forward"
    },
    'squat': {
        25: "Bend your left knee more",
        26: "Bend your right knee more",
        23: "Push your hips back more",
        24: "Keep your hips level",
        0: "Keep your chest up and eyes forward"
    },
    'pushup': {
        13: "Lower your left elbow more",
        14: "Lower your right elbow more",
        11: "Keep your shoulders aligned",
        23: "Don't let your hips sag"
    }
}

# Generic feedback templates
GENERIC_FEEDBACK = {
    'excellent': "Excellent form! Keep it up! 💪",
    'good': "Good form! Minor improvements possible.",
    'fair': "Fair form. Focus on consistency.",
    'poor': "Form needs improvement. Pay attention to these points:"
}


def generate_feedback(
    accuracy: float,
    top_error_joints: List[int],
    exercise: str = 'jumping_jack'
) -> List[str]:
    # \"\"\"
    # Generate feedback messages based on accuracy and error joints
    
    # Args:
    #     accuracy: Accuracy percentage (0-100)
    #     top_error_joints: List of joint indices with highest errors
    #     exercise: Exercise type
        
    # Returns:
    #     List of feedback messages
    # \"\"\"
    feedback_messages = []
    
    # Overall quality message
    if accuracy >= 90:
        feedback_messages.append(GENERIC_FEEDBACK['excellent'])
    elif accuracy >= 75:
        feedback_messages.append(GENERIC_FEEDBACK['good'])
    elif accuracy >= 60:
        feedback_messages.append(GENERIC_FEEDBACK['fair'])
    else:
        feedback_messages.append(GENERIC_FEEDBACK['poor'])
    
    # Specific joint feedback (only if accuracy < 90)
    if accuracy < 90:
        exercise_feedback = EXERCISE_FEEDBACK.get(exercise.lower(), {})
        
        for joint_idx in top_error_joints[:3]:  # Top 3 errors
            if joint_idx in exercise_feedback:
                feedback_messages.append(f"• {exercise_feedback[joint_idx]}")
            else:
                joint_name = JOINT_NAMES.get(joint_idx, f"joint {joint_idx}")
                feedback_messages.append(f"• Check your {joint_name} position")
    
    return feedback_messages