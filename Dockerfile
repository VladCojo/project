#Dockerfile, Image, Container
FROM python:3.12

ADD Solve_N_Queens.py .

CMD [ "python", "./Solve_N_Queens.py" ]