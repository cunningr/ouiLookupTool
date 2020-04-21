FROM python:3.7.7-alpine3.10
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
RUN rm /requirements.txt
COPY ./mac_oui_lookup.py /
CMD ["sh", "-c", "python3 mac_oui_lookup.py"]
