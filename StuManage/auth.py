from StuManage.studentManage.models import Administer

class AdministerBackend:
	def authenticate(self, username=None, password=None):  
        		try:  
            		user = Administer.objects.get(username=username)  
        		except Administer.DoesNotExist:  
            		pass  
        		else:  
            		if user.check_password(password):  
                			return user  
        		return None  
   
    	def get_user(self, user_id):  
        		try:  
            		return Administer.objects.get(pk=user_id)  
        		except Administer.DoesNotExist:  
            		return None  