FROM python:3.7

RUN sudo apt-get update \
    && pip install --upgrade pip \
    && pip install theano -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && git clone -b Authority https://github.com/baiyanquan/2019-XLab-TransEImplementation.git ~/TransE \
    && chmod 777 ~/TransE/run.sh

CMD ["sh", "/root/TransE/run.sh"]