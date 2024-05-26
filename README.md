# Phishing detection package

## Motivation

## Code structure

### Configs

The model parameters are set via configs. The configs are represented by yaml files. The values
for parameters can be set in `phishing_detection_model/config.yml` file. The cofigs are parsed and validated
in `phishing_detection_model/config/core.py` module using [StrictYaml](https://github.com/crdoconnor/strictyaml) lib for parsing
and [Pydantic](https://pydantic-docs.helpmanual.io/) lib for type checking the values.

### Setting the pipeline and training

The pipeline is set in `phishing_detection_model/pipeline.py` file. Training is set in
`phishing_detection_model/train_pipeline.py` file. All the data processing steps are made in the same
[Scikit-learn](https://scikit-learn.org/stable/) style including custom transformations, stored in
`phishing_detection_model/processing/features.py` file.

### Making predictions

The code for prediction is set in `phishing_detection_model/predict.py` file. Before every prediction
the validation of input data is made. The code for validation can be found in
`phishing_detection_model/processing/validation.py` file.

## How to run the code

The code can be run via the [Tox](https://pypi.org/project/tox/) tool. Tox is a
convenient way to set up the environment and python paths automatically and run the
required commands from the command line. The file with description for tox can be found
in `tox.ini` file. The following commands can be run from the command line
using tox:

- Install tox: `python -m pip install --user tox`
- Run training: first create a directory for saving models if there is no any `mkdir ./phishing_detection_model/trained_models` and then run `python -m tox -e train`
- Run testing (via [pytest](https://docs.pytest.org/en/6.2.x/)): `python -m tox -e test_package`
- Run typechecking (via [mypy](https://mypy.readthedocs.io/en/stable/)): `python -m tox -e typechecks`
- Run style checks
  (via [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort),
  [mypy](https://mypy.readthedocs.io/en/stable/)
  and [flake8](https://pypi.org/project/flake8/)): `python -m tox -e stylechecks`

## How to install the package

In order to install the package run

```
pip install phishing-detection-model
```

After that you can make predictions, using the package:

```
from phishing_detection_model.predict import make_prediction

# Example input
input_dict = {'URL': ['https://google.com']}

result = make_prediction(input_data=input_dict)

print(result)
```

## Web application

Link to the app: https://github.com/mike56k/phishing-detection-webapp

## CI (Continuous Integration)

CI has been added to the project using Github Actions in order to automate package testing step and upload to PyPI step. The files that stand for CI are located in `./github/workflows/` directory. `CI.yml` file stands for automatic testing of the package every pull-request and push to the main branch, while `PyPI.yml` file is responsible for the automatic upload of the package to the PyPI every time the release is made for the corresponding version of the package.
