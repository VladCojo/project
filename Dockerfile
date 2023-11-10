#Dockerfile, Image, Container
#docker run -t -i  python-queens (pt a accepta input)
FROM python:latest
WORKDIR /app
ADD Solve_N_Queens.py .

CMD [ "python","-u", "-i", "./Solve_N_Queens.py" ]