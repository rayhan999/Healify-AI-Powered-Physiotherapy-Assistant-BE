from fastapi import APIRouter, HTTPException, status
from app.models.request_models import EvaluateRequest
from app.models.response_models import EvaluateResponse, RepResult
from app.services.evaluation import evaluate_single_rep
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post(
    "/evaluate",
    response_model=EvaluateResponse,
    status_code=status.HTTP_200_OK,
    summary="Evaluate Exercise Form",
    description="Evaluates exercise form and returns accuracy with feedback"
)
async def evaluate_exercise(request: EvaluateRequest):
    # \"\"\"
    # Evaluate exercise repetitions and provide feedback
    
    # - **exercise**: Type of exercise (e.g., 'jumping_jack')
    # - **user_id**: User identifier
    # - **reps**: List of repetitions with pose data
    # \"\"\"
    try:
        logger.info(f"Evaluating {len(request.reps)} reps for user {request.user_id}")
        
        results = []
        
        # Evaluate each rep
        for i, rep in enumerate(request.reps):
            result = evaluate_single_rep(rep.frames, request.exercise)
            
            results.append(RepResult(
                rep=i + 1,
                accuracy=result['accuracy'],
                reconstruction_error=result['reconstruction_error'],
                is_correct_form=result['is_correct_form'],
                feedback=result['feedback']
            ))
        
        # Calculate average accuracy
        avg_accuracy = sum(r.accuracy for r in results) / len(results)
        
        response = EvaluateResponse(
            exercise=request.exercise,
            user_id=request.user_id,
            total_reps=len(results),
            average_accuracy=round(avg_accuracy, 1),
            results=results
        )
        
        logger.info(f"Evaluation complete. Average accuracy: {avg_accuracy:.1f}%")
        
        return response
        
    except Exception as e:
        logger.error(f"Error evaluating exercise: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error evaluating exercise: {str(e)}"
        )