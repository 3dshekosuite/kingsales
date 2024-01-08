Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... # استبدل 'path/to/your/app' بالمسار الفعلي لتطبيق Flask الخاص بك
... path = '/home/shekozo/mysite'
... if path not in sys.path:
...     sys.path.append(path)
... 
... from your_flask_app import app as application  # استبدل 'your_flask_app' بأسم ملف Flask الرئيسي الخاص بك
... 
