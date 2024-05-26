import numpy as np

from phishing_detection_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_shape = (109870, 2)

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    preds = result.get("preds")
    probs = result.get("probs")

    assert isinstance(preds, list)
    assert isinstance(probs, list)
    assert isinstance(preds[0], str)
    assert isinstance(probs[0], np.float64)
    assert result.get("errors") is None
    assert len(preds) == len(probs) == expected_shape[0]
