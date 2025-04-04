class OrderStatus:
    """Enum for order statuses."""
    NEW = "new"
    PROCESSING_ERROR = "processing_error"
    UNKNOWN_TYPE = "unknown_type"
    EXPORTED = "exported"
    EXPORT_FAILED = "export_failed"
    PROCESSED = "processed"
    PENDING = "pending"
    ERROR = "error"
    API_ERROR = "api_error"
    API_FAILURE = "api_failure"
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    DB_ERROR = "db_error"


class OrderType:
    """Enum for order types."""

    A = "A"
    B = "B"
    C = "C"


class OrderPriority:
    """Enum for order priorities."""

    LOW = "low"
    HIGH = "high"


class OrderAmountThreshold:
    """Enum for order amount thresholds."""

    PRIORITY_THRESHOLD = 200
    HIGH_VALUE_ORDER_THRESHOLD = 150
    PROCESSED_ORDER_THRESHOLD = 100


class APIStatus:
    """Enum for API statuses."""

    SUCCESS = "success"
    FAILURE = "failure"
    ERROR = "error"


ORDER_API_RESPONSE_THRESHOLD = 50
