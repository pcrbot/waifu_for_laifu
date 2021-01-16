from typing import List


class ChatResult:
    CHAT_RESULT_FINISH = 'finish'
    CHAT_RESULT_EXIT = 'exit'
    CHAT_RESULT_PAUSE = 'pause'
    CHAT_RESULT_NEXT = 'next'

    def __init__(self, result_type: str, msg: str, msgs=None):
        self.result_type: str = result_type
        self.task_finish = 0
        if result_type == ChatResult.CHAT_RESULT_FINISH:
            self.task_finish = 10
        elif result_type == ChatResult.CHAT_RESULT_EXIT:
            self.task_finish = 20

        self.msg: str = msg
        self.msgs: List[str] = msgs or []
        if msg:
            self.msgs.append(msg)
