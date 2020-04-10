class Median:
    def __init__(self):
        pass

    @staticmethod
    def media(data):
        whole_data = len(data)
        sorted_data = sorted(data)
        return (sum(s[whole_data // 2 - 1:whole_data // 2 + 1]) / 2.0, s[whole_data // 2])[whole_data % 2] if whole_data else None
