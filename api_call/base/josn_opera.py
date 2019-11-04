# coding=utf-8

"""
    json操作
"""

import json


class JsonOpera:
    def __init__(self):
        pass

    # 写入数据
    def write_json(self, data):
        # data  type ->(dict)

        if not isinstance(data, dict):
            raise TypeError('{} most is dict '.format(data))

        try:
            with open("auto.json", "w") as f:
                json.dump(data, f, indent=4, ensure_ascii=False, sort_keys=True, encoding='utf-8')
        except Exception as e:
            print(e)

    # 读取json数据
    def read_josn(self):
        """
        :return: dict
        """
        try:
            with open("auto.json", "r") as f:
                data = json.load(f, encoding='utf8')
                return data
        except Exception as err:
            print(err)
            return None

    # 追加数据
    def add_json(self, data):
        """

        :param data: dict
        :return:
        """
        if not isinstance(data, dict):
            raise TypeError('{} most is dict '.format(data))

        raw = self.read_josn()
        if raw is None:
            raw = dict()
        raw.update(data)  # 合并两个字典
        self.write_json(raw)


if __name__ == '__main__':
    t = {"a": "1"}
    # b = {"k": {"b": "2"}}
    d = {"k": [{"p": "2"}]}

    j = JsonOpera()
    j.write_json(t)
    # j.add_json(b)
    j.add_json(d)
    d = j.read_josn()
    print(d.get(u"k"))
