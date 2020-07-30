FROM python:3.7.3-stretch


# 以下改编自mentor的dockerfile
# Working Directory
WORKDIR /app

# Copy source code to working directory
RUN mkdir /app/apps/
RUN mkdir /app/apps/know
COPY apps/app2.py /app/apps/
COPY requirement.txt /app/
COPY apps/know  /app/apps/know

RUN mkdir /app/templates/
RUN mkdir /app/templates/templates
RUN mkdir /app/templates/static
RUN mkdir /app/templates/static/css
RUN mkdir /app/templates/static/img
RUN mkdir /app/templates/static/pictures_of_people_unknow

COPY templates/templates  /app/templates/templates
COPY templates/static/css /app/templates/static/css
COPY templates/static/img  /app/templates/static/img
COPY templates/static/pictures_of_people_unknow  /app/templates/static/pictures_of_people_unknow
COPY templates/templates/  /app/templates/templates



# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirement.txt

# Expose port 8080
EXPOSE 8080

# Run app.py at container launch
CMD ["python", "apps/app2.py"]