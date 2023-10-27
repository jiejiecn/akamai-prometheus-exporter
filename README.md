# akamai-prometheus-exporter
Akamai CDN Metrics based on DataStream2

Backend storage based on Elasticsearch, support 7.x/8.x


Copy config.py.template to config.py
Modify the parameter 
run with  "Python exportor.py"



性能指标（Metrics）
timestamp 时间戳：分钟级
Hits数（总请求数）
HTTP 2XX计数
HTTP 3XX计数
HTTP 4XX计数
HTTP 5XX计数
HTTP 其他计数
HTTP 200/206计数
HTTP 404计数
HTTP 403计数
Hit数（命中数）
Miss数（未命中数）
Cache命中率    （百分比 %）
responseTime响应时间（ms），含 分位值    => pipeline计算
tlsOverheadTimeMSec （ms），含 分位值
reqEndTimeMSec （ms），含 分位值
turnAroundTimeMSec （ms），含 分位值
transferTimeMSec （ms），含 分位值
timeToFirstByte（ms)，含 分位值    


指标计算公式：
responseTime = tlsOverheadTimeMSec+reqEndTimeMSec+turnAroundTimeMSec+transferTimeMSec
timeToFirstByte = reqEndTimeMSec + turnAroundTimeMSec