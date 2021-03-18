#  Stat Bot Discord.py

# Try Import Libarys If Not Throw Exception
try:
	import json
	import discord
	import psutil
	import os
	from discord import Colour
except Exception as e:
	print("Could Not Import: " + str(e))

# Machine Data

# Free Memory Round Up To Decimal Place!
free_bytes = round(psutil.virtual_memory().free)
free_mb = round(psutil.virtual_memory().free / 1024 / 1024) # Divide bytes By 1024 2x For Megabytes
free_gb = round(psutil.virtual_memory().free / 1024 / 1024 / 1024)

# Total Memory
total_bytes = round(psutil.virtual_memory().total)
total_mb = round(psutil.virtual_memory().total / 1024 / 1024)
total_gb = round(psutil.virtual_memory().total / 1024 / 1024 / 1024)

# Total Memory Used
used_bytes = round(psutil.virtual_memory().used)
used_mb = round(psutil.virtual_memory().used / 1024 / 1024)
used_gb = round(psutil.virtual_memory().used / 1024 / 1024 / 1024)

# Client PID
pid = os.getpid()
calc = psutil.Process(pid) # Get Data About Our Pid
memoryUsage = round(calc.memory_info()[0] / 1024 / 1024)

client = discord.Client()


# Get CPU Load Avg
t1, t2, t15 = psutil.getloadavg() # Tuple 
CPU_USAGE = (t15/os.cpu_count()) * 100


# Get statistcs Of Process
def GrabStats(pid):
	pass

# Get All PIDS
'''
def GetAllProcesses():
	for proc in psutil.process_iter():
		try:
			procName = proc.name()
			procID = proc.pid
			print(procName , " <-> " , procID)
    	except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        	pass
'''
# Decode JSON
path = "config/config.json"
data = json.loads(open(path).read())
# Set Variables
token = data['token']
author = data['Author']
imglink = data['img_link']
prefix = data['prefix']

@client.event
async def on_ready():
	print("======================")
	print('Logged In As {0.user}'.format(client))
	print(f'We Are In {str(len(client.guilds))} Server(s)')
	print('Client ID {0.user.id}'.format(client))
	print("======================")


@client.event
async def on_message(message):
	if message.author == client.user:
		print(f"Ignored Input From Self!")
		return
	if message.content.startswith(prefix+"stats"):
		embed = discord.Embed(
			colour= Colour.orange(),
			title="Showing Machine Stats!")
		embed.set_footer(text=f"Made By {author}")
		embed.set_thumbnail(url=imglink)
		embed.add_field(name="Total Memory", value = f"```{total_mb}MB```")
		embed.add_field(name="Free Memory", value = f"```{free_mb}MB```")
		embed.add_field(name="Used Memory", value = f"```{used_mb}MB```\n")
		embed.add_field(name="Memory Percentage", value = f"```{psutil.virtual_memory().percent}%```")
		embed.add_field(name="Memory Usage", value = f"```{memoryUsage}MB```")
		embed.add_field(name="CPU Usage", value = f"```{psutil.cpu_percent(interval=1)}%```")
		await message.channel.send(embed=embed)
	
try:
	client.run(token)
except Exception as e:
	print("Something Has Gone Wrong! Error: " + e)