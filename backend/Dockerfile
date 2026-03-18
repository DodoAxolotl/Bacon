FROM python:3.14-slim

WORKDIR /backend

COPY . .

EXPOSE 5000

RUN pip install .

RUN python generate_db/generate_db.py

CMD ["python", "bacon_distance/server.py"]
