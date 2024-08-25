## Goal
A service that a proxy server make user have free and large size of cloud 
by connecting free Cloud Services

### Practice
- How does server work? [Completed]
> https://woolbro.tistory.com/29 

- How to implement the Proxy server? [Completed]
> https://velog.io/@adduci/%EC%9E%90%EB%B0%94%EC%9D%98-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9D%EC%8B%9C 

- Make Client & Server Class
> https://supermemi.tistory.com/entry/Python-3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%81%B4%EB%9E%98%EC%8A%A4%EC%9D%98-super-%EC%97%90-%EB%8C%80%ED%95%B4-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90-superinit-super%EC%9D%98-%EC%9C%84%EC%B9%98

### Implement
Make Machine Learning model that distribute resources(server, storage and so on) by considering network traffic and make it work on the service.




## AWS (EC2, RDS, VPC)
- 빌드
> https://velog.io/@kyj311/AWS-EC2-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0 
- InBound & OutBound
> https://repost.aws/ko/knowledge-center/ec2-block-or-allow-ips
- EC2 Ochestration (feat. kubernetes)
> https://bosungtea9416.tistory.com/entry/AWS-AWS-ECS-%EB%B0%8F-EKS-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC-EC2-%EB%B0%A9%EC%8B%9D-Fargate-%EB%B0%A9%EC%8B%9D

- Process
    - EC2 인스턴스 생성
    - VPC 인바운드 아웃바운드 제한
    - Elastic IP로 고정 IP 설정
        - 포트 22(SSH)가 모든 IPv4 주소에 개방되어 있음
        포트 22(SSH)는 현재 보안 그룹의 인바운드 규칙에 0.0.0.0/0으로 표시된 모든 IPv4 주소에 개방되어 있습니다. 보안을 강화하려면 3.16.146.0/29 리전의 EC2 인스턴스 연결 서비스 IP 주소에만 액세스하도록 제한하는 것이 좋습니다. -> AWS(US) 네트워크 대역폭인듯하다.
    - ssh 접속(?)

## Jenkins (CI/CD)
- What is Jenkins? 
> https://velog.io/@kakdark/%EC%A0%A0%ED%82%A8%EC%8A%A4
- Jenkins push to EC2
> https://bosungtea9416.tistory.com/entry/AWS-EC2-%EC%97%90-Jenkins-%EC%84%A4%EC%B9%98-%EB%B0%8F-default-%ED%8F%AC%ED%8A%B8-%EB%B3%80%EA%B2%BD
- Jenkins with Kubernetes(EKS)
> https://wlsdn3004.tistory.com/63#google_vignette
- Jenkins CI/CD pipeline
> https://velog.io/@uiop5487/Jenkins-CICD-Pipeline-%EA%B5%AC%EC%B6%95 
> https://kjw1313.tistory.com/83

### puTTy Connect
> https://velog.io/@spamdong/PuTTy-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95
-> 하지만 macOS 접근을 위해서 .pem 키 다운 -> ssh .ppk 키 변환 가능 (with. puTTygen)

------------
PuTTy 설치 및 사용법
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.html

AWS: PuTTY를 사용하여 Linux 인스턴스에 연결
https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/connect-linux-inst-from-windows.html

단축어 활용:리눅스 서버와의 연결
https://gorgeouskid.tistory.com/32

Amazon EC2 Instance Connect를 통해 EC2 인스턴스에 대한 SSH 연결하기
https://aws.amazon.com/ko/blogs/korea/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/