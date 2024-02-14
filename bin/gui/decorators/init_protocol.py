def init_protocol(init):
    def decorator(self, *args, **kwargs):
        init(self, *args, **kwargs)
        self.post_setup()
        self.make()
        self.show()

    return decorator
