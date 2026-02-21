from pydantic import BaseModel, Field
from typing import List

class RepData(BaseModel):
    # \"\"\"Single repetition pose data\"\"\"
    frames: List[List[float]] = Field(
        ..., 
        description="List of frames, each frame has 132 features (33 landmarks × 4 values)",
        min_items=10,
        max_items=200
    )

class EvaluateRequest(BaseModel):
    # \"\"\"Request model for exercise evaluation\"\"\"
    exercise: str = Field(..., description="Exercise type (e.g., 'jumping_jack')")
    user_id: str = Field(..., description="User identifier")
    reps: List[RepData] = Field(
        ..., 
        description="List of repetitions to evaluate",
        min_items=1,
        max_items=10
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "exercise": "jumping_jack",
                "user_id": "user_123",
                "reps": [
                    {
                        "frames": [
                            [0.5, 0.3, 0.1, 0.99] * 33,  # Frame 1: 132 values
                            [0.5, 0.3, 0.1, 0.99] * 33,  # Frame 2: 132 values
                            # ... more frames
                        ]
                    }
                ]
            }
        }