FROM alpine:3.7

WORKDIR /app
ENV GOPATH /go

# 빌드 시에만 필요한 라이브러리 및 도구 설치
RUN apk add --no-cache --virtual=build-deps go gcc g++

# 실행 시에도 필요한 라이브러리 및 도구 설치

# 애플리케이션 빌드해 실행 파일을 만듬
COPY . .
RUN GOOS=linux GOARCH=amd64 go build hello.go

# 빌드 시에만 필요한 라이브러리 및 도구 제거
RUN apk del --no-cache build-deps

CMD ["/hello"]