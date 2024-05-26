from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from phishing_detection_model.config.core import config

def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    relevant_data = input_data[config.model_config.features].copy()
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultiplePhishingDetectionInputs(inputs=relevant_data.replace({np.nan: None}).to_dict(orient="records"))
    except ValidationError as error:
        errors = error.json()

    return relevant_data, errors


class PhishingDetectionInputSchema(BaseModel):
    URL: Optional[str]


class MultiplePhishingDetectionInputs(BaseModel):
    inputs: List[PhishingDetectionInputSchema]
