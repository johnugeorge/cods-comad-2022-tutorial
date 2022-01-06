From tensorflow/tensorflow


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         nginx \
         python \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install flask gevent gunicorn six

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/predict:${PATH}"

COPY anomaly /opt/predict
WORKDIR /opt/predict
