import numpy as np
from typing import List

def preprocess_rep(frames: List[List[float]], sequence_length: int = 50) -> np.ndarray:
    """
    Preprocess a single repetition
    
    Args:
        frames: List of frames, each with 132 features
        sequence_length: Target sequence length
        
    Returns:
        Normalized numpy array of shape (sequence_length, 132)
    """
    # Convert to numpy array
    sequence = np.array(frames, dtype=np.float32)
    
    # Get number of features from the data
    n_features = sequence.shape[1]
    
    # Pad or truncate to fixed length
    if len(sequence) > sequence_length:
        sequence = sequence[:sequence_length]
    else:
        padding = np.zeros((sequence_length - len(sequence), n_features), dtype=np.float32)
        sequence = np.vstack([sequence, padding])
    
    # Normalize
    sequence = normalize_pose(sequence)
    
    return sequence


def normalize_pose(seq: np.ndarray) -> np.ndarray:
    """
    Normalize pose landmarks:
    1. Center at hip midpoint
    2. Scale by shoulder width
    3. Clip and scale to [-1, 1]
    """
    seq = seq.copy().astype(np.float32)
    
    # Get number of features and calculate landmarks count
    n_features = seq.shape[1]
    n_landmarks = n_features // 4  # Each landmark has 4 values (x, y, z, visibility)
    
    # Only process if we have the expected number of features
    if n_features != 132:
        # If wrong size, just clip and scale without normalization
        return np.clip(seq, -3, 3) / 3.0
    
    # Calculate hip center (landmarks 23 and 24)
    hip_center_x = (seq[:, 23*4] + seq[:, 24*4]) / 2
    hip_center_y = (seq[:, 23*4+1] + seq[:, 24*4+1]) / 2
    
    # Center all x and y coordinates
    for joint_idx in range(n_landmarks):
        seq[:, joint_idx*4] -= hip_center_x
        seq[:, joint_idx*4+1] -= hip_center_y
    
    # Calculate shoulder width (landmarks 11 and 12)
    shoulder_width = np.sqrt(
        (seq[:, 11*4] - seq[:, 12*4])**2 + 
        (seq[:, 11*4+1] - seq[:, 12*4+1])**2
    )
    
    # Avoid division by zero
    shoulder_width = np.where(shoulder_width < 0.01, 1, shoulder_width)
    
    # Scale by shoulder width
    for joint_idx in range(n_landmarks):
        seq[:, joint_idx*4] = seq[:, joint_idx*4] / shoulder_width
        seq[:, joint_idx*4+1] = seq[:, joint_idx*4+1] / shoulder_width
        seq[:, joint_idx*4+2] = seq[:, joint_idx*4+2] / shoulder_width
    
    # Clip outliers and scale to [-1, 1]
    seq = np.clip(seq, -3, 3) / 3.0
    
    return seq