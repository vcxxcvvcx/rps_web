#클래스와 인스턴스 - 소셜미디어 회원정보 및 게시물관리
class Member: # 멤버라는 클라스 를 정의 함
 
    def __init__(self, name, username, password): #인스턴스 속성 초기화 메서드 / 셀프는 인스턴스자신, 네임, 유저네임, 패스워드는 사용자로부터입력받음
        self.name = name #매서드 내에서 네임의 값을 인스턴스의 속성으로 설정
        self.username = username
        self.password = password

    def display(self): # 회원정보 출력 매서드
        print(f"회원 이름: {self.name}, 회원 아이디: {self.username}")


class Post: #포스트 클라스 정의
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = [ ] # 빈 리스트 생성 - 이 리스트에 회원정보 저장

# 회원 인스턴스 생성 및 리스트에 추가
members.append(Member("박씨", "park", "1234")) #어펜드 메서드로 리스트에 요소 추가
members.append(Member("혜씨", "hye", "5678"))
members.append(Member("진씨", "jin", "9012"))

# 회원 이름 출력 - 디스플레이 메서드 호출
print("회원 이름:")
for member in members:
    member.display()

posts = [ ] # 빈 리스트 생성 -포스트에 게시물 저장

# 게시물 인스턴스 생성 및 리스트에 추가
posts.append(Post("첫 번째 게시물", "과제가 어렵다", "park"))
posts.append(Post("두 번째 게시물", "파이썬 어렵다", "hye"))
posts.append(Post("세 번째 게시물", "코딩은 어렵다", "jin"))
posts.append(Post("네 번째 게시물", "과제가 쉽다", "park"))
posts.append(Post("다섯 번째 게시물", "파이썬 쉽다", "park"))
posts.append(Post("여섯 번째 게시물", "코딩은 쉽다", "hye"))
posts.append(Post("일곱 번째 게시물", "과제를 하지 말까?", "hye"))
posts.append(Post("여덟 번째 게시물", "파이썬 하지 말까?", "jin"))
posts.append(Post("아홉 번째 게시물", "코딩을 하지 말까?", "jin"))

# 특정 유저가 작성한 게시글 제목 출력
print("\n박씨가 작성한 게시글 제목:") #\n줄 띄우기
for post in posts:
    if post.author == "park":
        print(post.title, ":", post.content)

# 특정 단어가 content에 포함된 게시글 제목/내용 출력
print("\n과제가 포함된 게시글 제목:")
for post in posts:
    if "과제" in post.content:
        print(f"{post.title} : {post.content}")
       
