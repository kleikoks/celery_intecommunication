from enum import Enum


class Queue(str, Enum):
    AI_SERVICE = "ai_service"
    BE_SERVICE = "be_service"


class AITask(str, Enum):
    PRODUCE_MESSAGE = "ai.produce_message"
    CONSUME_MESSAGE = "ai.consume_message"


class BETask(str, Enum):
    CONSUME_MESSAGE = "be.consume_message"
