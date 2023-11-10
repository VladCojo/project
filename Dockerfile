
FROM python:latest


WORKDIR /usr/src/myapp


COPY Solve_N_Queens.py .



CMD ["python", "Solve_N_Queens.py"]