def init_protocol(cls):
    """
    FOR GUI BASE CLASSES
    decorator for classes that implement:
    1. cls.__init__()
    2. cls.post_setup()
    3. cls.make()
    4. cls.show()
    after creation an instance
    """

    class WrappedClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.post_setup()
            self.make()
            self.show()

        def post_setup(self):
            if hasattr(cls, 'post_setup'):
                return super().post_setup()
            else:
                raise AttributeError(f"{cls.__name__} has no make method")

        def make(self):
            if hasattr(cls, 'make'):
                return super().make()
            else:
                raise AttributeError(f"{cls.__name__} has no make method")

        def show(self):
            if hasattr(cls, 'show'):
                return super().show()
            else:
                raise AttributeError(f"{cls.__name__} has no show method")

    return WrappedClass
