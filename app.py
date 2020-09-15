import random
import time

from flask import (Flask,
                   Response)
from prometheus_client import (generate_latest,
                               CONTENT_TYPE_LATEST,
                               Counter,
                               Gauge,
                               Summary)

#import enviroplus

app = Flask(__name__)

PROM_METRICS = {
    "counter": {
        "my_counter": Counter('my_counter',
                                 'Number Of counts',
                                 ['count']),
    }
}

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@app.route('/metrics')
@REQUEST_TIME.time()
def metrics():
    """Flask endpoint to gather the metrics, will be called by Prometheus."""
 # business counter
    PROM_METRICS['counter']['my_counter'].labels('count').inc()
    return Response(generate_latest(),
                    mimetype=CONTENT_TYPE_LATEST)

app.run(port=8000)