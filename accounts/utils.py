import random
import string

def random_string_generator_user(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def unique_user_id_generator(instance):
	user_new_id= random_string_generator_user()

	Klass= instance.__class__

	qs_exists= Klass.objects.filter(user_id=user_new_id).exists()
	if qs_exists:
		return unique_user_id_generator(instance)
	return user_new_id