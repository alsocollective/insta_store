from django.db import models
from django.template.defaultfilters import slugify
import shopify,json,requests
from django.conf import settings
from django.contrib.auth.models import User


class Stores(models.Model):
	website = models.CharField(max_length=100,unique=True,blank=True,null=True)
	authCode = models.CharField(max_length=40,unique=True,blank=True,null=True)

	instagram_account = models.CharField(max_length=100,blank=True,null=True)
	instagram_userId = models.CharField(max_length=100,blank=True,null=True)

	custom_text_before = models.TextField(max_length=3000,blank=True,null=True)
	custom_text_after = models.TextField(max_length=3000,blank=True,null=True)
	
	wrapper_text_before = models.TextField(max_length=3000,default='<div class="instagramphoto" style="background-image:url(')
	wrapper_text_after = models.TextField(max_length=3000,default=')"></div>')
	
	user = models.ForeignKey(User,blank=True,null=True) 

	def save(self,*args, **kwargs):
		if not self.instagram_userId:
			self.instagram_userId = self.getUserId()
		self.updateStore()			
		super(Stores, self).save(*args, **kwargs)
	

	def __unicode__(self):
		return self.website

	def checkIfPageAlreadyExists(self):
		for page in shopify.Page.find():
			if(page.title == "instagram generator page"):
				return page
		return False

	def getUserId(self):
		user_id = self.instagram_account
		if not user_id:
			return None
		address = "https://api.instagram.com/v1/users/search?q=%s&client_id=f6f99af9459c462d90e826d5893b61f7"%user_id
		data = json.loads(requests.get(address).content)
		return data["data"][0]["id"]

	def retriveInstagramFeed(self):
		user_id = self.instagram_userId
		address = "https://api.instagram.com/v1/users/%s/media/recent/?client_id=f6f99af9459c462d90e826d5893b61f7"%user_id

		data = json.loads(requests.get(address).content)

		out = ""
		for image in data["data"]:
			out += "%s%s%s" %(self.wrapper_text_before,image["images"]["standard_resolution"]["url"],self.wrapper_text_after)
		return out

	def updateStore(self):
		session = shopify.Session(self.website,self.authCode)
		shopify.ShopifyResource.activate_session(session)
		page = self.checkIfPageAlreadyExists()

		if not page:
			page = shopify.Page.create({"title":"instagram generator page"})

		page.body_html = "%s %s %s"%(self.custom_text_before, self.retriveInstagramFeed(), self.custom_text_after)
		page.save()


from django.forms import ModelForm

class StoresForm(ModelForm):
	class Meta:
		model = Stores
		fields = '__all__'		