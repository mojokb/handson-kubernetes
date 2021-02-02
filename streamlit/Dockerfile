FROM python:3.7

EXPOSE 8501

WORKDIR /app

RUN pip install streamlit

COPY . .

CMD ["streamlit", "run",  "app.py"]

