import time
import logging


class TimeLogger:
    def __init__(self, log_file="task_log.log"):
        """
        Initializes a new instance of the TimeLogger class.

        Args:
            log_file (str, optional): The path to the log file. Defaults to 'task_log.log'.

        Returns:
            None

        Configures logging with the specified log file and log level. The log format is set to
        '%(asctime)s - %(levelname)s - %(message)s'.

        The start_time and end_time attributes are initialized to None.
        """
        self.start_time = None
        self.end_time = None

        # Configure logging
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

    def start(self):
        """
        Starts the task by recording the current time and logging a start message.

        Args:
            None

        Returns:
            None
        """
        self.start_time = time.time()
        logging.info(
            f"Task started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.start_time))}"
        )

    def stop(self):
        """
        Stops the task by recording the current time, logging the end time, and calculating the duration.

        This method updates the `end_time` attribute of the object with the current time. It then logs the end time in the format "YYYY-MM-DD HH:MM:SS". Finally, it calls the `log_duration()` method to calculate and log the duration of the task.

        Parameters:
            None

        Returns:
            None
        """
        self.end_time = time.time()
        logging.info(
            f"Task ended at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.end_time))}"
        )
        self.log_duration()

    def log_duration(self):
        """
        Calculates and logs the duration of a task.

        This method checks if both the start time and end time of the task are not None. If they are not None, it calculates the duration by subtracting the start time from the end time. The duration is then logged using the logging module with the INFO level.

        If either the start time or end time is None, a warning message is logged using the logging module with the WARNING level. The warning message suggests that both the start and stop methods should be called to ensure accurate time logging.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        if self.start_time is not None and self.end_time is not None:
            duration = self.end_time - self.start_time
            logging.info(f"Task duration: {duration:.2f} seconds")
        else:
            logging.warning(
                "Task time logging is incomplete. Please ensure both start and stop methods are called."
            )
