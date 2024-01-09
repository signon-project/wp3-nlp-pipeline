FROM python:3.8
COPY requirements.txt .
COPY SignON_NLP.py .
COPY TextNormalizer/ /TextNormalizer/
COPY LinguisticTagger/ /LinguisticTagger/
COPY WSD/ /WSD/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD [ "python", "./SignON_NLP.py" ]
