import json
import operator


def points_add(ign, points):
	print(f'Passed ign {ign} with {points} amount of season points.')
	with open('data.json', 'r') as data_file:
		json_file = json.load(data_file)

	try:
		old_value = json_file[ign]
		json_file[ign] = old_value + int(points)
		emote = '🆗'
	except KeyError:
		json_file[ign] = int(points)
		emote = '🛐'

	with open('data.json', 'w') as data_file:
		json.dump(json_file, data_file, indent=4)

	return emote


def points_show(ign):
	print(f'Passed {ign} to show amount of season points.')
	with open('data.json', 'r') as data_file:
		json_file = json.load(data_file)
	info = json_file[ign]
	out = f'Player **{ign}** contributed **{info}** season points.'
	return out


def leaderboard_show():
	print('Leaderboard requested.')
	with open('data.json', 'r') as data_file:
		json_file = json.load(data_file)

	leaderboard_dict = dict(sorted(json_file.items(), key=operator.itemgetter(1), reverse=True))
	leaderboard_ign_list = list(leaderboard_dict.keys())
	print(leaderboard_ign_list)
	embed_description = f'1. **{leaderboard_ign_list[0]}** : {leaderboard_dict[leaderboard_ign_list[0]]}\n' \
	                    f'2. **{leaderboard_ign_list[1]}** : {leaderboard_dict[leaderboard_ign_list[1]]}\n' \
	                    f'3. **{leaderboard_ign_list[2]}** : {leaderboard_dict[leaderboard_ign_list[2]]}\n' \
	                    f'4. **{leaderboard_ign_list[3]}** : {leaderboard_dict[leaderboard_ign_list[3]]}\n' \
	                    f'5. **{leaderboard_ign_list[4]}** : {leaderboard_dict[leaderboard_ign_list[4]]}\n' \
	                    f'6. **{leaderboard_ign_list[5]}** : {leaderboard_dict[leaderboard_ign_list[5]]}\n' \
	                    f'7. **{leaderboard_ign_list[6]}** : {leaderboard_dict[leaderboard_ign_list[6]]}\n' \
	                    f'8. **{leaderboard_ign_list[7]}** : {leaderboard_dict[leaderboard_ign_list[7]]}\n' \
	                    f'9. **{leaderboard_ign_list[8]}** : {leaderboard_dict[leaderboard_ign_list[8]]}\n' \
	                    f'10. **{leaderboard_ign_list[9]}** : {leaderboard_dict[leaderboard_ign_list[9]]}\n' \
	                    f'11. **{leaderboard_ign_list[10]}** : {leaderboard_dict[leaderboard_ign_list[10]]}\n' \
	                    f'12. **{leaderboard_ign_list[11]}** : {leaderboard_dict[leaderboard_ign_list[11]]}\n' \
	                    f'13. **{leaderboard_ign_list[12]}** : {leaderboard_dict[leaderboard_ign_list[12]]}\n' \
	                    f'14. **{leaderboard_ign_list[13]}** : {leaderboard_dict[leaderboard_ign_list[13]]}\n' \
	                    f'15. **{leaderboard_ign_list[14]}** : {leaderboard_dict[leaderboard_ign_list[14]]}\n' \
	                    f'16. **{leaderboard_ign_list[15]}** : {leaderboard_dict[leaderboard_ign_list[15]]}\n' \
	                    f'17. **{leaderboard_ign_list[16]}** : {leaderboard_dict[leaderboard_ign_list[16]]}\n' \
	                    f'18. **{leaderboard_ign_list[17]}** : {leaderboard_dict[leaderboard_ign_list[17]]}\n' \
	                    f'19. **{leaderboard_ign_list[18]}** : {leaderboard_dict[leaderboard_ign_list[18]]}\n' \
	                    f'20. **{leaderboard_ign_list[19]}** : {leaderboard_dict[leaderboard_ign_list[19]]}\n'
	return leaderboard_dict, embed_description


def ign_delete(ign):
	print(f'{ign} is about to be deleted from leaderboard')
	with open('data.json', 'r') as data_file:
		json_file = json.load(data_file)

	del json_file[ign]

	with open('data.json', 'w') as data_file:
		json.dump(json_file, data_file, indent=4)
