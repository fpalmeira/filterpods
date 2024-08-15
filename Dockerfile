FROM python:3.9 
ADD filterpods.py .
RUN pip install kubernetes
CMD ["python3", "./filterpods.py" ]
