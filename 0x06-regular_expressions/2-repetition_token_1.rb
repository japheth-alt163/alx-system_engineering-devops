#!/usr/bin/env ruby
# The above line specifies that the script should be interpreted by the Ruby interpreter.

# Output the substring that matches the regular expression /hb{0,1}tn/
puts ARGV[0].scan(/hb{0,1}tn/).join
