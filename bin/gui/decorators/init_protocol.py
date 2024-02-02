def init_protocol(cls):
    class WrappedClass(cls):
        def __init__(self, *args, **kwargs):
            if hasattr(cls, '__init__'):
                super().__init__(*args, **kwargs)
                self.post_setup()
                self.make()
                self.show()
            else:
                raise AttributeError(f"{cls.__name__} has no __init__ method")

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
