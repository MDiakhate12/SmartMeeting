from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
	eid = models.CharField(max_length=64, unique=True)

class ChatMessage(models.Model):
	room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='messages', blank=True, null=True)
	date = models.DateTimeField(auto_now=True, db_index=True)
	text = models.TextField()

	def to_data(self):
		out = {}
		out['id'] = self.id
		out['from'] = self.user
		out['date'] = self.date
		out['text'] = self.text
		return out
