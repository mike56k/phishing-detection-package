from nltk.tokenize import RegexpTokenizer # regexp tokenizers use to split words from text  
from sklearn.feature_extraction.text import CountVectorizer # create sparse matrix of words using regexptokenizes  

from sklearn.linear_model import LogisticRegression

# pipeline
from sklearn.pipeline import Pipeline

from phishing_detection_model.config.core import config

# set up the pipeline
phishing_detection_pipe = Pipeline(
    [
        (
            "count_vectorizer",
            CountVectorizer(tokenizer = RegexpTokenizer(r'[A-Za-z]+').tokenize,stop_words='english'),
        ),
        (
            "logit",
            LogisticRegression(
                C=config.model_config.alpha, solver="liblinear", random_state=config.model_config.random_state
            )
        ),
    ]
)
