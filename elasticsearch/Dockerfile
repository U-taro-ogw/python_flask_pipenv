FROM docker.elastic.co/elasticsearch/elasticsearch-oss:6.4.3

RUN /usr/share/elasticsearch/bin/elasticsearch-plugin list | grep -q analysis-kuromoji || /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-kuromoji
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin list | grep -q analysis-icu || /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
