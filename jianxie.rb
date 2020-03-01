# encoding: utf-8
require 'ruby-pinyin'

# jj,1=建军
File.open("./Phrases.ini","w") do |f|
    File.readlines("./name.txt", :encoding => 'UTF-8').each do |line|
        phrase = PinYin.abbr(line)+',1='+line
        f.puts phrase
    end
end