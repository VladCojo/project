#Dockerfile, Image, Container
#docker run -t -i  python-queens (pt a accepta input)
FROM python:latest
WORKDIR /app
COPY . /app

CMD [ "python","-u", "-i", "./Solve_N_Queens.py" ]