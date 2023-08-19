import sys
sys.path.append('/opt/render/project/src/src')  # このパスがapp.pyと同じディレクトリを指している

from app import app

if __name__ == '__main__':
    app.run()