class Singleton:
    # Private class variable
    _instance = None

    @staticmethod
    def get_intance():
        if not Singleton._instance:
            return Singleton()
        return Singleton._instance

    def __init__(self) -> None:
        if Singleton._instance:
            raise Exception("Instance already running!!")
        Singleton._instance = self
        print("New instance created successfully!!")


if __name__ == "__main__":
    print(Singleton.get_intance())
    print(Singleton.get_intance())
