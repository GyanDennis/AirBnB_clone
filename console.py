class ClassName:
    instances = {}

    def __init__(self, id, data):
        self.id = id
        self.data = data
        ClassName.instances[id] = self

    @classmethod
    def update(cls, id, new_data):
        instance = cls.instances.get(id)
        if instance:
            instance.data.update(new_data)
        else:
            raise ValueError("Instance with ID {} not found.".format(id))
