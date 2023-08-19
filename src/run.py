import sys
sys.path.append('/opt/render/project/src')  # このパスがapp.pyとanimal.pyが存在するディレクトリを指している

from app import app

if __name__ == '__main__':
    app.run()