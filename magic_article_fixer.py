def magic_article_fixer(article_path):
	with open(article_path, 'w+') as f:
		article = f.read()

	split = article.split()

	def adverb_counter(split):
		count = 0
		locations = []
		useless_words = ['so', 'very', 'just', 'way', 'much']
		for i, word in enumerate(split):
			if item[-2:] == 'ly' or if item in useless_words:
				counter += 1
				locations.append(i)
		return count, locations

	adv_count, adverb_locations = adverb_counter(split)

	for loc in adverb_locations:
		del split[loc]

	print "You have {} adverbs. Here are their locations {}.".format(adv_count, adv_locations)

	return " ".join(split) # TODO: Make split smart and join smart WRT. punctuation

	