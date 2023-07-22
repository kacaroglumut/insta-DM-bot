# insta-DM-bot
The project will be helpful to you for send automatically message in Instagram with bot

# Instagram Direct Message Bot

İnstagram botu ile doğrudan ve grup mesajı gönderin. Python 3.7.2 ve Selenium ile çalışın.


## **Örnek** :

```javascript
from instadm import InstaDM

if __name__ == '__main__':
	# Auto login
	insta = InstaDM(username='kullanıcı adı', password='şifre', headless=False)
	
	# Send message
	insta.sendMessage(user='target users', message='static message !')
	
	# Send message
	insta.sendGroupMessage(users=['group_user_1', 'group_user_2'], message='static message !') 
 
```



## InstaPY Kütüphanesi ile Çalışma:

Constructure’da `ınstapy_workspace` parametresini kullanın:


```javascript
from instadm import InstaDM

if __name__ == '__main__':
	# Auto login
	insta = InstaDM(
		username='your_username',
		password='your_password',
		headless=False,
		instapy_workspace='workspace/'
	)
```


Eğer sistemde mesaj yoksa InstDM içerisinde sanal tablo oluşturup adını `message` olarak verin.

```javascript
CREATE TABLE "message" (
	"username"	TEXT NOT NULL UNIQUE,
	"message"	TEXT DEFAULT NULL,
	"sent_message_at"	TIMESTAMP
);
```


## InstPY Kütüphanesinin Dashboard’u ile Çalışın

InstaDM, [InstaPy Dashboard'un değiştirilmiş bir sürümüyle çalışır.](https://github.com/CamTosh/instapy-dashboard)


> Instapic Dashboard, İnstagram hesaplarının ilerlemesini ve tarayıcıdaki gerçek zamanlı InstaPy günlüklerini görselleştirmek için @converge tarafından geliştirilen Açık Kaynaklı bir projedir.



