from elasticsearch import Elasticsearch

import config, query, logger


server = config.elastic_host
user = config.elastic_user
password = config.elastic_pass

es = Elasticsearch(hosts=server, http_auth=(user, password))

def getMetrics():

    body = query.metrics_query
    idxname = query.metrics_index

    resp = es.search(index=idxname, body=body)


    return resp



