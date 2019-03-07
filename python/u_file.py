import os 
import os.path 
import shutil


def create_file():
	pass


def open_file():
	pass


def open_file():
	pass


def read_file():
	src = "./temp/u_file.json"
	fp = open(src, 'r')
	print fp.read()
	fp.close()


def write_file():
	target = "./temp/u_file.json"
	fp_target = open(target, 'w')
	fp_target.write("{}")
	fp_target.close()


def	copy_file():
	src = "./temp/u_file.json"
	target = "./temp/u_file_c.json"
	shutil.copy(src,  target)


def remove_file():
	try:
		target = "./temp/u_file.json"
		os.remove(target)
	except Exception, e:
		print "Failed remove file"
		print e
	else:
		print "Failed remove file"
	finally:
		pass


def main():
	create_file()
	open_file()
	write_file()
	read_file()
	copy_file()
	remove_file()


if __name__ == '__main__':
	main()