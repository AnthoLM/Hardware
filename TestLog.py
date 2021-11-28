import logging

logger = logging.getLogger("TestLog")
logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.WARNING)

fh = logging.FileHandler('TestLog')
fh.setLevel(logging.INFO)
fh.setLevel(logging.DEBUG)
fh.setLevel(logging.WARNING)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setLevel(logging.DEBUG)
ch.setLevel(logging.WARNING)

formatter = logging.Formatter('%(levelname)-8s %(asctime)s %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('Mon message info')
logger.debug('Mon message debug')
logger.warning('Mon message warning')
