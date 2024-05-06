import logging
import logging


def test_abc():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s');
    logging.info('Your message here')
    assert True
