# encoding: utf-8
require 'ruby-pinyin'
INPUT_FILE="./fenci_output_result.txt"
# jj,1=建军
File.open("./Phrases.ini","w") do |f|
    File.readlines(INPUT_FILE, :encoding => 'UTF-8').each do |line|
    	words=line.split(',')
    	words.each  {|x|phrase = PinYin.abbr(x.strip)+',1='+x.strip ; f.puts phrase}
    end
end