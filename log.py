from celery.utils.log import get_task_logger
 
def register_task_logger(module_name):
    """Instantiate a logger at the decorated class instance level."""
    def wrapper(cls):
        cls.log = get_task_logger('%s.%s' % (module_name, cls.__name__))
        return cls
    return wrapper