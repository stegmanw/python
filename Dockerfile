FROM python

WORKDIR /app

COPY . /app

CMD [ "python", "bmi-calc.py"]

