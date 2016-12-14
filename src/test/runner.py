import sys
import nose


if __name__ == '__main__':
    module_name = sys.modules[__name__].__file__

    config_name = 'nose.cfg'

    result = nose.run(
        argv=[sys.argv[0],
              '-v']
        )