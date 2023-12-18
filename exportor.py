from prometheus_client import start_http_server
from prometheus_client import Gauge, Summary
from prometheus_client import REGISTRY


import time, random, os, platform
import prometheus_client
import datasource, config

REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)


if __name__ == '__main__':
    
    hostPort = config.hostPort
    hostAddr = config.hostAddr
    start_http_server(port=hostPort, addr=hostAddr)

    percentiles = config.metrics_percentiles

    httpRequestCount = Gauge("akamai_cdn_request_status", "Hits on EdgeServer", ["hostName", "region", "cacheStatus"])
    httpCodeStatus = Gauge("akamai_cdn_http_status_code", "StatusCode on EdgeServer", ["hostName", "region", "httpCode"])
    serverTimePercentile = Gauge("akamai_cdn_server_time_percentile", "", ["hostName", "region", "metric", "stats"])
    serverTimeStats = Gauge("akamai_cdn_server_time_stats", "", ["hostName", "region", "metric", "stats"])

    while(True):
        
        httpRequestCount.clear()
        httpCodeStatus.clear()
        serverTimePercentile.clear()
        serverTimeStats.clear()
        
        try:
            query = datasource.getMetrics()
            
            for item in query['aggregations']['hostName']['buckets']:
                hostName = item['key']
                totalHits = item['doc_count']

                for region in item['region']['buckets']:
                    country = region['key']
                    regionHits = region['doc_count']

                    for hitStatus in region['cacheStatus']['buckets']:
                        key = int(hitStatus['key'])
                        if key == 1:
                            hitCount = hitStatus['doc_count']
                        
                        if key == 0:
                            missCount = hitStatus['doc_count']

                    #hitRatio = round(hitCount / regionHits, 4)

                    httpRequestCount.labels(hostName, country, "requests").set(regionHits)
                    httpRequestCount.labels(hostName, country, "hit").set(hitCount)
                    httpRequestCount.labels(hostName, country, "miss").set(missCount)
                    #print(hostName, country, regionHits, hitCount, missCount)
                    
                    for httpCode in region['requestCount']['buckets']:
                        code = httpCode['key']
                        count = httpCode['doc_count']

                        httpCodeStatus.labels(hostName, country, code).set(count)
                        #print(httpCode['key'], httpCode['doc_count'])


                    for suffix in ['avg', 'min', 'max', 'std_deviation', 'variance']:
                        responseTime = region['stats_responseTime'][suffix]
                        serverTimeStats.labels(hostName, country, "responseTime", suffix).set(responseTime)

                        rspContentLen = region['stats_rspContentLen'][suffix]
                        serverTimeStats.labels(hostName, country, "contentLength", suffix).set(rspContentLen)

                        tlsOverheadTime = region['stats_tlsOverheadTime'][suffix]
                        serverTimeStats.labels(hostName, country, "tlsOverheadTime", suffix).set(tlsOverheadTime)

                        transferTime = region['stats_transferTime'][suffix]
                        serverTimeStats.labels(hostName, country, "transferTime", suffix).set(transferTime)

                        reqEndTime = region['stats_reqEndTime'][suffix]
                        serverTimeStats.labels(hostName, country, "reqEndTime", suffix).set(reqEndTime)

                        turnAroundTime = region['stats_turnAroundTime'][suffix]
                        serverTimeStats.labels(hostName, country, "turnAroundTime", suffix).set(turnAroundTime)

                    
                    for percent in ['5.0', '10.0', '50.0', '90.0', '95.0', '99.0']:
                        percentile = 'p' + percent.replace('.0', '')

                        responseTime = region['responseTime']['values'][percent]
                        serverTimePercentile.labels(hostName, country, "responseTime", percentile).set(responseTime)

                        rspContentLen = region['rspContentLen']['values'][percent]
                        serverTimePercentile.labels(hostName, country, "contentLength", percentile).set(responseTime)

                        transferTime = region['transferTime']['values'][percent]
                        serverTimePercentile.labels(hostName, country, "transferTime", percentile).set(transferTime)

                        turnAroundTime = region['turnAroundTime']['values'][percent]
                        serverTimePercentile.labels(hostName, country, "turnAroundTime", percentile).set(responseTime)

                        tlsOverheadTime = region['tlsOverheadTime']['values'][percent]
                        serverTimePercentile.labels(hostName, country, "tlsOverheadTime", percentile).set(responseTime)

                        reqEndTime = region['reqEndTime']['values'][percent]
                        serverTimePercentile.labels(hostName, country, "reqEndTime", percentile).set(responseTime)

            time.sleep(10)

        except:
            time.sleep(5)


            

