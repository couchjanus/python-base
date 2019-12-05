import logging
import logging.config
from todo05.app import App

# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger("todoApp")
    
# logger.info("Program started")
# logger.info("Done!")

# dictLogConfig = {
#     "version":1,
#     "handlers":{
#         "fileHandler":{
#             "class":"logging.FileHandler",
#             "formatter":"todoFormatter",
#             "filename":"config2.log"
#         }
#         },
#         "loggers":{
#             "todoApp":{
#                 "handlers":["fileHandler"],
#                 "level":"INFO",
#             }
#         },
#         "formatters":{
#             "todoFormatter":{
#                 "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#             }
#         }
# }
    
# logging.config.dictConfig(dictLogConfig)
# logger = logging.getLogger("todoApp")
# logger.info("Program started")
# logger.info("Done!")

# Main
if __name__ == "__main__":
    """
    The main entry point of the application
    """
    logging_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=logging_format)
    # add filemode="w" to overwrite
    # logging.basicConfig(filename="todo.log", level=logging.INFO)
    # logging.basicConfig(filename="todo.log", level=logging.DEBUG, format=logging_format)
    # logging.debug("This is a debug message")
    # logging.info("Informational message")
    # logging.error("An error has happened!")

    # logging.basicConfig(filename="logging.log", level=logging.INFO)
    # log = logging.getLogger("ex")

    # logger = logging.getLogger("guiApp")
    # logger.setLevel(logging.INFO)
    
    # create the logging file handler
    # fh = logging.FileHandler("gui_app.log")

    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # fh.setFormatter(formatter)
    
    # add handler to logger object
    # logger.addHandler(fh)

    try:
        # logging.info("Program started")
        # logging.debug("Creating GUI")
        filename = "todos.db"
        # raise RuntimeError
        root = App(filename)
        root.mainloop()
        # logging.info("Done!")

    # except RuntimeError:
    #     log.exception("Error!")
    except KeyboardInterrupt:
        # logging.critical("Program Force quit")
        quit(0)
