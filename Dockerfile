FROM python:3.9.0
RUN pip3 install openpyxl requests click progress

WORKDIR /home/FAB-DIS/
ENTRYPOINT ["python3","fabdis_url_checker.py"]