language: python

python:
    - "3.6"

install:
    - pip install - r requirements.txt
    - pip install coveralls

script:
    - nosetests - -with-coverage - -cover-package = app

after_success:
    - coveralls
