# coding=utf-8


class TxtOpera:

    def __init__(self):
        pass

    # 读取txt数据 1
    def read_txt(self):
        try:
            with open('token.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入数据
    def write_txt(self, data):
        try:
            with open('token.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')

    # 读取txt数据2
    def read_txt_access(self):
        try:
            with open('access_token.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入数据
    def write_txt_access(self, data):
        try:
            with open('access_token.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')


    # 读取txt数据3
    def read_txt_cookies(self):
        try:
            with open('cookies.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入数据运行当前路径地下
    def write_txt_cookies(self, data):
        try:
            with open('cookies.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')


    # 读取txt数据3
    def read_txt_cookies_p(self):
        try:
            with open('cookies_p.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入数据
    def write_txt_cookies_p(self, data):
        try:
            with open('cookies_p.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')


    # 读取txt数据3
    def read_txt_cookies_x(self):
        try:
            with open('cookies_x.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入数据
    def write_txt_cookies_x(self, data):
        try:
            with open('cookies_x.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')
            
            
    # # 读取AuthorizationToken数据
    # def read_txt_authorizationToken(self):
    #     try:
    #         with open('../authorizationToken.txt', 'r') as f:
    #             txt = f.read()
    #             return txt
    #     except IOError:
    #         print('')
    #
    # # 写入AuthorizationToken数据
    # def write_txt_authorizationToken(self, data):
    #     try:
    #         with open('../authorizationToken.txt', 'w') as f:
    #             f.write(data)
    #
    #     except IOError:
    #         print('')





  #   # 读取AuthorizationToken数据
  #   def read_txt_authorizationToken(self):
  #       try:
  #           with open('../../data_struct/authorizationToken.txt', 'r') as f:
  #               txt = f.read()
  #               return txt
  #       except IOError:
  #           print('')
  #
  #   # 写入AuthorizationToken数据
  #   def write_txt_authorizationToken(self, data):
  #       try:
  #           with open('../../data_struct/authorizationToken.txt', 'w') as f:
  #               f.write(data)
  #
  #       except IOError:
  #           print('')
  #
  # #读取tag id
  #   def read_tag_id(self):
  #       try:
  #           with open('../../data_struct/create_tag_id.txt', 'r') as f:
  #               txt = f.read()
  #               return txt
  #       except IOError:
  #           print('')
  #
  #   # 写入AuthorizationToken数据
  #   def write_tag_id(self, data):
  #       try:
  #           with open('../../data_struct/create_tag_id.txt', 'w') as f:
  #               f.write(data)
  #
  #       except IOError:
  #           print('')
  #
  #  #读取tag group
  #   def read_tag_group(self):
  #       try:
  #           with open('../../data_struct/create_tag_group.txt', 'r') as f:
  #               txt = f.read()
  #               return txt
  #       except IOError:
  #           print('')
  #
  #       # 写入AuthorizationToken数据
  #
  #   def write_tag_group(self, data):
  #       try:
  #           with open('../../data_struct/create_tag_group.txt', 'w') as f:
  #               f.write(data)
  #
  #       except IOError:
  #           print('')
















    # 读取AuthorizationToken数据
    def read_txt_authorizationToken(self):
        try:
            with open('../authorizationToken.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入AuthorizationToken数据
    def write_txt_authorizationToken(self, data):
        try:
            with open('../authorizationToken.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')

  #读取tag id
    def read_tag_id(self):
        try:
            with open('../create_tag_id.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

    # 写入AuthorizationToken数据
    def write_tag_id(self, data):
        try:
            with open('../create_tag_id.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')

   #读取tag group
    def read_tag_group(self):
        try:
            with open('../create_tag_group.txt', 'r') as f:
                txt = f.read()
                return txt
        except IOError:
            print('')

        # 写入AuthorizationToken数据

    def write_tag_group(self, data):
        try:
            with open('../create_tag_group.txt', 'w') as f:
                f.write(data)

        except IOError:
            print('')


