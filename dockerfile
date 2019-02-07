FROM registry.centos.org/centos/centos:7

ENV APP_DIR='/schedule_check'
RUN touch /var/log/access.log

WORKDIR ${APP_DIR}
ADD .  ${APP_DIR}

RUN yum install -y epel-release &&\
    yum install -y gcc  python34-pip python34-devel &&\
    yum clean all

# Pre-install application dependencies to better utilize caching in Docker
COPY requirements.txt /
RUN pip3 install -r /requirements.txt && rm /requirements.txt

ENTRYPOINT ["python3", "schedule_check.py"]