import json


def json2file():
	json_obj = {"name":"john", "sex":"male"}
	json_str = json.dumps(json_obj, indent=4)

	target = "./temp/u_json.json"
	fp_target = open(target, 'w')
	fp_target.write(json_str)
	fp_target.close()

	print "json obj write to: " + target


def file2json():
	src = "./temp/u_json.json"
	fp_src = open(src, 'r')
	obj = json.loads(fp_src.read())
	fp_src.close()

	print "json object from " + src + " is:" 
	print obj


def main():
	json2file()
	file2json()


if __name__ == '__main__':
	main()