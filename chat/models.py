from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
	eid = models.CharField(max_length=64, unique=True)


	def __str__(self):
	 return 'chatroom_' + self.eid


class ChatMessage(models.Model):
	room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
	user = models.CharField(max_length=64, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True, blank=True, db_index=True)
	text = models.TextField()
	sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE, blank=True, null=True)
	last_modified = models.DateTimeField(auto_now=True, blank=True)


	def to_data(self):
		out = {}
		out['id'] = self.id
		out['from'] = self.user
		out['date'] = self.date
		out['text'] = self.text
		return out

	def __str__(self):
		return self.text
