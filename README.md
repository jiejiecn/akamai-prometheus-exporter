# akamai-prometheus-exporter
Akamai CDN Metrics based on DataStream2

Backend storage based on Elasticsearch, support 7.x/8.x


Copy config.py.template to config.py
Modify the parameter 
run with  "Python exportor.py"



性能指标（Metrics） </br>
timestamp 时间戳：分钟级 </br>
Hits数（总请求数） </br>
HTTP 2XX计数 </br>
HTTP 3XX计数 </br>
HTTP 4XX计数 </br>
HTTP 5XX计数</br>
HTTP 其他计数</br>
HTTP 200/206计数</br>
HTTP 404计数</br>
HTTP 403计数</br>
Hit数（命中数）</br>
Miss数（未命中数）</br>
Cache命中率    （百分比 %）</br>
responseTime响应时间（ms），含 分位值   </br>
tlsOverheadTimeMSec （ms），含 分位值 </br>
reqEndTimeMSec （ms），含 分位值 </br>
turnAroundTimeMSec （ms），含 分位值 </br>
transferTimeMSec （ms），含 分位值 </br>
timeToFirstByte（ms)，含 分位值    </br>


指标计算公式：</br>
responseTime = tlsOverheadTimeMSec+reqEndTimeMSec+turnAroundTimeMSec+transferTimeMSec </br>
timeToFirstByte = reqEndTimeMSec + turnAroundTimeMSec </br>