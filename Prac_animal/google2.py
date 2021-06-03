from google_images_download import google_images_download   #importing the library
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"조지 클루니,주 드로,방탄소년단 진,라이언 고슬링,소지섭,존박,김우빈,잭 에프론,송중기,조정석,서강준,데이비드 베컴,김종국,이병헌,지드래곤,강다니엘,저스틴 팀버레이크,제라드 버틀러,브래들리 쿠퍼,현빈,방탄소년단 뷔","limit":50,"print_urls":True, "format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images