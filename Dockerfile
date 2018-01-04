FROM jrottenberg/ffmpeg:2.8-centos

RUN yum groupinstall -y "Development tools"
RUN yum install -y mysql-devel numpy portaudio-devel python-devel gcc python-setuptools python-pip scipy python-matplotlib net-tools
RUN pip install PyAudio
RUN pip install pydub
RUN pip install Flask
RUN pip install Redis
RUN pip install MySQL-python
RUN pip install virtualenv
RUN virtualenv --system-site-packages env_with_system

RUN source env_with_system/bin/activate
#RUN pip install PyDejavu
RUN mkdir /app
RUN mkdir /uploads
ADD . /app/

EXPOSE 5000
#--host tag exposes the server to other networks
ENTRYPOINT cd /app && export FLASK_DEBUG=1 docke&& FLASK_APP=recognizeFile.py flask run --host=0.0.0.0

