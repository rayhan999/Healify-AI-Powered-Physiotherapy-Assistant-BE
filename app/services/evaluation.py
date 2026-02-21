import numpy as np
from typing import List
from app.core.model_loader import model_loader
from app.core.preprocessing import preprocess_rep
from app.services.feedback import generate_feedback

def evaluate_single_rep(
    frames: List[List[float]],
    exercise: str
) -> dict:
    # \"\"\"
    # Evaluate a single repetition
    
    # Args:
    #     frames: List of pose landmark frames
    #     exercise: Exercise type
        
    # Returns:
    #     Dict with accuracy, error, and feedback
    # \"\"\"
    # Get model and config
    model = model_loader.model
    threshold = model_loader.threshold
    config = model_loader.config
    
    # Preprocess
    sequence = preprocess_rep(frames, config['sequence_length'])
    
    # Reshape for model
    seq_input = sequence.reshape(1, sequence.shape[0], sequence.shape[1])
    
    # Get reconstruction
    reconstructed = model.predict(seq_input, verbose=0)[0]
    
    # Calculate MSE
    mse = np.mean(np.square(sequence - reconstructed))
    
    # Calculate accuracy
    if mse <= threshold:
        accuracy = 70 + 30 * (1 - (mse / threshold))
    else:
        accuracy = max(0, 70 * (1 - ((mse - threshold) / threshold)))
    
    accuracy = min(100, max(0, accuracy))
    
    # Calculate per-joint errors
    joint_errors = []
    for joint_idx in range(33):
        joint_original = sequence[:, joint_idx*4:joint_idx*4+3]
        joint_recon = reconstructed[:, joint_idx*4:joint_idx*4+3]
        joint_error = np.mean(np.square(joint_original - joint_recon))
        joint_errors.append(joint_error)
    
    # Get top error joints
    top_error_indices = np.argsort(joint_errors)[-3:][::-1].tolist()
    
    # Generate feedback
    feedback = generate_feedback(accuracy, top_error_indices, exercise)
    
    return {
        'accuracy': round(accuracy, 1),
        'reconstruction_error': float(mse),
        'is_correct_form': mse <= threshold,
        'feedback': feedback
    }