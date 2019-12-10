import logging
import logging.config
from emp01.app import App

# Main
if __name__ == "__main__":
    """
    The main entry point of the application
    """
    try:
        root = App()
        root.mainloop()

    except KeyboardInterrupt:
        quit(0)
