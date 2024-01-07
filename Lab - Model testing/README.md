# Comparison of FastAPI Model Serving and Dockerized API



We will utilize the Locust library for load testing.

```commandline
locust -r locustfile.py
```

Adjust the number of users and model URLs as needed.

![](https://media.discordapp.net/attachments/1179056718064386200/1193505110391791737/Screenshot_from_2024-01-07_11-43-02.png?ex=65acf540&is=659a8040&hm=4be7a650cf9eb68e5166ecbca31a08cba4aa25ec6e2a3da5e3fef0c3aa663927&=&format=webp&quality=lossless)

Start the swarm and allow the data to save. Once completed, the data can be viewed as follows:
## Fast api model serving results
![](https://media.discordapp.net/attachments/1179056718064386200/1193503730667114557/Screenshot_from_2024-01-07_11-32-57.png?ex=65acf3f7&is=659a7ef7&hm=9ff796a277ee8d70302233902c7df9826bb61adcd4101175f9b8666662545072&=&format=webp&quality=lossless&width=1138&height=640)


![](https://media.discordapp.net/attachments/1179056718064386200/1193503730205736990/Screenshot_from_2024-01-07_11-33-02.png?ex=65acf3f7&is=659a7ef7&hm=0463482ce2f0955e16c83cef59bce3c7973fd7099fafec65d888e57c5980a44d&=&format=webp&quality=lossless&width=1138&height=640)

## Docker results

![](https://media.discordapp.net/attachments/1179056718064386200/1193503775206420520/Screenshot_from_2024-01-07_11-37-30.png?ex=65acf402&is=659a7f02&hm=277dd593b85f751ac1919cc71477d7c87426908808ed995b74fc5c0903b9a9bf&=&format=webp&quality=lossless&width=1138&height=640)

# Comparing resutls

![](https://media.discordapp.net/attachments/1179056718064386200/1193503775659409478/Screenshot_from_2024-01-07_11-37-19.png?ex=65acf402&is=659a7f02&hm=517f97466966693af7480f83b23e245e363cd2eb77ab6ef14bd2c805799df5af&=&format=webp&quality=lossless&width=1138&height=640)

Endpoint: The endpoint being tested is /question_answering using the POST method.
Number of Requests: A total of 4843 requests were made to the endpoint.
Failure Rate: There were no failures observed, with a failure rate of 0.00%.
Response Times: The average response time (Avg) is 2253 milliseconds (approximately 2.25 seconds). The minimum (Min) and maximum (Max) response times are 24 milliseconds and 7738 milliseconds (approximately 7.74 seconds), respectively. The median (Med) response time is 2300 milliseconds.
Request Rate: The throughput is 30.17 requests per second, with no failed requests.
Response Time Percentiles:
* 50% (Median): 2300 milliseconds
* 66%: 3000 milliseconds
* 75%: 3200 milliseconds
* 80%: 3300 milliseconds
* 90%: 3400 milliseconds
* 95%: 3800 milliseconds
* 98%: 4300 milliseconds
* 99%: 4600 milliseconds
* 99.9%: 6400 milliseconds
* 99.99%: 7700 milliseconds
* 100%: 7700 milliseconds
### Interpretation:
1. Consistency: Most of the requests (99.99%) were served within 7700 milliseconds (approximately 7.7 seconds), indicating that the service is consistent for almost all requests.
2. Performance: The median response time is 2300 milliseconds (approximately 2.3 seconds), suggesting that half of the requests were processed within this time. However, the 99.9th percentile indicates that a small fraction of requests (0.1%) took up to 6400 milliseconds (approximately 6.4 seconds), which might be a concern depending on the application's requirements.
3. Throughput: The service handled a throughput of 30.17 requests per second without any failures, indicating that it can handle a moderate load effectively.
4. In conclusion, the FastAPI service appears to be performing well with consistent response times and a decent throughput rate. However, monitoring and optimization might be needed if faster response times are required for all percentiles or if higher throughputs are expected.
