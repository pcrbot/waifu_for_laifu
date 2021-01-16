from typing import Dict, List, Optional

from .chat_result import ChatResult


class ChatSession:

    SESSIONS = {}

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.state = {}
        self.nicknames = {}
        self.data: Optional[str] = None

    def finish(self, answer: str = None, answers=None):
        del ChatSession.SESSIONS[self.session_id]
        return ChatResult(ChatResult.CHAT_RESULT_FINISH, answer, answers)

    def exit(self, answer: str = None, answers=None):
        del ChatSession.SESSIONS[self.session_id]
        return ChatResult(ChatResult.CHAT_RESULT_EXIT, answer, answers)

    def pause(self, answer: str = None, answers=None):
        ChatSession.SESSIONS[self.session_id] = self
        return ChatResult(ChatResult.CHAT_RESULT_PAUSE, answer, answers)

    def next(self, ask: str):
        ChatSession.SESSIONS[self.session_id] = self
        return ChatResult(ChatResult.CHAT_RESULT_NEXT, ask)

    @staticmethod
    async def get_session(group_id, user_id):
        session_id = user_id
        if session_id not in ChatSession.SESSIONS:
            ChatSession.SESSIONS[session_id] = ChatSession(session_id)
        return ChatSession.SESSIONS[session_id]
