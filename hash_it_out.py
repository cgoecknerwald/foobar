def answer(digest):
	message = [inverse(digest[0])]
	for i in range(1, 16):
		message.append(inverse(digest[i], message[i - 1]))
	return message

def inverse(digest_value, prev_message_value = 0):
	message_value = 1
	while (not (message_value % 129 == 0)):
		message_value = digest_value ^ prev_message_value
		digest_value += 256
	return message_value / 129

print (answer( [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165] ))