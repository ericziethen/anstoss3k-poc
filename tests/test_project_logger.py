import os

from anstoss3k import project_logger


def test_logging():
    log_dir = R'anstoss3k\logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    project_logger.setup_logger(R'anstoss3k\logs\test_log.txt')
    project_logger.test_logging()
