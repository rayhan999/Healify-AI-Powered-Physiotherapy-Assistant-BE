import numpy as np
import tensorflow as tf
from tensorflow import keras
import json
import logging
from app.config import settings

logger = logging.getLogger(__name__)

class ModelLoader:
    # \"\"\"Singleton class for loading and managing ML model\"\"\"
    
    _instance = None
    _model = None
    _threshold = None
    _config = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
        return cls._instance
    
    def load_model(self):
        # \"\"\"Load the trained LSTM model, threshold, and config\"\"\"
        try:
            logger.info("Loading ML model...")
            
            # Load model
            self._model = keras.models.load_model(settings.MODEL_PATH)
            logger.info(f"✓ Model loaded from {settings.MODEL_PATH}")
            
            # Load threshold
            self._threshold = float(np.load(settings.THRESHOLD_PATH))
            logger.info(f"✓ Threshold loaded: {self._threshold:.6f}")
            
            # Load config
            with open(settings.CONFIG_PATH, 'r') as f:
                self._config = json.load(f)
            logger.info(f"✓ Config loaded")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise
    
    @property
    def model(self):
        if self._model is None:
            self.load_model()
        return self._model
    
    @property
    def threshold(self):
        if self._threshold is None:
            self.load_model()
        return self._threshold
    
    @property
    def config(self):
        if self._config is None:
            self.load_model()
        return self._config
    
    def is_loaded(self):
        return self._model is not None

# Global model loader instance
model_loader = ModelLoader()