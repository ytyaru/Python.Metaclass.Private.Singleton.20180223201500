class DbMeta(type):
    def __new__(cls, name, bases, attrs):
        print('__new__')
        attrs['_{0}__secret'.format(name)] = 'my_secret' # Db.__secret 定義
        return type.__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('__init__')
        setattr(cls, 'Secret', property(lambda cls: attrs['_{0}__secret'.format(name)])) # Db.Secretプロパティ定義

    _instance = None
    def __call__(cls, *args, **kwargs):
        print('__call__')
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
            print('***** singleton instance *****')
        return cls._instance

