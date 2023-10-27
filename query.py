import config


percentiles = [5, 10, 50, 90, 95, 99]   #性能指标百分位

metrics_index = config.datastream_idx

metrics_query = {
  "size": 0,
  "query": {
    "bool": {
    "filter": [
        {"range": {
          "reqTimeSec": {
            "gte": "now-120s",
            "lte": "now-60s"
          }
        }
        }
      ]
    }
  },
  
  "aggs": {
    "hostName": {
      "terms": {
        "field": "hostName"
      },
      "aggs": {
          "region":{
              "terms":{
                  "field": "country"
              },
              "aggs": {
                "requestCount": {
                  "terms": {
                    "field": "statusCode"
                  }
                },
                "cacheStatus": {
                  "terms": {
                    "field": "cacheStatus"
                  }
                },
                "stats_responseTime": {
                  "extended_stats": {
                    "field": "responseTimeMSec"
                  }
                },
                "stats_rspContentLen": {
                  "extended_stats": {
                    "field": "rspContentLen"
                  }
                },
                "stats_turnAroundTime": {
                  "extended_stats": {
                    "field": "turnAroundTimeMSec"
                  }
                },
                "stats_tlsOverheadTime": {
                  "extended_stats": {
                    "field": "tlsOverheadTimeMSec"
                  }
                },
                "stats_reqEndTime": {
                  "extended_stats": {
                    "field": "reqEndTimeMSec"
                  }
                },
                "stats_transferTime": {
                  "extended_stats": {
                    "field": "transferTimeMSec"
                  }
                },
                "responseTime": {
                  "percentiles": {
                        "field": "responseTimeMSec",
                        "percents": percentiles
                      }
                },
                "reqEndTime": {
                      "percentiles": {
                        "field": "reqEndTimeMSec",
                        "percents": percentiles
                      }
                    },
                "tlsOverheadTime": {
                  "percentiles": {
                    "field": "tlsOverheadTimeMSec",
                    "percents": percentiles
                  }
                },
                
                "turnAroundTime": {
                  "percentiles": {
                    "field": "turnAroundTimeMSec",
                    "percents": percentiles
                  }
                },
                "transferTime": {
                  "percentiles": {
                    "field": "transferTimeMSec",
                    "percents": percentiles
                  }
                },
                "rspContentLen": {
                  "percentiles": {
                    "field": "rspContentLen",
                    "percents": percentiles
                  }
                },
              }
          }
      }



    }
  }
}