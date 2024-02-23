FROM python:3.11

RUN apt-get update && apt-get install -y \
    allure \
    curl \
    default-jre \
    default-jdk

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && pip install tox \
    && pip install playwright \
    && playwright install \
    && playwright install-deps \
    && curl -o allure-commandline-2.17.3.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.17.3/allure-commandline-2.17.3.tgz \
    && tar -zxvf allure-commandline-2.17.3.tgz -C /opt/ \
    && ln -s /opt/allure-2.17.3/bin/allure /usr/bin/allure \
    && rm -rf allure-commandline-2.17.3.tgz \
    && allure --version

EXPOSE 36355    

COPY . .

ENTRYPOINT ["tox"]
