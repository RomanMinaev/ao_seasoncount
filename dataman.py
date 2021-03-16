import json
import operator
import datetime


def log_entry(ign, mark, caller, sp=0):  # UTC:datetime.datetime.utcnow()

	sp = str(sp)
	with open('logs.json', 'r') as logs:
		json_logs = json.load(logs)
	try:
		raiser = json_logs[ign]
	except KeyError:
		mark = 'c'

	if mark == 'c':
		with open('logs.json', 'r') as logs:
			json_logs = json.load(logs)

		json_logs[ign] = {
			"CREATED": {
				"TIME": str(datetime.datetime.utcnow()),
				"BY": caller
			},
			"COUNTER": 0
		}

		if sp != 0:
			opened_ign = json_logs[ign]
			counter = opened_ign["COUNTER"]
			opened_ign["COUNTER"] = opened_ign["COUNTER"] + 1
			entry_name = "ENTRY_" + str(counter)
			opened_ign[entry_name] = {
				"TIME": str(datetime.datetime.utcnow()),
				"BY": caller,
				"CHANGE": sp
			}

		with open('logs.json', 'w') as logs:
			json.dump(json_logs, logs, indent=4)

		return f"New log entry was created for {ign}"

	if mark == 'w':
		with open('logs.json', 'r') as logs:
			json_logs = json.load(logs)

		opened_ign = json_logs[ign]
		counter = opened_ign["COUNTER"]
		opened_ign["COUNTER"] = opened_ign["COUNTER"] + 1
		entry_name = "ENTRY_" + str(counter)
		opened_ign[entry_name] = {
			"TIME": str(datetime.datetime.utcnow()),
			"BY": caller,
			"CHANGE": sp
		}

		with open('logs.json', 'w') as logs:
			json.dump(json_logs, logs, indent=4)

		return f"New log entry was added for {ign}"

	if mark == 'd':
		with open('logs.json', 'r') as logs:
			json_logs = json.load(logs)

		opened_ign = json_logs[ign]
		opened_ign["DELETED"] = {
			"TIME": str(datetime.datetime.utcnow()),
			"BY": caller
		}

		with open('logs.json', 'w') as logs:
			json.dump(json_logs, logs, indent=4)

		pass

	return f"{ign} was deleted, saved to logs"


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


def logs_show(ign):
	with open("logs.json", 'r') as data_file:
		json_file = json.load(data_file)

	try:
		opened_ign = json_file[ign]
	except KeyError:
		return "Participant was not added yet."
	try:
		DELETED = opened_ign["DELETED"]
		is_deleted = True
	except KeyError:
		is_deleted = False
	try:
		CREATED = opened_ign["CREATED"]
	except KeyError:
		CREATED = {
			"TIME": "NO INFO",
			"BY": "NO INFO"
		}
	embed_body = f'**FIRST ADDED BY:** {CREATED["BY"]} , **AT:** {CREATED["TIME"].split(".")[0]}\n' \
	             f'\n'
	if is_deleted:
		embed_body = embed_body + f'**DELETED BY:** {DELETED["BY"]} , **AT:** {CREATED["TIME"].split(".")[0]}\n' \
		                          f'\n'
	count = int(opened_ign["COUNTER"])
	for i in range(count):
		build_key = "ENTRY_" + str(i)
		ENTRY = opened_ign[build_key]
		embed_body = embed_body + f'{ENTRY["CHANGE"]} , **BY:** {ENTRY["BY"]} , **AT:** {ENTRY["TIME"].split(".")[0]}\n' \
		                          f'\n'

	return embed_body


def leaderboard_show():
	print('Leaderboard requested.')
	with open('data.json', 'r') as data_file:
		json_file = json.load(data_file)

	leaderboard_dict = dict(sorted(json_file.items(), key=operator.itemgetter(1), reverse=True))
	leaderboard_ign_list = list(leaderboard_dict.keys())
	print(leaderboard_ign_list)
	embed_description = ''
	for i in range(len(leaderboard_ign_list)):
		a = f'{i+1}. **{leaderboard_ign_list[i]}** : {leaderboard_dict[leaderboard_ign_list[i]]}\n'
		embed_description = embed_description + a

	return leaderboard_dict, embed_description


def ign_delete(ign):
	print(f'{ign} is about to be deleted from leaderboard')
	with open('data.json', 'r') as data_file:
		json_file = json.load(data_file)

	del json_file[ign]

	with open('data.json', 'w') as data_file:
		json.dump(json_file, data_file, indent=4)

