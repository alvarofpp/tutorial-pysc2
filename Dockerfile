FROM alvarofpp/sc2le

RUN apt-get update -yq && apt-get install -yq python3 python3-pip

# copy and install from requirements.txt
COPY . requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
# copy project to container
COPY . /app

ENV C_FORCE_ROOT=true

#ENTRYPOINT ["bash"]