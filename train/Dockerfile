From tensorflow/tensorflow


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         nginx \
         python \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*


ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

WORKDIR /opt/
COPY . /opt/
RUN pip install pandas boto3 sagemaker
CMD [ "python", "/opt/anomalytrain.py" ]
