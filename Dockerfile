FROM registry.cn-shanghai.aliyuncs.com/aliseccompetition/tensorflow:1.1.0-devel-gpu
#MAINTAINER
MAINTAINER AlibabaSec

ADD . /competition
WORKDIR /competition

# INSTALL cleverhans foolbox
# pretrained_models
RUN mkdir ./models
