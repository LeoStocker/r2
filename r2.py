#讀取檔案
def read_file(filename):
	lines=[]
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for c in f:
			lines.append(c.strip())
	return lines

# 轉換檔案
def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '圖片':
				allen_image_count += 1
			elif s[2] == '貼圖':
				allen_sticker_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name =='Viki':
			if s[2] == '圖片':
				viki_image_count += 1
			elif s[2] == '貼圖':
				viki_sticker_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
		print(s)
	print('allen說了', allen_word_count, '個字', '、', '傳了', allen_sticker_count, '個貼圖', '傳了', allen_image_count, '張圖片')
	print('viki說了', viki_word_count, '個字', '、', '傳了', viki_sticker_count, '個貼圖', '傳了', viki_image_count, '張圖片')

# 寫入檔案
def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')
#主程式
def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)
	#write_file('output.txt', lines)
main()