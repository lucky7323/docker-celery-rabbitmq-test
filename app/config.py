class CelerySettings:
    task_serializer: str = "json"
    result_serializer: str = "json"
    timezone: str = "Asia/Seoul"
    enable_utc: bool = True
    broker_url: str = "amqp://guest:guest@rabbitmq:5672//"
    result_backend: str = "redis://redis:6379/0"
    result_expires: int = 300

