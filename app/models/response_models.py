from pydantic import BaseModel, Field
from typing import List

class RepResult(BaseModel):
    # \"\"\"Result for a single repetition\"\"\"
    rep: int = Field(..., description="Repetition number")
    accuracy: float = Field(..., ge=0, le=100, description="Accuracy percentage (0-100)")
    reconstruction_error: float = Field(..., description="Model reconstruction error")
    is_correct_form: bool = Field(..., description="Whether form is considered correct")
    feedback: List[str] = Field(..., description="Feedback messages")

class EvaluateResponse(BaseModel):
    # \"\"\"Response model for exercise evaluation\"\"\"
    exercise: str = Field(..., description="Exercise type")
    user_id: str = Field(..., description="User identifier")
    total_reps: int = Field(..., description="Number of reps evaluated")
    average_accuracy: float = Field(..., ge=0, le=100, description="Average accuracy across all reps")
    results: List[RepResult] = Field(..., description="Individual rep results")
    
    class Config:
        json_schema_extra = {
            "example": {
                "exercise": "jumping_jack",
                "user_id": "user_123",
                "total_reps": 5,
                "average_accuracy": 85.4,
                "results": [
                    {
                        "rep": 1,
                        "accuracy": 92.3,
                        "reconstruction_error": 0.008,
                        "is_correct_form": True,
                        "feedback": ["Excellent form! Keep it up! 💪"]
                    },
                    {
                        "rep": 2,
                        "accuracy": 78.5,
                        "reconstruction_error": 0.015,
                        "is_correct_form": False,
                        "feedback": [
                            "Good form! Minor improvements possible.",
                            "• Raise your left arm higher"
                        ]
                    }
                ]
            }
        }

class HealthResponse(BaseModel):
    # \"\"\"Health check response\"\"\"
    status: str = Field(..., description="API status")
    version: str = Field(..., description="API version")
    model_loaded: bool = Field(..., description="Whether ML model is loaded")