import sys

if len(sys.argv) == 1 or sys.argv[1] == "/?":
    print(
        """
    이 프로그램의 사용 방법은
    도스 명령창에서 python subtract.py <인수 1> <인수 2>와 같습니다
    <인수 1>이 "/?"일 경우에는 도움말을 출력합니다
    <인수 1>과 <인수 2>가 정수일 경우에는 <인수 1>에서 <인수 2>를 뺀 값을 출력합니다
    """
    )

else:
    print(f"{sys.argv[1]} - {sys.argv[2]} =  {int(sys.argv[1]) - int(sys.argv[2])}")
