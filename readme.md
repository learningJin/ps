# 문제풀이 던져놓는 저장소

### 구조
* 폴더 : 날짜별 생성. 파일명은 YYMMDD
* 파일 : 문제별 생성. 파일명은 문제번호 ( 각 파일안에 백준 링크와 문제이름 기재 )


### node.js I/O
[내용 출처](https://mingcoder.me/2020/01/15/Programming/etc/acmicpc-nodejs-input/)
``` javascript
var fs = require("fs")

// 문자 하나
var input = fs.readFileSync("/dev/stdin").toString()

// 한 칸 띄어쓰기로 구분
// input[0], input[1] 배열에서 꺼내쓰면 된다.
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")

// 줄바꿈으로 구분
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n")

// 만약 인풋값이 숫자라면
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(function(a) {
    return +a
  })
```