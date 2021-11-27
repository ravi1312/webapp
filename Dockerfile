FROM ubuntu:latest
ENV TZ=US/Eastern
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y  update
RUN apt-get install -y awscli
RUN apt-get -y  update
RUN apt-get install -y jq
