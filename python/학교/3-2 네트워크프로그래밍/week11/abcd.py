import argparse

parser = argparse.ArgumentParser(prog='abcd.py',
                                 description='이것은 명령행 파라미터를 시험하는 것.') #step 1

parser.add_argument('filename1', help='원본 파일/경로') # step 2
parser.add_argument('filename2', help='복사본 파일/경로') # step 2
parser.add_argument('-p','--port', required=True, help='포트 번호')
parser.add_argument('-a', '--addr', required=True, help='서버 IP')

args = parser.parse_args() # step 3
print(args.filename1)
print(args.filename2)
print(args.port)
print(args.addr)