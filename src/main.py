from session_manager import SessionManager
from message_dispatcher import MessageDispatcher

def main():
    session = SessionManager()
    session.start()

    dispatcher = MessageDispatcher(session.driver)
    dispatcher.run_campaign()

if __name__ == "__main__":
    main()